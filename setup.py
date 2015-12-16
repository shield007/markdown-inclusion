from distutils.core import setup
import os
import sys
from setuptools import find_packages, setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='markdown-inclusion',
    description='This is plugin to extend python markdown and allow it include other markdown files.',
    long_description=(read('Readme.md')),
    author='John-Paul Stanford',
    author_email='John-Paul.Stanford@arm.com',
    license='BSD',
    url='https://github.com/shield007/markdown-inclusion',
    include_package_data=True,
    version='1.0',
    py_modules=['mdx_inclusion'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = ['markdown>=2.5'],
)
