import random

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


a = []
for base in range(2, 37):
    dec = random.randint(0, 100)
    v = convert_base(dec, to_base=base)
    t = (dec, base, v)
    a.append(t)
print(a)

l = [0, 1, 2, 3, 4, 5]
exp = []
slice_limits_input = [(0, 0), (1, 2), (-3, -2),
                      (-500, 500), (500, -500),
                      (None, None), (1, None), (None, 2)]
for tup in slice_limits_input:
    start, stop = tup
    exp.append(l[start:stop])
print(exp)

slice_limits_input = [(0, 0), (1, 2), (-3, -2),
                      (-500, 500), (500, -500),
                      (None, None), (1, None), (None, 2)
                      ]
slice_expected = [[], [1], [3],
                  [0, 1, 2, 3, 4, 5], [],
                  [0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [0, 1]
                  ]
o = list(zip(slice_limits_input, slice_expected))
print(o)

start_stop_step_input = [(None, None, None), (None, None, 2), (1, None, 2),
                         (None, None, -1), (None, None, -2), (3, None, -2),
                         (3, 3, -2), (3, 2, -2), (3, 1, -2), (3, 0, -2),
                         (None, None, -100), (100, -100, None), (100, 100, None),
                         (100, -100, -1), (-100, 100, -1), (-100, 100, 2)
                         ]
exp_step = []
for tup in start_stop_step_input:
    start, stop, step = tup
    exp_step.append(l[start:stop:step])
print(exp_step)