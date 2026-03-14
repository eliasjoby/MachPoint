from setuptools import setup, find_packages

setup(
    name="machpoint",
    version="0.1.0",
    description="A blazing-fast Python web framework with Go-powered core.",
    author="Elias Joby",
    author_email="eliasjoby1618@gmail.com",
    packages=find_packages(include=["machpoint", "machpoint.*"]),
    include_package_data=True,
    package_data={
        "machpoint": ["*.so", "*.h", "*.mod", "*.sum"],
    },
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)