from dd.cudd import BDD

class DataManager():
    def __init__(self, variables, dimension=20):
        super().__init__()
        self.variables = set(variables)
        self.dimension = dimension                                  # Dimension per variable 

        self.bdd = BDD()                                            # BDD Manager (dd/CUDD/Sylvan)
        self.bdd.declare(*['{}{}'.format(var, i) 
            for var in self.variables 
            for i in range(self.dimension)])

        self.size = {var: 0 for var in self.variables}              # Current size for variables
        self.dejavu = {var: dict() for var in self.variables}       # Dicts of values seen before

    def const(self, value):
        return self.bdd.true if value else self.bdd.false

    def encode(self, value, variable):

        if value == None:
            return self.bdd.false

        try:
            cube = self.dejavu[variable][value]
        except KeyError: # If the value is not seen before
            index = self.size[variable]

            # Bit-blasting integer-valued index
            d = {'{}{}'.format(variable, bit_index): bit_value == '1'
                    for (bit_index, bit_value) in zip(
                        range(self.dimension), 
                        "{0:0{length}b}".format(index, length=self.dimension)
                        )
                }

            cube = self.bdd.cube(d)
            self.dejavu[variable][value] = cube

            self.size[variable] = self.size[variable] + 1
            
        return cube

    def decode(self, value, variable):
        pass

