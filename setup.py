from setuptools import setup, find_packages

setup(
    name="someRSAcode",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        'libnum',
        'gmpy2',
    ],
    author="kknncrypt",
    author_email="wargod2024@hotmail.com",
    description="Some standard methods of attack on RSA encryption have been implemented, such as the common mode attack, non-coprime modulus, low encryption index attack, etc.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="encryption RSA",
    url="https://github.com/blockcll/someRSAcode",
)
