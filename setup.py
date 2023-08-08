"""
Sample setup.py file
"""
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="declare4py",
    version='{{VERSION_PLACEHOLDER}}',
    author="XXXX",
    author_email="fake@gmail.com",
    description="Python library to perform discovery, conformance checking and query checking of DECLARE constraints.",
    url="https://github.com/johndoe/my_package",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["logaut",
                      "packaging",
                      "mlxtend >= 0.20.0",
                      "pm4py >= 2.5.1",
                      "clingo >= 5.6.2",
                      "boolean.py",
                      "pandas >= 1.3.4"
                      ],
    keywords=['python', 'bpm', 'declare', 'process-mining', 'rule-mining', 'business-process-management',
              'declarative-process-models'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
