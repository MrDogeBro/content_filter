import setuptools

with open('pypi/README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='content-filter',
    version='1.0.4',
    author='MrDogeBro',
    author_email='bornoffire54@gmail.com',
    description='A basic but robust content filter for python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MrDogeBro/content_filter',
    download_url = 'https://github.com/MrDogeBro/content_filter/archive/v1.0.3.tar.gz',
    packages=setuptools.find_packages(),
    package_data = {'content_filter': ['data/filter.json']},
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
    test_suite='nose.collector',
    tests_require=['nose']
)