from random import shuffle
from card import Card
from queue_list import Queue
class Deck(Queue):
    """
    This class represents a Deck of Cards. This class inherits from
    the Queue class, which has a Python list to hold the Cards in 
    the Deck. The Cards are enqueued which adds them to the end of 
    the Python list. The Cards are dequeued when dealt which removes 
    them from the front of the Python list.
    
    There are no instance variables for this class, except for those
    inherited from the Queue class: The Python list: self._items

    The class methods include 
    a. __init__: This method is the Deck constructor. Call the Queue 
                 constructor.
    b. initialize: This method initializes all 52 Cards with their 
                   suit and rank.
    c. add_card: This method adds a Card to the Deck using enqueue.
    d. deal: This method removes the first Card from the Deck using 
             dequeue.
    e. shuffle: This method uses the random class shuffle method that 
                accepts a Python list as an argument and shuffles the 
                elements of the Queue's Python list and returns the 
                shuffled Deck.
    f. __str__: This method returns a string containing the Cards 
                in the Deck: 13 Cards to a line - The "\n" character 
                is added for every 13th Card
    """
    
    def __init__(self):
        """
        This method is the Deck constructor. Call the Queue 
        constructor using super().
        """
        ## Add your code here ##
        super().__init__()
    
    def initialize(self):    
        """
        This method initializes the Deck with 52 Cards. Both the suits 
        and ranks are integers: 
        Suits: 0=Clubs, 1=Diamonds, 2=Hearts, 3=Spades
        Ranks: 1 = Ace, 2-10 = 2-10, 11 = Jacks, 12 = Queen, 13 = King
        """
        ## Add your code here ##
        for suit in range(0, 4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.enqueue(card)
        
        
    def add_card(self, card):
        """
        This method adds a Card to the Deck using enqueue.
        """
        ## Add your code here ##
        self.enqueue(card)

    def deal(self):
        """
        This method removes the first Card from the Deck using 
        dequeue.
        """
        ## Add your code here ##
        self.dequeue()
        
    def shuffle(self):        
        """
        This method uses the random class shuffle method that accepts 
        a list as an argument to shuffle the elements of the Queue's 
        Python list and returns the shuffled Deck.
        """
        ## Add your code here ##
        return shuffle(self._items)
    
    def __str__(self):
        """
        This method returns a string containing the Cards in the Deck: 
        13 Cards to a line - The "\n" character is added for every 
        13th Card
        """
        ## Add your code here ##
        line = ""
        out = ""
        for i in range(1, len(self)+1):
            card = self._items[i-1]
            line += card.__str__() + " "
            if i % 13 == 0:
                out += line + "\n"
                line = ""
        return out
