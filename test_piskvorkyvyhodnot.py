from piskvorkyvyhodnot import vyhodnot

def test_vyhodnot():
    assert vyhodnot('xxx----------------') == 'x'
    assert vyhodnot('-----------------ooo') == 'o'
    assert vyhodnot('xoxoxoxoxoxoxoxoxoxo') == '!'
    assert vyhodnot('--------------------') == '-'
