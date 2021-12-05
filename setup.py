import setuptools

import content_filter

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=content_filter.__name__,
    version=content_filter.__version__,
    author=content_filter.__author__,
    description=content_filter.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrDogeBro/content_filter",
    download_url=f"https://github.com/MrDogeBro/content_filter/archive/v{content_filter.__version__}.tar.gz",
    packages=setuptools.find_packages(),
    package_data={"content_filter": ["data/filter.json", "data/replacements.json"]},
    license=content_filter.__license__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    test_suite="nose.collector",
    tests_require=["nose"],
)
