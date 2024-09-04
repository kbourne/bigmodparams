from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bigmodparams",
    version="0.0.1",
    author="Keith Bourne",
    author_email="keith@gradientvalley.com",
    description="A package for optimizing parameters for the training and fine-tuning of large generative AI models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kbourne/bigmodparams",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        # List your package dependencies here
    ],
)