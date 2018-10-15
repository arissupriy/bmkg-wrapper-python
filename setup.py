from distutils.core import setup
from setuptools import find_packages

setup(
    name='bmkg-wrapper',
    version='0.1',
    url='https://github.com/arissupriy/bmkg-wrapper-python',
    author='Aris Supriyanto',
    packages=find_packages(exclude=['venv/','examples/', '.vscode/', 'wrapper.py']),
    install_requires=['beautifulsoup4==4.6.3', 'requests==2.19.1'],
    license='MIT'
)

