from setuptools import setup, find_packages

setup(
    name="ml_logger",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["rich"],
    author="Ruslan Mamedov",
    description="Reusable logger for ML projects with rich console and file output",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
