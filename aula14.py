a = 'AAAAAAAA'
b = 'BBBBBBBBBB'
c = 1.1

string = 'b ={1} a={0} a={0} a={0} c= {nome3:.2f}'
formato = string.format(a, b, c, nome3=c)

print(formato)
