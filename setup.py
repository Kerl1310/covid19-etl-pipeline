import os
import re

from setuptools import setup, find_packages

requires = [
    'boto3>=1.0.0'
]

setup(
    name='covid19-etl',
    version='1.0.0',
    description='An ETL processing pipeline for COVID-19 data using Python and cloud services',
    long_description=open('README.md').read(),
    author='Kyle Jones',
    url='https://github.com/Kerl1310/covid19-etl-pipeline',
    scripts=[],
    install_requires=requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)