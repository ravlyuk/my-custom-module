from setuptools import find_packages, setup


def read_requirements_txt():
    with open('requirements.txt') as fp:
        requirements = [line.strip() for line in fp]
        return requirements

setup(
    name="mycalc",
    version="0.0.1",
    description="A small example package with some arithmetics",
    packages=find_packages(),
    include_package_data=True,
    author="Evgeny Ravlyuk",
    author_email="kobtok1@example.com",
    python_requirements='>=3',
    install_requires=read_requirements_txt(),
    # install_requires=[
    #     'pandas==0.24.2',
    #     'numpy==1.16.3',
    # ],
    url="https://github.com/ravlyuk/my-custom-module",
)
