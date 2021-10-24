class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
class MyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def get(self,index):
        if index <0 or index> self.size:
            return -1
        curr_node=self.head
        for i in range(0,index):
           curr_node=curr_node.next
        return curr_node.value
    def addAtHead(self,value):
        return self.addAtindex(0,value)
        
    def addAtTail(self,value):
        return self.addAtindex(self.size,value)
    def addAtindex(self,index,value):
        if index>self.size:
            return
        curr_node=self.head
        new_node=Node(value)
        if index<=0:
            new_node.next=self.head
            if curr_node is not None:
                curr_node.prev=new_node
            self.head=new_node
        else:
            for f in (index-1):
                curr_node=curr_node.next
            new_node.prev=curr_node
            new_node.next=curr_node.next
            if curr_node.next is not None:
                curr_node.next.prev=new_node
            curr_node.next=new_node
            self.size=self.size+1
        return
    def deleteAtHead(self):
        return self.deleteAtindex(0)
    def deleteAtTail(self):
        return self.deleteAtTail(self.size)
    def deleteAtindex(self,index):
        if index>=self.size or index<0:
            return
        if index==0 or self.size==1:
            temp=self.head.next 
            self.head.next=None
            if temp is not None:
                temp.prev=None
        else:
            curr_node=self.head
            for f in range(0,index-1):
                curr_node=curr_node.next
            if curr_node.next.next is not None:
                curr_node.next=curr_node.next.next
                curr_node.next.prev=curr_node
            else:
                curr_node.next=None
        return 


            

        



