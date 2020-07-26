# UK Postcodes Validator     

Package uk_postcodes contains module "validator" for validating the format
of UK postcodes.

The project was created as a simple technical exercise
and to try GitHub and packaging of Python project.

## Install

You can use the module validator.py in your code.

I created Python package on test.pypi.org for study purposes but you can use it.

https://test.pypi.org/project/uk-postcodes-pkg-frantisekmelan/


## Technologies

Python

## Usage:


```python
from uk_postcodes import validator

validator.is_valid("SW1W 0NY")
```

## Docstring

```python
def is_valid(postal_code):
    """
    Checks the correct format of UK postcode. Special cases are allowed.
    :param postal_code: the checked postcode
    :return: True if the format is valid, False otherwise
    """
```