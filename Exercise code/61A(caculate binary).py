'''bin1=input()
bin2=input()
result = bin(int(bin1, 2) + int(bin2, 2))[2:]
print(result)'''
bin1=input()
bin2=input()
for i in range(len(bin1)):
    if bin1[i]=='1' and bin2[i]=='1':
        bin1=bin1[:i] + '0' + bin1[i+1:]
    elif bin1[i]=='0' and bin2[i]=='0':
        bin1=bin1[:i] + '0' + bin1[i+1:]
    else:
        bin1=bin1[:i] + '1' + bin1[i+1:]
print(bin1)