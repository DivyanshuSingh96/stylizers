import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    name="stylizer",
    version="v0.0.1",
    author="Divyanshu Singh",
    author_email="divyanshu.singh144400@gmail.com",
    license="MIT",
    description='A Beautiful Library which will modify your Beautiful Name into an Extraordinary Styled Name.',
    long_description=README,
    url='https://github.com/DivyanshuSingh96/stylizer',
    packages=setuptools.find_packages(),
    python_requires=">=3.0",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)
