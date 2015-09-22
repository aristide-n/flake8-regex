# coding: utf-8

from __future__ import with_statement
from setuptools import setup


def get_version(fname='flake8_regex.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.md',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name='flake8-regex',
    version=get_version(),
    description="Arbitrary regex checker, extension for flake8",  # noqa
    long_description=get_long_description(),
    keywords='flake8 regex',
    author='Aristide Niyungeko',
    author_email='aristide.niyungeko@gmail.com',
    url='https://github.com/aristiden7o/flake8-regex',
    license='GNU General Public License v2 (GPLv2)',
    py_modules=['flake8_regex'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'flake8_regex = flake8_regex:check_regex_patterns',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
