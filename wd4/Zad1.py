A = [1-x for x in [1,2,3,4,5,6,7,8,9,10]]
B = [4**x for x in range(8)]
C = [x for x in B if x%2==0]
print(A)
print(B)
print(C)