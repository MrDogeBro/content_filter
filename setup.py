import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='content-filter',
    version='1.0.0',
    author='MrDogeBro',
    author_email='bornoffire54@gmail.com',
    description='A basic but robust content filter for python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MrDogeBro/content_filter',
    download_url = 'https://github.com/MrDogeBro/content_filter/archive/v1.0.0.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Natural Language :: English",
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
    test_suite='nose.collector',
    tests_require=['nose']
)