""" This module is provides the configuration and command line tools for
distributiing this exmaple project. """

from setuptools import find_packages, setup

long_description = 'get this from README.rst' #TODO: get from README
install_requires = [
        'requests>=2.0'
        ]

setup(
    name='example-package',
    description='A minimal example of a Python project',
    long_description=long_description,
    # See PEP440 for valid version string schemes:
    # https://www.python.org/dev/peps/pep-0440/
    version='1.2.0',
    url='https://github.com/tylerdave/minimal-python-package',
    author='Dave Forgac',
    author_email='tylerdave@tylerdave.com',
    license='Public Domain',
    packages=find_packages(exclude=['docs', 'tests']),
    # If distributing module(s) only, use this instead of packages
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
