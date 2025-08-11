class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createDLL(arr):
    head=None
    for val in arr:
        if (head==None):
            head=Node(val)
            temp=head
        else:
            
            temp.next=Node(val)
            temp.prev=head
            temp=temp.next
    return head
arr=list(map(int,input().split()))
print(createDLL(arr))