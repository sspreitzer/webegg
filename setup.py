from setuptools import setup, find_packages

setup(
    name = 'webegg',
    version = '0.0.1',
    description = 'Python webegg, run code from URL',
    url = 'https://github.com/sspreitzer/webegg',
    author = 'Sascha Spreitzer',
    author_email = 'sascha@spreitzer.ch',
    license = 'GPLv2',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
    ],
    keywords = 'webegg',
    install_requires=['pycurl'],
    package_dir={'':'src'},
    packages=find_packages('src'),
)
