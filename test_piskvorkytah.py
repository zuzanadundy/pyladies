from piskvorkytah import tah

def test_tah():
    assert tah('--------------------', 1, 'x') == '-x------------------'
    assert tah('--------------------', 5, 'o') == '-----o--------------'