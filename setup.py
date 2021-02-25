from setuptools import setup

setup(
    name="twinedew",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Python package deployment tools for internal use at DEW Water Science",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/dew-waterscience/twinedew",
    author="Kent Inverarity",
    author_email="kent.inverarity@sa.gov.au",
    packages=["twinedew"],
    include_package_data=True,
    entry_points={
        "console_scripts": ["twinedew = twinedew.twinedew:twinedew"]
    },
    install_requires=[
    ],
)

