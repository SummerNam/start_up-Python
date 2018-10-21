x = 'Korea:Korean' #split()
y = 'England:English' #partition()
z = 'France:French' #find() or index()

x1 = x.split(':')
string = 'In {}, people speak {}.'
print(string.format(x1[0],x1[1]))

# print('In {}, people speak {}.'.format(x1[0],x1[1]))

y1 = y.partition(':')
print(string.format(y1[0],y1[2]))

# print('In {}, people speak {}.'.format(y1[0],y1[1]))

z1 = z.index(':')
print(string.format(z[:z1],z[z1+1:]))
