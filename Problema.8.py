n=int(input('Introduceti numarul de siruri:'))
S=[str(input('Introduceti literele sirului: ')) for i in range(n)]
print('Sirurile sunt:')
for i in S:
    S1=''
    for j in range(len(i)):
        if i[j]=='Z':
            S1+='A'
        elif i[j]==' ':
            S1+='-'
        else:
            S1+=chr(ord(i[j])+1)
    print(S1)
