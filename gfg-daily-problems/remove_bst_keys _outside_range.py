 def removekeys(self, root, Min, Max):
        if root == None:
            return None
     
 
        root.left = self.removekeys(root.left,
                                       Min, Max)
        root.right = self.removekeys(root.right,
                                        Min, Max)
         
  
        if root.data < Min:
            rChild = root.right
            return rChild

        if root.data > Max:
            lChild = root.left
            return lChild