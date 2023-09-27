def quicksort(array):
    if len(array) < 2:
        return array
    else:
        a = array[0]

        b = [i for i in array[1:] if i < a]

        c = [i for i in array[1:] if i > a]

        return quicksort(b) + [a] + quicksort(c)
    

print(quicksort([5, 1, 24, 2, 3, 6, 7, 3, 0]))
