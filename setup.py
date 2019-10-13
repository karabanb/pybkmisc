
from setuptools import setup, find_packages

PACKAGE_NAME = 'pybkmisc'
REQUIREMENTS_PATH = 'requirements.txt'
README_PATH = 'README.md'
VERSION = '0.1.0'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    url='https://github.com/karabanb/pybkmisc',
    author='Bartlomiej Karaban',
    author_email='bkarabands@gmail.com',
    install_requires=['numpy']
)
