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
    
class LibraryManagement:

    def __init__(self):
        self.books = {} #key = book_id, value = book_data in clude title, author, year
        self.root = None
        self.avl = avltree()
        
    def insert(self, book_id, book_data):
        self.root = self.avl.insert(self.root,book_id)
        self.books[book_id] = book_data
        
    def delete(self, book_id):
        self.root = self.avl.delete(self.root, book_id)
        del self.books[book_id]
        
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        print("Book ID:", root.id)
        print("Title:", self.books[root.id][0])
        print("Author:", self.books[root.id][1])
        print("Year:", self.books[root.id][2])
        print("________________________")
        self.inorder(root.right)
        
    def display(self):
        self.inorder(self.root)
        print()
        
    def searchbyid(self, book_id):
        if self.avl.search(self.root, book_id):
            print("________________________")
            print("Book ID:", book_id)
            print("Title:", self.books[book_id][0])
            print("Author:", self.books[book_id][1])
            print("Year:", self.books[book_id][2])
            print("________________________")
        else:
            print("BOOK NOT FOUND!")
    
    def id_traverse_author(self, root, author_name):
        # Search the inorder traversal of the tree to find the author
        if not root: return
        self.id_traverse_author(root.left, author_name)
        if self.books[root.id][1] == author_name:
            print("________________________")
            print("Book ID:", root.id)
            print("Title:", self.books[root.id][0])
            print("Author:", self.books[root.id][1])
            print("Year:", self.books[root.id][2])
            print("________________________")
        self.id_traverse_author(root.right, author_name)
        
    def searchbyauthor(self, author_name):
        self.id_traverse_author(self.root, author_name)
            
            
if __name__ == "__main__":
    #Test the library management
    libary = LibraryManagement()
    libary.insert(1, ('The Great Gatsby', 'F. Scott Fitzgerald', 1925))
    libary.insert(2, ('To Kill a Mockingbird', 'Harper Lee', 1960))
    libary.insert(3, ('1984', 'George Orwell', 1949))
    libary.insert(4, ('The Catcher in the Rye', 'J.D. Salinger', 1951))
    libary.insert(5, ('The Grapes of Wrath', 'John Steinbeck', 1939))
    libary.insert(6, ('Brave New World', 'Aldous Huxley', 1932))
    libary.delete(5)
    libary.insert(7, ('The Sound and the Fury', 'William Faulkner', 1929))
    libary.display()