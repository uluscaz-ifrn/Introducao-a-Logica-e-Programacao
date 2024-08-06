x = float(input("Digite um valor para X: "))
fx = 0
if x <= 1:
    fx = 1
elif x > 1 and x <= 2:
    fx = 2
elif x > 2 and x <= 3:
    fx = x * x
elif x > 3:
    fx = x * x * x
print("O valor de f(x) é %2.f" % fx)
