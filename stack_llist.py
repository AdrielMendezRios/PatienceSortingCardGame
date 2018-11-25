from copy import deepcopy
class _StackNode():
    """
    This class represents the Node of a Stack implemented as a 
    LinkedList.
    
    The instances variables of this class include:
    1. self.item: holds the item for the StackNode.
    2. self.next: holds the pointer to the next StackNode.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 each instance variable to the passed in parameters.
    """
    
    def __init__(self, item, link):
        """
        This method is the constructor and it initializes each
        nstance variable to the passed in parameters.
        """
        ## Add your code here ##
        self.item = item
        self.link = link
        
    def __str__(self):
        return "NodeItem: "+str(self.item)
        
class Stack():
    """
    This Stack class is a singly LinkedList implementation of a Stack.
    
    The instances variables of this class include:
    1. self._top: holds the pointer to the top StackNode of the Stack
    2. self._size: holds the number of StackNode on the Stack.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 the Stack instance variables.
    b. is_empty: This method returns True, if the Stack  is empty or 
                 False otherwise.
    c. __len__: This method returns the number of items in the Stack.
    d. peek: This method returns the top item on the Stack without 
             removing it.
    e. pop: This method removes and returns the top item on the Stack.
    f. push: This method pushes an item onto the top of the Stack.
    g. __str__: This method returns the contents of the Stack as a 
                string. 
    """
    
    def __init__(self):
        """
        This method is the constructor and it initializes the Stack 
        instance variables, creating an empth Stack.
        """
        ## Add your code here ##
        self._top = None
        self._size = 0


    def is_empty(self):
        """
        This method returns True if the Stack is empty or False 
        otherwise.
        """
        ## Add your code here ##

        return self._size <= 0

    def __len__(self):
        """
        This method returns the number of items in the Stack.
        """
        ## Add your code here ##
        return self._size

    def peek(self):
        """
        This method returns the top item on the Stack without 
        removing it.
        """
        ## Add your code here ##

        return self._top.item

    def pop(self):
        """
        This method removes and returns the top item on the Stack.
        """
       
        node = self._top
        if node.link is not None:
            self._top = node.link
        self._size -= 1
        return node.item
        
        
        ## Add your code here ##

    def push(self, item):
        """
        This method pushes an item onto the top of the Stack.
        """
        ## Add your code here ##
        node = _StackNode(item, None)
        if self._top is None:
            self._top = node
        else:
            node.link = self._top
            self._top = node
        self._size += 1
        
    def __str__(self):
        """
        This method returns the contents of the Stack as a string
        """
        ## Add your code here ##
        item_str = ""
        current = self._top
        for i in range(len(self)):
            item_str += str(current.item) + " "
            current = current.link
        return item_str