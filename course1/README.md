## 格式化输出

| 表达式         | 含义            | 示例输出         |
| ----------- | ------------- | ------------ |
| `{:.2f}`    | 保留两位小数，四舍五入   | `'3.14'`     |
| `{:.0f}`    | 不保留小数，四舍五入    | `'3'`        |
| `{:8.2f}`   | 总宽度8，右对齐，2位小数 | `'    3.14'` |
| `{:<8.2f}`  | 左对齐           | `'3.14    '` |
| `{:>08.2f}` | 补零对齐          | `'00003.14'` |

## 浮点

- 浮点误差
```
print((2.1+2.2)==4.3) # False
```
- nan
```
f1 = float('nan')
print(f1 == f1, f1 != f1) # False True
print(f1 + 1000) # nan
```

- inf
```
f2 = float('inf')
print(f2 + 1000) # inf
print(f2 - f2) # nan
print(f2 + f2) # inf
```

- eps
```
import math
print(math.ulp(1.0))  # 2.220446049250313e-16
```

## 复数

- 定义和基本方法

```python
a = 3 + 4j
b = complex(5, 12)
print(a.real, b.imga, (a + b).conjugate)
```

- 模长

```python
a = 3 + 4j
print(abs(a))
```

- 复杂运算

```python
from cmath import sin, cos, exp # 注意是 cmath
print(sin(a), cos(a), exp(b))
```

## 分数


- 分数定义
  
```python
from fractions import Fraction

a = Fraction(3, 4)      # 四分之三
b = Fraction('0.25')    # 字符串避免浮点误差
c = Fraction(2.1)       # ⚠️ 先转浮点，浮点误差
d = Fraction(2.1).limit_denominator()  # 自动找最简近邻分数

print(a, b, c, d)
# 3/4  1/4  4728779608739021/2251799813685248  21/10
```

- 分子分母

```python
print(a.numerator, a.denominator)
```

- 转实数

```python
print(float(a))
```