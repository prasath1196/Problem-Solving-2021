
'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return true/false or 1/0

def hasChildren(ref):
    if ref.left != None or ref.right != None:
        return True
    else:
        return False
        
def store_preorder(root,store):
    if root:
        if hasChildren(root):
            store.append(root)
        store_preorder(root.left,store)
        store_preorder(root.right,store)
        
def isChildrenIdentical(ref1,ref2):
    right = False
    left = False
    if ref1.right == None and ref2.right == None:
        right = True
    elif ref1.right == None and ref2.right!= None:
        right = False
    elif ref1.right != None and ref2.right == None:
        right = False
    elif ref1.right.data == ref2.right.data:
        right = True
        
    if ref1.left == None and ref2.left == None:
        left = True
    elif ref1.left == None and ref2.left!= None:
        left = False
    elif ref1.left != None and ref2.left == None:
        left = False
    elif ref1.left.data == ref2.left.data:
        left = True
    if right and left:
        return True
    else:
        return False
        

def isIdentical(root1, root2):
    store1 = []
    store2 = []
    store_preorder(root1,store1)
    store_preorder(root2,store2)
    if len(store1) != len(store2):
        return False
    elif len(store1) == 0:
        if root1 == None and root2 ==  None:
            return True
        elif root1 == None or root2 == None:
            return False
        elif root1.data != root2.data:
            return False
        else:
            return True
    else:
        for i in range(len(store1)):
            if store1[i].data != store2[i].data:
                return False
            elif isChildrenIdentical(store1[i],store2[i]):
                continue
            else:
                return False
    return True



#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3



#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s1=input()
        s2=input()
        head1=buildTree(s1)
        head2=buildTree(s2)
        if isIdentical(head1, head2):
            print("Yes")
        else:
            print("No")
        
        

# } Driver Code Ends
