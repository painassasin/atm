from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="atm",
    version="0.0.1",
    author="Vadim Meshcheryakov",
    author_email="painassasin@icloud.com",
    description="Atm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/painassasin/atm",
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.9',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
