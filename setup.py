"""
Setup configuration for MLP - Monitoring Linux Processes
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlp",
    version="1.0.0",
    author="Amirsam Azmoodeh",
    author_email="amirsamazmoodeh@gmail.com",
    description="A lightweight, real-time process monitoring tool for Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mlp",
    py_modules=["mlp", "get_data", "calculate"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "mlp=mlp:main",
        ],
    },
)