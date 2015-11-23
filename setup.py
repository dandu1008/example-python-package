""" This module is provides the configuration and command line tools for
distributiing this exmaple project. """

from codecs import open
from setuptools import setup

with open('README.rst', 'r', 'utf-8') as f:
        readme = f.read()

install_requires = [
        'requests>=2.0'
        ]

setup(
    name='example-package',
    description='A typical example of a Python project',
    long_description=readme,
    # See PEP440 for valid version string schemes:
    # https://www.python.org/dev/peps/pep-0440/
    version='1.2.0',
    url='https://github.com/tylerdave/example-python-package',
    author='Dave Forgac',
    author_email='tylerdave@tylerdave.com',
    license='Public Domain',
    packages=['example_package'], # or use find_packages from setuptools
    # If distributing module(s) only, use py_modules instead of packages
    # py_modules=['example_module']
    install_requires=install_requires,
    extras_require={
        'dev': ['tox'],
        'test': ['coverage'],
        },
    package_data={
        'example_package': ['exmaple_package_data.dat'],
        },
    include_package_data=True,
    data_files=[
        ('example_data',['data/example_data.dat']),
        ],
    entry_points={
        'console_scripts': [
            'hello=example_package.cli:main',
            'get-example=example_package.cli:get_example',
            ],
        },
    # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    keywords='packaging example',
    )
