from setuptools import setup, find_packages

setup(
    name='processingpipeline',
    packages=find_packages(exclude=['tests', 'tests.*']),
)
