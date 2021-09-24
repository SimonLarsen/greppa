from setuptools import setup, find_packages
import greppa


setup(
    name="greppa",
    version=greppa.__version__,
    packages=find_packages(),
    install_requires=[
        "click",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "greppa = greppa.cli:cli"
        ]
    }
)
