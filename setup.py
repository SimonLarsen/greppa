from setuptools import setup, find_packages
import pandas_grep


setup(
    name="pandas-grep",
    version=pandas_grep.__version__,
    packages=find_packages(),
    install_requires=[
        "click",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "pandas_grep = pandas_grep.cli:cli"
        ]
    }
)
