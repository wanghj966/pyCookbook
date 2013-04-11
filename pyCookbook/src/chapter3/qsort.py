def qsort(L):
    if len(L)<=1:return L
    return qsort([lt for lt in L[1:] if lt<L[0]])+L[0:1] +qsort([gt for gt in L[1:] if gt>L[0]])
