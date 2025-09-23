print((2.1+2.2)==4.3)
f1 = float("nan")
f2 = float("inf")
f3 = float("-inf")
print(f1, f2, f3)
print(-f2 == f3)
print(f1 == f1, f1 != f1)
print(f2 + 100)
print(f1 + 1000)
print(f2 + f2)
import math
print(math.ulp(1.0))  # 2.220446049250313e-16