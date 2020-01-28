import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(
    os.path.join(os.path.dirname(__file__), "lib", "sqlalchemymonitor", "__init__.py")
) as v_file:
    VERSION = (
        re.compile(r""".*__version__ = ["'](.*?)['"]""", re.S)
        .match(v_file.read())
        .group(1)
    )

setup(
    name='sqlalchemymonitor',
    version=VERSION,
    author="Lucas Limeira",
    author_email="lucasalveslm@gmail.com",
    description="A monitoring lib for SQLAlchemy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasalveslm/sqlalchemymonitor",
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )