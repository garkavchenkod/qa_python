import pytest


class TestStringCases:
    string_var = ['abc1de', 'Abc1de', 'aBc1De', 'ABC1DE']
    string_up = 'ABC1DE'
    string_low = 'abc1de'

    @pytest.mark.parametrize('upper_case', [string_up])
    @pytest.mark.parametrize('input_string', string_var)
    def test_upper(self, input_string, upper_case):
        assert input_string.upper() == upper_case

    @pytest.mark.parametrize('lower_case', [string_low])
    @pytest.mark.parametrize('input_string', string_var)
    def test_lower(self, input_string, lower_case):
        assert input_string.lower() == lower_case


def test_index():
    string = "abcd1 ad1"
    assert string.index('a') == 0
    assert string.index('a', 4) == 6
    assert string.index('a', 4, -1) == 6
    with pytest.raises(ValueError):
        string.index('a', 3, 5)
    assert string.index('1') == 4
    with pytest.raises(TypeError):
        string.index(1)
    assert string.index('d1') == 3
    assert string.index('d1', 4) == 7


def test_find():
    string = "abcd1 ad1"
    assert string.find('a') == 0
    assert string.find('a', 4) == 6
    assert string.find('a', 4, -1) == 6
    assert string.find('a', 3, 5) == -1
    assert string.find('1') == 4
    with pytest.raises(TypeError):
        string.find(1)
    assert string.find('d1') == 3
    assert string.find('d1', 4) == 7


def test_len():
    strings_0 = [str(), '', ""]
    for _ in strings_0:
        assert len(_) == 0
    abc = 'abc'
    ef = 'ef'
    assert len(abc) == 3
    assert len(ef) == 2
    assert len(abc + ef) == 5
    assert len(abc * 3) == 9
    assert len(ef * 1000) == 2000
    assert len(ef * 0) == 0
