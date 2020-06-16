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
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Natural Language :: English",
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)