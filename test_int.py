# TODO: переписать параметризацию так, чтобы в отчете pytest было видно, какие именно значения передаются

import pytest
from random import randint


class TestInt:
    bases = [0]
    bases.extend(range(2, 37))

    @pytest.mark.parametrize('base', bases)
    def test_base_limit_positive(self, base):
        """Проверяет, что системы счисления с целым осноывнием с 2 по 36 и 0 допустимы"""
        assert int('1', base=base) == 1

    invalid_bases = [-1, 1, 37, -(2**234), 2**234,
                     3.3, -3.3, 'h', True, None, [2], (2,), {2}
                     ]

    @pytest.mark.parametrize('base', invalid_bases)
    def test_base_limit_negative(self, base):
        """
        Проверяет, что при использовании недопустимых значений основания системы счисления
        возникают соответствующие исключения
        """
        if isinstance(base, int):
            with pytest.raises(ValueError):
                assert int('0', base=base)
        else:
            with pytest.raises(TypeError):
                assert int('0', base=base)

    decimal_base_val = [(34, 2, '100010'), (43, 3, '1121'), (96, 4, '1200'), (13, 5, '23'),
                        (42, 6, '110'), (19, 7, '25'), (57, 8, '71'), (88, 9, '107'),
                        (73, 10, '73'), (6, 11, '6'), (11, 12, 'B'), (0, 13, '0'),
                        (92, 14, '68'), (2, 15, '2'), (51, 16, '33'), (20, 17, '13'),
                        (48, 18, '2C'), (9, 19, '9'), (55, 20, '2F'), (62, 21, '2K'),
                        (90, 22, '42'), (60, 23, '2E'), (22, 24, 'M'), (11, 25, 'B'),
                        (5, 26, '5'), (59, 27, '25'), (88, 28, '34'), (2, 29, '2'),
                        (24, 30, 'O'), (72, 31, '2A'), (87, 32, '2N'), (64, 33, '1V'),
                        (40, 34, '16'), (96, 35, '2Q'), (63, 36, '1R')
                        ]

    @pytest.mark.parametrize('dec_base_val', decimal_base_val)
    def test_convert_from_string(self, dec_base_val):
        """
        Проверяет перевод из строки в целое число в десятичной системе счисления
        в зависимости от исходной системы счисления
        """
        decimal, base, val = dec_base_val
        assert int(val, base=base) == decimal

    val_decimal = [(500, 500), ('5', 5), (5.11, 5), (5.9, 5), (-5, -5),
                   ('-5', -5), (' -5 ', -5), ('\n-5\t', -5), (-5.11, -5), (-5.9, -5),
                   (1.1e5, 110000), (1.1e-05, 0)
                   ]

    @pytest.mark.parametrize('val_dec', val_decimal)
    def test_convert(self, val_dec):
        """
        Проверяет перевод в целое число в десятичной системе в зависимости от способа задания исходного значения
        без указания основания исходой системы
        """
        val, decimal = val_dec
        assert int(val) == decimal

    division_methods = [int.__truediv__,
                        int.__floordiv__,
                        int.__divmod__,
                        int.__mod__
                        ]

    @pytest.mark.parametrize('division', division_methods)
    def test_zero_division2(self, division):
        """Проверяет возникновение исключения при делении на 0"""
        num = randint(1, 1000)
        with pytest.raises(ZeroDivisionError):
            assert division(num, 0)
