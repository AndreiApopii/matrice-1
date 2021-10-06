A=[[1, 3, 6, 7, 4],[1, 3, 2, 5, 7],[10, 11, 7, 4, 12],[18, 5, 3, 11, 13],[20, 7, 8, 11, 19]]
suma_liniilor=[]
suma_coloanelor=[]
diagonala_principala=[]
diagonala_secundara=[]
for i in range(len(A)):
    print(A[i])
    suma_liniilor.append(sum(A[i]))
    for j in range(len(A[0])):
        suma_coloanelor[i]+=A[j][i]
        if i==j:
            diagonala_principala.append(A[i][j])
for i in range(len(A)):
   for j in range(len(A[0])):
        if(i+j)==(len(A)-1):
            diagonala_secundara.append(A[i][j])


for i in range(len(A)):
    print(f"Suma pe linia {i} este {suma_liniilor[i]} ")
for i in range(len(A)):
     print(f"Suma pe coloana {i} este {suma_coloanelor[i]}")
print(f"Elementele diagonalei principale sunt: {diagonala_principala}")
print(f"Elementele diagonalei secundare sunt: {diagonala_secundara}")
