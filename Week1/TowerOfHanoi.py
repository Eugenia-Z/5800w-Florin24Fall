def Hanoi(n, i, j):
    k = ({1,2,3} - {i,j}).pop()
    # base case
    if n == 0:
        return
    Hanoi(n-1, i , k)
    print("Move a disk from peg" ,i, " to peg ", j)
    Hanoi(n-1, k, j)

Hanoi(3, 1,2)