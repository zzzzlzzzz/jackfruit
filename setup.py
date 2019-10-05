import setuptools
import re


with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fh:
    install_requires = fh.read().splitlines()


with open('jackfruit/_version.py', 'r') as fh:
    version = re.search(r'''__version__ = \'(.+)\'''', fh.read()).group(1)


setuptools.setup(
    name='jackfruit',
    version=version,
    author='Tosha',
    author_email='zzzzlzzzz@yandex.com',
    description='Generic views for python-telegram-bot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zzzzlzzzz/jackfruit',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
