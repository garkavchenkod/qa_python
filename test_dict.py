import pytest


class TestDict:
    d0 = dict()
    d1 = {'a': 1, 'b': 2}
    d2 = {1: 'a', 2: 'b', 3: 'c'}
    d3 = d0.fromkeys(range(100), 0)
    dicts = [d0, d1, d2, d3]
    lens = [0, 2, 3, 100]

    def test_keys(self):
        assert set(self.d0.keys()) == set()
        keys = self.d1.keys()
        assert 'a' in keys
        assert 'b' in keys
        assert 'a' in self.d1
        assert 'b' in self.d1
        assert set(keys) == {'a', 'b'}
        assert repr(keys) == "dict_keys(['a', 'b'])"

    def test_values(self):
        assert set(self.d0.values()) == set()
        values = self.d1.values()
        assert 1 in values
        assert 2 in values
        assert set(values) == {1, 2}
        assert repr(values) == "dict_values([1, 2])"

    def test_items(self):
        assert set(self.d0.items()) == set()
        items = self.d1.items()
        assert ('a', 1) in items
        assert ('b', 2) in items
        assert set(items) == {('a', 1), ('b', 2)}
        assert repr(items) == "dict_items([('a', 1), ('b', 2)])"

    @pytest.mark.parametrize('d', dicts)
    def test_clear(self, d):
        d_copy = d.copy()
        d_copy.clear()
        assert d_copy == dict()

    @pytest.mark.parametrize('d, length', list(zip(dicts, lens)))
    def test_len(self, d, length):
        assert len(d) == length
