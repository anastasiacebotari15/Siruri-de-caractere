s=str(input('Sirul de caractere: '))
print(s)
k=0
for i in s:
    if i=='A':
        k+=1
print('a) Numarul de aparitii a caracterului A in sirul s este',k,'ori' )
b=s.replace('A','*')
print('b) Sirul obtinut prin substituirea caracterului A prin caracterul * este:', b)
c=''
c=s.replace('B','')
print('c) Sirul obtinut prin radierea caracterului B din sirul s este:',c)
d=s.count('MA')
print('d) Numarul de aparitii a silabei MA in sirul s este:',d)
e=''
e=s.replace('MA','TA')
print('e) Sirul obtinut prin substituirea tuturol aparitiilor silabei MA prin silaba TA este:',e)
f=''
f=s.replace('TO','')
print('f) Sirul obtinut prin radierea silabei TO din sirul s este:',f)
g='' 
x=len(s)
g=s[x::-1]  
print('g) Scrierea inversa a sirului s:',g)