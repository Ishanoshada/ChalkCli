from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='ChalkCli',
    version='0.1.0',
    author='Ishan Oshada',
    author_email='Ishan.kodithuwakku.official@gmail.com',
    description='A Python package for terminal text styling and coloring.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ishanoshada/ChalkCli',  
    packages=find_packages(),
     classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
