import pytest


class TestSetOperations:
    s0 = set()
    abcd = set('abcd')
    cdef = set('cdef')

    def test_union(self):
        assert self.abcd.union(self.cdef) == set('abcdef')
        assert self.cdef.union(self.abcd) == set('abcdef')
        assert self.abcd.union(self.s0) == self.abcd
        assert self.s0.union(self.cdef) == self.cdef

    def test_intersection(self):
        assert self.abcd.intersection(self.cdef) == set('cd')
        assert self.cdef.intersection(self.abcd) == set('cd')
        assert self.abcd.intersection(self.s0) == set()
        assert self.s0.intersection(self.cdef) == set()

    def test_difference(self):
        assert self.abcd.difference(self.cdef) == set('ab')
        assert self.cdef.difference(self.abcd) == set('ef')
        assert self.abcd.difference(self.s0) == self.abcd
        assert self.s0.difference(self.cdef) == set()

    def test_symmetric_difference(self):
        assert self.abcd.symmetric_difference(self.cdef) == set('abef')
        assert self.cdef.symmetric_difference(self.abcd) == set('abef')
        assert self.abcd.symmetric_difference(self.s0) == self.abcd
        assert self.s0.symmetric_difference(self.cdef) == self.cdef


s0 = set()
s1 = set('abcde')
s2 = {0, 1, 2, 3, 4}
sets = [s0, s1, s2]


@pytest.mark.parametrize('s', sets)
def test_pop(s):
    for _ in range(len(s)):
        i = s.pop()
        assert i not in s
    with pytest.raises(KeyError):
        s.pop()
