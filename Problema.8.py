n=int(input('Introduceti numarul de siruri:'))
S=[str(input('Introduceti literele sirului: ')) for i in range(n)]
S1=''
print('Sirurile sunt:')
for i in S:
    for j in range(len(i)):
        if ord(i[j])==90:
            S1+='A'
        elif ord(i[j])==32:
            S1+='-'
        else:
            S1+=chr(ord(i[j])+1)
    print(S1) 
    S1=''
