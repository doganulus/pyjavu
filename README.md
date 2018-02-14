# PyJavu

`pyjavu` is an experimental package to generate sequential machines from formal specifications such as regular expressions.

# Install

This package requires `python3`,  `antlr4-python3-runtime`, `pandas` and the decision diagram package `dd`.

The easiest way to install `pyjavu` is to run the following command (that requires `git` installed in your system). 

    pip install git+https://github.com/doganulus/pyjavu.git

# Usage

Pattern Syntax:     
  
    Expr = a                   (Pandas column name)
         : Func(column_args)   (Custom function over columns)
         : Expr1 | Expr2       (Union)
         : Expr1 ; Expr2       (Concatenation)
         : Expr *              (Zero-or-more Repetition)
         : Expr +              (One-or-more Repetition)
         : Expr ?              (Zero-or-one Repetition)
         : exists{vars}(Expr)  (Existential quantification for comma-separated data variables)
         : (Expr)              (Grouping)

# Pattern matching over data frames using `pyjavu`

Consider a `pandas` `DataFrame` with data columns named `p1` and `p2`. 

    import numpy as np
    import pandas as pd
     
    from pyjavu.formalism import regexp_data as spec

    d = {
         'p1': [None, 'x', None,  'a',  None, 'a', 'b', None, 'c', 'c', 'c', None], 
         'p2': ['x', 'c',  None,  None, 'a',  'b', 'a',  'c',  'b', 'b', 'c', None]
        }
    df = pd.DataFrame(data=d)

We would like evaluate regular expressions with data such as  

    expression = r"exists{k}(k <= p2; k <= p1)"

which specifies a pattern such that there exists a data value `k` that observed at `p2[i]` and then the same value observed at `p1[i+1]`. Thus the concatenation operator `;` here means sequential composition of patterns as usual. The assignment operator `<=` stores the current value at left hand side in a BDD-based database (see References) with the key `k` to be retrieved later.

We evaluate this expression over the data frame `df` as follows:

    df = spec.eval(df, expression)

The resulting frame would the following data.

     [False, True, False, False, False, True, True, False, True, True, False, False, False]

Optionally, you can give a name to the expression

    named_expression = r"out = exists{k}(k <= p2; k <= p1)"

and can evaluate it in place as follows.

    df = regexp.eval(df, named_expression, inplace=True)

          p1    p2    out
    0   None     x  False
    1      x     c   True
    2   None  None  False
    3      a  None  False
    4   None     a  False
    5      a     b   True
    6      b     a   True
    7   None     c  False
    8      c     b   True
    9      c     b  False
    10     c     c  False
    11  None  None  False

Now you can see that `out` is `True` at a position if a data value, say `a` observed at `p2` in the previous step and now at `p1`. Thus, `out` holds at the endpoint of an instance of the pattern. This behavior is standard for pattern matchers.

Moreover, you can define custom functions over data columns to be evaluated point-wise and the resulting will be passed to the sequential machine. For that you need to pass your predicate as a local dictionary:

    def my_func(a, b):
        return (a or b)    
     
    df = spec.eval(df, 'my_predicate(p1, p2); p2', inplace=True, local_dict={'my_func' : my_func})

This regular expression matches a sequence where `p1` or `p2` holds and then `p2` holds at the next row.

# References

This package is a toy Python implementation of the temporal logic monitoring tool, `DejaVu`, introduced in [First order temporal logic monitoring with BDDs](https://doi.org/10.23919/FMCAD.2017.8102249). `PyJavu` does not support all features of `DejaVu` but extends its functionality with regular expressions.

The sequential machine construction from regular expressions is explained [here](https://arxiv.org/pdf/1801.08979.pdf).
