#get random array

def Bubble_Sort(arr):
    ok = True
    arr = arr.copy()
    n = len(arr)
    x = 0
    while ok:
        ok = False
        for i in range(n-1):
            yield {"array" : arr.copy(), "comparing" : (i,i+1)}
            if arr[i] > arr[i+1]:
                x = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = x
                ok = True
                yield{"array" : arr.copy(), "comparing" : (i, i+1)}
    yield{"array" : arr.copy(), "comparing" : None}