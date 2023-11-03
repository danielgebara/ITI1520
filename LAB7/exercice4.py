# ITI1520
# Daniel Gebara
# 300401006
# Exercise 4


def bougeZerosv1(lst):
 i = 0 
 n = len(lst)
 tmp = []
 while i < n: 
    if lst[i] == 0: 
        tmp.append(lst.pop(i)) 
        n -= 1 
    else: 
        i += 1 
 zeros = [0] * (len(lst) - len(tmp)) 
 return lst + zeros


def bougeZerosv2(lst): 
 count_zeros = lst.count(0)
 while count_zeros > 0: 
    if 0 in lst: 
        lst.remove(0)
        lst.append(0)
        count_zeros -= 1


def bougeZeros_v3(lst):
    zero_idx = 0 
    n = len(lst)
    while zero_idx < n: 
        i = zero_idx 
        while i < n: 
            if lst[i] == 0:
                lst[i], lst[zero_idx] = lst[zero_idx], lst[i]
            i += 1 
        zero_idx += 1