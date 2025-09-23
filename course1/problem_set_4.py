from fractions import Fraction

a = Fraction(3, 4)      # 四分之三
b = Fraction('0.25')    # 字符串避免浮点误差
c = Fraction(2.1)       # ⚠️ 先转浮点，浮点误差
d = Fraction(2.1).limit_denominator()  # 自动找最简近邻分数

print(a, b, c, d)
print(a.numerator, a.denominator)
print(float(d))