from setuptools import setup, find_packages

setup(
    name='processing',
    packages=find_packages(exclude=['tests', 'tests.*']),
)
