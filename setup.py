#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import (
    setup,
    find_packages,
    )

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as fp:
    README = fp.read()

with open(os.path.join(here, 'requirements/master.txt')) as fp:
    install_requires = map(lambda st: st.strip(), fp.readlines())

with open(os.path.join(here, 'requirements/test.txt')) as fp:
    test_require = map(lambda st: st.strip(), fp.readlines())

src = 'src'
packages = find_packages(src)
package_dir = {'': src}
package_data = {}


setup(
    name='sximon',
    version='0.1',
    url='https://github.com/TakesxiSximada/sximon',
    download_url='https://github.com/TakesxiSximada/sximon/archives/master.zip',
    license='See http://www.python.org/3.4/license.html',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description="sximon is not human.",
    long_description=README,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        ],
    platforms='any',
    packages=find_packages(),
    package_dir=package_dir,
    namespace_packages=[
        ],
    keywords='web wsgi bfg pylons pyramid',
    package_data=package_data,
    include_package_data=True,
    install_requires=install_requires,
    test_require=test_require,
    test_suite='sximon',
    entry_points='''
    [paste.app_factory]
    main = sximon:main
    [console_scripts]
    initialize_sximon_db = sximon.scripts.initializedb:main
    '''
    )
