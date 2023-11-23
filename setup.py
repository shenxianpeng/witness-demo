import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="witness-demo",
    version="1.0.0",
    description="witness demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Peter Shen",
    author_email="xianpeng.shen@gmail.com",
    keywords=["test"],
    python_requires=">=3",
    license="MIT",
    project_urls={
        "Source": "https://github.com/shenxianpeng/witness-demo",
        "Tracker": "https://github.com/shenxianpeng/witness-demo/issues"
    },
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Topic :: Education :: Testing",
        "Programming Language :: Python :: 3",
    ],
)