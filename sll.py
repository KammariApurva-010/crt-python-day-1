class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
def createSLL(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            temp.next=Node(val)
            temp=temp.next
    return head
arr=list(map(int,input().split()))
print(createSLL(arr))