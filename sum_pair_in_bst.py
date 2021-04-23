'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    # root : the root Node of the given BST
    # target : the target sum
    def isPairPresent(self,root, target): 
        if self.findPair(root,target,set()) == True:
            return 1
        else:
            return 0
    
    
    def findPair(self,root,target,un_set):
        if root == None:
            return False
        if self.findPair(root.left,target,un_set):
            return True
        if un_set and (target - root.data) in un_set: 
            return True
        else:
            un_set.add(root.data)
        return self.findPair(root.right,target,un_set)