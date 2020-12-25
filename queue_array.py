
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.list = [None]*capacity
        self.num_items = 0
        self.front = 0 #this is the index for the front in the array
        self.back = 0 #this is the index for the back in the array
        #front and back attributes are declared here^^


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True

        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True

        return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise IndexError

        #places the item in the index indicated by the back attribute
        self.list[self.back] = item
        #adds 1 to the back attribute 
        self.back += 1
        #checks if back was at the end of the array and if so sets back to index 0 
        if self.back > self.capacity-1:
            self.back = 0
        #adds 1 to num_items attribute
        self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise IndexError

        #adds 1 to the front making the new "front" the next index
        self.front += 1
        #creates a variable return_index in order to return the dequeued front
        return_index = self.front-1
        #checks to see if the front was at the end of the array and if so resets it to 0
        if self.front > self.capacity-1:
            self.front = 0
        #subtracts 1 from total of num_items
        self.num_items -= 1
        #returns the old front 
        return self.list[return_index]


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items

