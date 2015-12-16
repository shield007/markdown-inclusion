from distutils.core import setup
import os
import sys
from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = []

setup(
    name='markdown-inclusion',
    description='This is plugin to extend python markdown and allow it include other markdown files.',
    author='John-Paul Stanford',
    author_email='John-Paul.Stanford@arm.com',
    url='https://github.com/shield007/markdown-inclusion',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    version='1.0',
    py_modules=['markdown_inclusion'],
    install_requires = ['markdown>=2.5'],
)
