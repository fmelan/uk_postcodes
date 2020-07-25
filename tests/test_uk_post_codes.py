from uk_postcodes.validator import is_valid


def test_validate():

    assert not is_valid(None)
    assert not is_valid("")

    # common
    assert is_valid("EC1A 1BB")
    assert is_valid("W1A 0AX")
    assert is_valid("M1 1AE")
    assert is_valid("B33 8TH")
    assert is_valid("B338TH")
    assert is_valid("CR2 6XH")
    assert is_valid("DN55 1PT")

    # special
    assert is_valid("AI-2640")
    assert is_valid("GX11 1AA")
    assert is_valid("KY2-2301")
    assert is_valid("CV4 8UW")
    assert is_valid("E20 2ST")
    assert is_valid("EC2N 2DB")
    assert is_valid("CO4 3SQ")
    assert is_valid("BFPO 57")
    assert is_valid("MSR-2135")

    # czech
    assert not is_valid("182 00")