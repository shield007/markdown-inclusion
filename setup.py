from distutils.core import setup
import os
import sys
from setuptools import find_packages, setup

os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src'))

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
    py_modules=['myextension'],
    install_requires = ['markdown>=2.5'],
)
