dict={'ankit':5000,'Mahesh':6000,'Rajesh':7000}
for keys, value in dict.items():
   print("1.",keys)
for i in dict:
    print('2.',dict['Mahesh'])
    print('3.',dict.values())
    dict['Rajesh']=9000
    print('4.',dict['Rajesh'])
