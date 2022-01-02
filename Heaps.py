class minheap:
    def __init__(self,maxSize):
        self.heapSize=maxSize
        self.minHeap=[0]*(maxSize+1)
        self.realsize=0
    def add(self,element):
        self.realsize=self.realsize+1
        if self.realsize>self.heapSize:
            print("HeapStack is full")
            self.realsize-=1
            return
        self.minHeap[self.realsize]=element
        index=self.realsize
        parent=index//2
        while self.minHeap[parent]>self.minHeap[index] and index>1:
            self.minHeap[parent],self.minHeap[index]=self.minHeap[index],self.minHeap[parent]
            index=parent
            parent=index//2
        return 
    def pop(self):
        if self.realsize<1:
            print("No elements exist")
            return
        removeElement=self.minHeap[1]
        index=1
        self.minHeap[1]=self.minHeap[self.realsize]
        self.realsize-=1
        while index<self.realsize and index<=self.realsize//2:
            left=index*2
            right=(index*2)+1
            if self.minHeap[left]<self.minHeap[index] or self.minHeap[right]<self.minHeap[index]:
                if self.minHeap[left]<self.minHeap[right]:
                    self.minHeap[index],self.minHeap[left]=self.minHeap[left],self.minHeap[index]
                    index=left
                else:
                    self.minHeap[index],self.minHeap[right]=self.minHeap[right]=self.minHeap[index]
                    index=right
            else:
                break
        return removeElement

s=minheap(5)
s.add(5)
s.add(4)
s.add(3)
s.add(2)
s.add(1)
print(s.minHeap)

