import pytest


def test_sort():
    l0 = list()
    l0.sort()
    assert l0 == []
    l1 = [100, 3, 1, 2, -5, 3, 7, 0]
    l1.sort()
    assert l1 == [-5, 0, 1, 2, 3, 3, 7, 100]
    l2 = [0.0001, 1e-05, 1e05, 1.1e-05]
    l2.sort()
    assert l2 == [1e-05, 1.1e-05, 0.0001, 1e05]
    l3 = ['b', 'C', 'a', '10.1', 'w', '2', 'X', '.']
    l3.sort()
    assert l3 == ['.', '10.1', '2', 'C', 'X', 'a', 'b', 'w']


def test_count():
    l1 = [1, 2, 2, 3, 3, 3]
    assert l1.count(0) == 0
    assert l1.count(1) == 1
    assert l1.count(2) == 2
    assert l1.count(3) == 3
    with pytest.raises(TypeError):
        l1.count()


def test_representation():
    l1 = [0, 1, 2.0, 'three', True, None]
    assert repr(l1) == "[0, 1, 2.0, 'three', True, None]"
    assert str(l1) == "[0, 1, 2.0, 'three', True, None]"
    l0 = list()
    assert repr(l0) == "[]"
    assert str(l0) == "[]"
    l2 = list(l1)
    l2.append(l2)
    l2.append('end')
    assert repr(l2) == "[0, 1, 2.0, 'three', True, None, [...], 'end']"
    assert str(l2) == "[0, 1, 2.0, 'three', True, None, [...], 'end']"


class TestSlice:
    l1 = [0, 1, 2, 3, 4, 5]
    start_stop_input = [(0, 0), (1, 2), (-3, -2),
                        (-500, 500), (500, -500),
                        (None, None), (1, None), (None, 2)
                        ]
    simple_expected = [[], [1], [3],
                       [0, 1, 2, 3, 4, 5], [],
                       [0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [0, 1]
                       ]
    start_stop_step_input = [(None, None, None), (None, None, 2), (1, None, 2),
                             (None, None, -1), (None, None, -2), (3, None, -2),
                             (3, 3, -2), (3, 2, -2), (3, 1, -2), (3, 0, -2),
                             (None, None, -100), (100, -100, None), (-100, 100, None),
                             (100, -100, -1), (-100, 100, -1), (-100, 100, 2)
                             ]
    step_expected = [[0, 1, 2, 3, 4, 5], [0, 2, 4], [1, 3, 5],
                     [5, 4, 3, 2, 1, 0], [5, 3, 1], [3, 1],
                     [], [3], [3], [3, 1],
                     [5], [], [0, 1, 2, 3, 4, 5],
                     [5, 4, 3, 2, 1, 0], [], [0, 2, 4]
                     ]

    @pytest.mark.parametrize('start_stop,expected', list(zip(start_stop_input, simple_expected)))
    def test_slice_simple(self, start_stop, expected):
        start, stop = start_stop
        assert self.l1[start:stop] == expected

    @pytest.mark.parametrize('start_stop_step,expected', list(zip(start_stop_step_input, step_expected)))
    def test_slice_step(self, start_stop_step, expected):
        start, stop, step = start_stop_step
        assert self.l1[start:stop:step] == expected
