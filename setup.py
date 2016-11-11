import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'simple_spark_lib',
    version = '0.0.1',
    author = 'Shekhar Singh',
    author_email = 'shekhar.singh@msn.com',
    description = ('Simple Spark Lib'),
    license = '',
    keywords = ['Spark', 'Apache', 'Cassandra', 'PySpark'],
    url = 'https://github.com/rootcss/simple_spark_lib',
    packages=['simple_spark_lib'],
    long_description=read('README.md'),
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    scripts = [
        'scripts/simple-runner'
    ]
)
