import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="search-github",
    version="1.0.0",
    author="Jonas",
    author_email="jonas.eukan@gmail.com",
    description="A CLI tool for searching repositories in Github",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Saliovin/search-github",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['search-github=search_github.search_github:main'],
    },
    python_requires='>=3.7',
)