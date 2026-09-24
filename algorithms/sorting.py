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

def Selection_Sort(arr):
    arr = arr.copy()
    n = len(arr)
    x = 0
    for i in range(n-1):
        for j in range(i+1,n):
            yield {"array" : arr.copy(), "comparing" : (i,j)}
            if arr[i] > arr[j]:
                x = arr[i]
                arr[i] = arr[j]
                arr[j] = x
                yield{"array" : arr.copy(), "comparing" : (i, j)}
    yield {"array" : arr.copy(), "comparing" : None}
def Insertion_Sort(arr):
    arr = arr.copy()
    n = len(arr)
    x = 0
    for i in range(n):
        pos = int(i)
        while pos > 0 and arr[pos-1] > arr[pos]:
            yield {"array" : arr.copy(), "comparing" : (pos,pos-1)}
            x = arr[pos]
            arr[pos] = arr[pos-1]
            arr[pos-1] = x
            pos -= 1
            yield {"array" : arr.copy(), "comparing" : (pos,pos-1)}
    yield {"array" : arr.copy(), "comparing" : None} 