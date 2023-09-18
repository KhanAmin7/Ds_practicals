# selection sort insertion sort and bubble sort

def selection_sort(list1):#amullyas academy
    for i in range(len(list1)):
        min_val = min(list1[i:])
        min_ind = list1.index(min_val, i)
        list1[i], list1[min_ind] = list1[min_ind], list1[i]

def insertion_sort(list1):# https://www.youtube.com/watch?v=R_wDA-PmGE4
    for i in range(1, len(list1)):
        j = i
        while list1[j - 1] > list1[j] and j > 0:
            list1[j - 1], list1[j] = list1[j], list1[j - 1]
            j -= 1

def bubble_sort(list1):#https://www.youtube.com/watch?v=g_xesqdQqvA
    indexing_length = len(list1) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, indexing_length):
            if list1[i] > list1[i + 1]:  # Compare adjacent elements for sorting
                sorted = False
                list1[i], list1[i + 1] = list1[i + 1], list1[i]

list1 = [56, 17, 8, 24, 18, 47, 17]
print(list1)

print("1. Selection Sort")
print("2. Insertion Sort")
print("3. Bubble Sort")

opt = int(input("Enter the option you want to perform the sorting (1/2/3): "))

if opt == 1:
    selection_sort(list1)
    print("Sorted using Selection Sort:", list1)
elif opt == 2:
    insertion_sort(list1)
    print("Sorted using Insertion Sort:", list1)
elif opt == 3:
    bubble_sort(list1)
    print("Sorted using Bubble Sort:", list1)
else:
    print("Invalid option. Please choose 1, 2, or 3.")


 

