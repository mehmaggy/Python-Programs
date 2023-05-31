from numpy import*
a= array([[10,20,30],[40,50,60]])
for el in a: 
    print('1.',el)
for el in a[0]: 
    print('2.',el)  
for el in a[1]: 
    print('3.',el)
for el in a[[1],[1]]:
    print('4.',el)
