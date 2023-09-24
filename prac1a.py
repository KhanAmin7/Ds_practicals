# code for sorting, binary search, merge, reversing in 1-D array
import numpy as np

arr= [22,11,34,9,56,44]
def sorting(arr):
    arr.sort()
    return arr
print(sorting(arr))

arr1= [11,22,33,44,55,66,77,88]
def binary_search(arr1,el,start,end):
    mid= (start+end)//2
    if el==arr1[mid]:
        return mid
    if el<arr1[mid]:
        return binary_search(arr1, el, start, mid-1)
    else:
        return binary_search(arr1, el, mid+1, end)

print(binary_search(arr1, 88, 0, len(arr1)))

def merge():
    a=[12,13,14,15]
    b=[16,17,18,19]
    merge_list= np.concatenate((a,b))

    return merge_list
merge_array=merge()
print(merge_array)

def rev():
    rev_ls= np.flipud(arr1)
    return rev_ls
rev_array= rev()
print(rev_array)