from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "./README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypergrowth",
    version="1.7.0",
    author="Alexander Mahabir",
    author_email="alex.mahabir@gmail.com",
    description="Hypergrowth framework to build upon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alex4u2nv/hypergrowth",
    project_urls={
        "Bug Tracker": "https://github.com/alex4u2nv/hypergrowth/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'hypergrowth': 'hypergrowth'},
    include_package_data=True,
    packages=setuptools.find_packages(exclude=("tests",)),
    python_requires=">=3.8",
    install_requires=[
        'click',
        'awslambdaric'
    ]
)
