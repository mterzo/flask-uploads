"""
Flask-Uploads
-------------
Flask-Uploads provides flexible upload handling for Flask applications. It
lets you divide your uploads into sets that the application user can publish
separately.

Links
`````
* `documentation <http://flask-uploads.readthedocs.io/en/latest/>`_
* `development version
  <https://github.com/maxcountryman/flask-uploads>`_


"""
from setuptools import setup


setup(
    name='Flask-Uploads',
    version='0.2.2',
    url='https://github.com/maxcountryman/flask-uploads',
    license='MIT',
    author='Matthew "LeafStorm" Frazier',
    author_email='leafstormrush@gmail.com',
    description='Flexible and efficient upload handling for Flask',
    long_description=__doc__,
    py_modules=['flask_uploads'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.8.0'
    ],
    tests_require='nose',
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
