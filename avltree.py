class treenode(object):
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None
        self.height = 1
        
class avltree(object):   
    
    def lrotate(self,z):
        '''Make a left rotation at node z'''        
        #Perform the rotation
        y = z.right
        temporary = y.left
        y.left = z
        z.right = temporary
        
        #Update the height
        z.height = 1 + max(self.getheight(z.left), self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))
        return y
    
    def rrotate(self,z):
        '''Make a right rotation at node z'''        
        #Perform the rotation
        y = z.left
        temporary = y.right
        y.right = z
        z.left = temporary
        
        #Update the height
        z.height = 1 + max(self.getheight(z.left), self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))
        return y

    def getheight(self, root):
        '''Get the height of the node'''
        if not root:
            return 0
        return root.height

    def getbalance(self, root):
        '''Get the balance factor of the node'''
        if not root:
            return 0
        return self.getheight(root.left) - self.getheight(root.right)
    
    def insert(self, root, new_value):
        if not root : return treenode(new_value)
        if new_value < root.id:
            root.left = self.insert(root.left, new_value)
        else:
            root.right = self.insert(root.right, new_value)
        
        #Update the height of the node
        root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
        
        #Get the balance factor of the node
        b= self.getbalance(root)
        if b>1 and  new_value < root.left.id: return self.rrotate(root)
        if b<-1 and new_value > root.right.id: return self.lrotate(root)
        if b>1 and  new_value > root.left.id:
            root.left = self.lrotate(root.left)
            return self.rrotate(root)
        if b<-1 and new_value < root.right.id:
            root.right = self.rrotate(root.right)
            return self.lrotate(root)
        return root
    
    def _minvalue(self, root):
        current = root
        while current.left: current = current.left
        return current
    
    def delete(self, root, value):
        if not root: return root
        if value < root.id:
            root.left = self.delete(root.left, value)
        elif value > root.id:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._minvalue(root.right)
            root.id = temp.id
            root.right = self.delete(root.right, temp.id)
        if not root: return root
        root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
        b = self.getbalance(root)
        if b > 1 and self.getbalance(root.left) >= 0: return self.rrotate(root)
        if b > 1 and self.getbalance(root.left) < 0:
            root.left = self.lrotate(root.left)
            return self.rrotate(root)
        if b < -1 and self.getbalance(root.right) <= 0: return self.lrotate(root)
        if b < -1 and self.getbalance(root.right) > 0:
            root.right = self.rrotate(root.right)
            return self.lrotate(root)
        return root
    
    def search(self, root, value):
        if not root or root.id == value: return root
        if value < root.id: return self.search(root.left, value)
        return self.search(root.right, value)
    