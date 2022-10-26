from setuptools import setup, find_packages

setup(
    name="slim",
    version=0.01,
    description="Constrained linear map parametrizations in pytorch",
    url="https://pnnl.github.io/Deep-Learning-Control-with-Embedded-Physical-Structure/",
    author="Aaron Tuor, Jan Drgona, Elliott Skomski",
    author_email="aaron.tuor@pnnl.gov",
    license="MIT",
    packages=find_packages(),  # or list of package paths from this directory
    zip_safe=False,
    classifiers=["Programming Language :: Python"],
    keywords=["Deep Learning", "Pytorch", "Linear Models"])