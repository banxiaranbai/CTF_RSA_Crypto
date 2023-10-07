import gmpy2
import libnum
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt

#N,c需要是十进制
N1 =
N2 =
N3 =
c1 =
c2 =
c3 =

# e = 3
e =
n = [N1, N2, N3]
c = [c1, c2, c3]
resultant, mod = crt(n, c)
value, is_perfect = gmpy2.iroot(resultant, e)
print(long_to_bytes(value))