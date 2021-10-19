S='A B a Z Z Y c'
S1=''
for i in range(len(S)):
    if ord(S[i])==90:
        S1+='A'
    elif ord(S[i])==32:
        S1+=' '
    else:
        S1+=chr(ord(S[i])+1)
print('Sirul modificat este', S1)
