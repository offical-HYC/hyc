import setuptools
from hyc import version

setuptools.setup(
    name="hyc",
    packages=setuptools.find_packages(),
    version=version,
    license="MIT",
    description="HYC means HELP YOU CALCULATE.It has many functions to help you calculate quickly and easily.",
    author="Zou",
    author_email="873039943@QQ.com",
    download_url="https://github.com/fourlight/hyc",
    keywords=["calculate", "maths"],
    classifiers=[
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Natural Language :: Chinese (Simplified)"
    ],
)
