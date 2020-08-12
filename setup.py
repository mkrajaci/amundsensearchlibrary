# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import os

from setuptools import setup, find_packages

__version__ = '2.4.2rc2'

requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name='amundsen-search',
    version=__version__,
    description='Search Service for Amundsen',
    url='https://github.com/lyft/amundsensearchlibrary.git',
    maintainer='Lyft',
    maintainer_email='amundsen-dev@lyft.com',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[],
    install_requires=requirements,
    python_requires=">=3.6"
)
