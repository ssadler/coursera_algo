import sys
from math import log

funcs = {
    'a': lambda n: 2 ** (2 ** n),
    'b': lambda n: 2 ** (n ** 2),
    'c': lambda n: n ** 2 * log(n),
    'd': lambda n: n,
    'e': lambda n: n ** (2 ** n),
}

print '\n'.join("%s\t%s" % (a, b) for b, a in sorted((funcs[l](int(sys.argv[2])), l) for l in 'abcde'))
