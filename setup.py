__author__ = ["Francisco Clavero"]
__description__ = "Build setup for the package."
__email__ = ["fcoclavero32@gmail.com"]
__status__ = "Prototype"

import nltk, setuptools

# Download required nltk corpus.

nltk.download("wordnet")
nltk.download("stopwords")

# Tell `setuptools` about the package.

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textpreprocess",
    version="0.1.0",
    author="Francisco Clavero",
    author_email="fcoclavero32@gmail.com",
    description="Python package for natural language pre-processing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fcoclavero/textpreprocess",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
