S=str(input('Introduceti literele sirului: '))
print('a)numărul de apariţii ale caracterului ’A’ în şirul S:', S.count('A'))
print('b)şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’:', S.replace('A','*'))
print('c)şirul obţinut prin radierea din şirul S a tuturor apariţiilor caracterului ’B’:', S.replace('B',''))
print('d)numărul de apariţii ale silabei MA în şirul S:', S.count('MA'))
print('e)şirul obţinut prin substituirea tuturor apariţiilor în şirul S a silabei MA prin silaba TA:', S.replace('MA','TA'))
print('f)şirul obţinut prin radierea din şirul S a tuturor apariţiilor silabei TO:', S.replace('TO',''))
print('g)scrierea inversă a şirului S:', S[::-1])
if S==S[::-1]:
    print('h)true')
else:
    print('h)false')
print('i)şirul obţinut prin transformarea tuturor literelor mici din componenţa şirului S în litere mari:', S.upper())
S1 = ''
for i in range(len(S)):
    if (i==0) or (S[i-1]==' ') :
        S1=S1 + S[i].upper()
    else:
        S1=S1 + S[i]
print('j)şirul obţinut prin transformarea primei litere a fiecăruia dintre cuvintele din componenţa şirului S în literă mare:', S1)
print('k)şirul obţinut prin sortarea în ordine alfabetică a caracterelor din şirul S:', ''.join(sorted(S, key=lambda x:x.lower()))) #ordinea alfabetica cu spatiile
print('k)şirul obţinut prin sortarea în ordine alfabetică a caracterelor din şirul S:', ''.join(filter(lambda x:x.isalpha(), sorted(S, key=lambda x:x.lower())))) #ordinea alfabetica fara spatii
