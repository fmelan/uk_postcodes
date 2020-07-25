from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='uk-postcodes-pkg-frantisekmelan',
    version='0.0.3',
    packages=['uk_postcodes'],
    url='https://github.com/fmelan/uk_postcodes',
    license='MIT License',
    author='František Melán',
    author_email='fmelan@gmail.com',
    description='Validator of UK postcodes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=2.7'
)
