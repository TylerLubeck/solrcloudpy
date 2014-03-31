from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name = "solrcloudpy",
    version = "1.1.406",
    author = 'Didier Deshommes',
    author_email = 'dfdeshom@gmail.com',
    packages=find_packages(exclude=['ez_setup']),
    url='https://github.com/dfdeshom/solrcloudpy',
    license='LICENSE.txt',
    keywords='solr solrcloud',
    description='python library for interacting with SolrCloud ',
    long_description=long_description,
    include_package_data=True,
    platforms='any',
    entry_points = {
        'console_scripts': [
        'solrconsole = scripts.solrconsole:main [ip]']
        },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
        ],

    install_requires = ['requests == 2.2.1',],
    extras_require = {"ip": ['IPython == 1.2.0'] }, 
        )
