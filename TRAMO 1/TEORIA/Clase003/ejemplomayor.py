
a = 10
b = 20

if a > b:
    print("Mayor: ",a)
else:
    if b > a:
        print("Mayor: ",b)
    else:
        print("Son iguales")


mayor = max(a,b)

print("Mayor python:",mayor)

mayor = a
if b > mayor:
    mayor = b

print("Mayor:",mayor)






