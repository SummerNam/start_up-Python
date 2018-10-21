a='happy' ; b='pig'; c='python'


x = a[1:] + a[0] +'ay'
y = b[1:] + b[0] +'ay'
z = c[1:] + c[0] +'ay'


string = '{} -> {}'

print(string.format(a,x))
print(string.format(b,y))
print(string.format(c,z))
