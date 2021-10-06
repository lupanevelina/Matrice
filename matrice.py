x=[[1,2,3,4,5],
  [3,5,9,3,10],
  [7,2,9,6,11],
  [8,12,9,3,10],
  [1,4,8,2,15]]

  
#suma elem de pe fiecare linie
for i in range(len(x)):
    print("Suma elem de pe fiecare linie:",sum(x[i]))
#suma elem de pe fiecare coloana
for j in range(len(x[0])):
    coloana=[]
    for rind in x:
        coloana.append(rind[j])
    print("Suma elem de pe fiecare coloana:",sum(coloana))
#diagonala principala
diag_princ=[]
for i in range(len(x)):
    for j in range(len(x[0])) :
        if i==j :
            diag_princ.append(x[i][j])
print("Diagonala principala=",diag_princ)
#diagonala secundara  
diag_sec=[] 
for i in range(len(x)):
    for j in range(len(x[0])) :
        n=5
        if i+j==n-1:
            diag_sec.append(x[i][j])
            
print("Diagonala secundara=",diag_sec) 

    

    

    
 