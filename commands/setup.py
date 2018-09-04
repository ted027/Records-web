from setuptools import setup, find_packages

setup(
    name='records-dev',
    packages=find_packages(),
    entry_points={'console_scripts': ['records-dev=records_dev.main:handle']},
    install_requires=['click', 'boto3', 'requests', 'bs4'])