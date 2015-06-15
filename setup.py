import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-raster-aggregation',
    version='0.1.7',
    packages=['raster_aggregation', 'raster_aggregation.migrations'],
    include_package_data=True,
    license='BSD',
    description='Zonal aggregation functionality for django-raster',
    long_description=README,
    url='https://github.com/geodesign/django-raster-aggregation',
    author='Daniel Wiesmann',
    author_email='daniel@urbmet.com',
    install_requires=[
        'Django>=1.8',
        'django-raster',
        'celery>=3.1.18'
    ],
    keywords=['django', 'raster', 'gis', 'gdal', 'celery', 'geo', 'spatial'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)