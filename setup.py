import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open ("VERSION","r") as f:
    build_version = f.read()

setuptools.setup(
    name="barebone_package", # Replace with your own username
    version=build_version,
    author="henry",
    author_email="hto1999@gmail.com",
    description="template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts":[
            "hello=app1.main:say_hello",
            "goodbye=app2.main:say_good_bye",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)