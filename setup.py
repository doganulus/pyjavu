import os
import sys

from distutils.core import setup
from distutils import util

if __name__ == "__main__":
    path_to_parser = util.convert_path('pyjavu/parser')
    path_to_formalisms = util.convert_path('pyjavu/formalism')
    setup ( name = 'pyjavu',
            version='0.0.1',
            author='Dogan Ulus',
            author_email='doganulus@gmail.com',
            #url='http://github.com/doganulus/reelay/',
            package_dir = {
                'pyjavu': 'pyjavu',
                'pyjavu.parser': path_to_parser,
                'pyjavu.formalism': path_to_formalisms},
            packages=[
                "pyjavu",
                "pyjavu.parser",
                "pyjavu.formalism" 
            ],
            #scripts=['bin/re2cpp'],
            license='GPLv3+',
            classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'Intended Audience :: Science/Research',
                'Topic :: Scientific/Engineering',
                'Topic :: Scientific/Engineering :: Mathematics',
                'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                'Programming Language :: Python :: 3',
            ],
            description = 'A Python implementation of the monitoring tool DejaVu',
            # url='http://pypi.python.org/pypi/reelay/',
            # py_modules = ["reelay.classical"],
            python_requires='>=3',
            install_requires=[
                'dd',
                'pandas',
                'antlr4-python3-runtime'
            ],
            include_package_data=True,
    )

