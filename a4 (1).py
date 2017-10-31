"""
Team - Agnel Aaron and Anjanay Kirti Gour
Roll no. - 2017010 and 217021 respectively
Section - B5 and A6 respectively
"""


def make_int(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(A[i][j])
    return A
def matrixrank(A):
    for c in A:
        for a in c:
            assert isinstance(a,int),"Preconditions not satisfied"
    rank = min(len(A),len(A[0]))
    row=0
    last_col = len(A[0])-1
    while row<=rank-1:
        if A[row][row]!=0:
           for i in range(0,len(A)):
                if i!=row:
                    cur = A[i][row]
                    cur*=-1
                    #A=make_int(A)
                    Row_transformation(A,cur/A[row][row],row,i)
                    #A = make_int(A)
        else:
            if row == len(A)-1:
                rank=rank-1
                row=row-1
            else:
                cond = True
                for i in range(row+1,len(A)):
                    if A[i][row]!=0:
                        cond=False
                        break
                if not cond:
                    swaprows(A,i,row)
                else:
                    columnswap(A,row,last_col)
                    last_col-=1
                    rank=rank-1
                row=row-1
        row+=1
    count_1=0
    cust_row=0
    while cust_row <= min(len(A),len(A[0]))-1:
        if A[cust_row][cust_row]!=0:
            count_1+=1
        cust_row+=1
    rank=count_1
    return rank


def columnswap(A,col1,col2):
    for i in range(len(A)):
        A[i][col1],A[i][col2] = A[i][col2],A[i][col1]
    return A

def swaprows(A,row1,row2):
    A[row1],A[row2]=A[row2],A[row1]
    return A

def Row_transformation(A,x,row1,row2):
    assert isinstance(x,float),"Preconditions not satisfied"
    for c in A:
        for a in c:
            assert isinstance(a,int),"Preconditions not satisfied"
    assert (row1<len(A))and(row2<len(A)),"Preconditions not satisfied"
    for i in range(len(A[row1])):
        A[row2][i] = A[row2][i] + x*A[row1][i]
    A=make_int(A)
    return A




#A=[[1,0,0],[0,1,0],[0,0,1]]
#A=[[0,0,0],[0,4,0],[0,0,0]]
#A=[[10,20,10],[-20,-30,10],[30,50,0]]
#A=[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
#A=[[1,2,3],[2,3,5],[3,4,7],[4,5,9]]
#A = [[10,20,30,40],[50,56,0,-1],[34,45,56,76]]
A = [[0,1,0],[0,0,0]]
#A=[[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]]
#A=[[1],[1],[1],[1],[1],[1],[1]]
print(matrixrank(A))
