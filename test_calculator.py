def test_check_HDL_Normal():
    from calculator import check
    assert check('HDL', 70) == 'Normal'

def test_check_HDL_Borderline_Low():
    from calculator import check
    assert check('HDL', 50) == 'Borderline Low'

def test_check_HDL_Low():
    from calculator import check
    assert check('HDL', 30) == 'Low'

