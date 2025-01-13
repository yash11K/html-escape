from setuptools import setup, find_packages

setup(
    name="xml-formatter-plus",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "argparse",
    ],
    author="YashKabra",
    description="A Python package to format and beautify XML strings with HTML entity handling",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YashKabra/decoder-package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "xml-formatter=xml_formatter:main",
        ],
    },
    python_requires=">=3.6",
)
