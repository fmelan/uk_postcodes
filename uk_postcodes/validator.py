import re

UK_POST_CODE_REGEX = "^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

def is_valid(postal_code):
    """
    Checks the correct format of UK postcode. Special cases are allowed.
    :param postal_code: the checked postcode
    :return: True if the format is valid, False otherwise
    """
    return bool(re.match(UK_POST_CODE_REGEX, postal_code)) if postal_code else False
