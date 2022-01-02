#Heap Sort 
#First create Maxheap of the binary heap 

def heapify(arr,n,f):
    largest=f
    left=(f*2)+1
    right=(f*2)+2
    if left<n and arr[largest]<arr[left]:
        largest=left
    if right<n and arr[largest]<arr[right]:
        largest=right
    if largest!=f:
        arr[largest],arr[f]=arr[f],arr[largest]
        heapify(arr,n,largest)





#driver code
arr=[2,1,3,4,0]
n=len(arr)
for f in range(n//2,-1,-1):
    heapify(arr,n,f)
for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i] # swap
    heapify(arr, i, 0)
print(arr)
