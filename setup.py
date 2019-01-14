import nltk, setuptools

# download required nltk corpus

nltk.download("wordnet")
nltk.download("stopwords")

# tell setuptools about the package

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textpreprocess",
    version="0.0.1",
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