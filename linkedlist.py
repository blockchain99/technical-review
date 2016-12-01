# '''
# Created on Nov 30, 2016
# 
# @author: Gloria
# '''
# '''There isn't a built-in data structure in Python that looks like a linked list. 
# Thankfully, it's easy to make classes that represent data structures in Python! 
# 
# Here's the code for an Element, which will be a single unit in a linked list:'''
# class Element1(object):
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         
# '''This code is very similar—we're just establishing that a LinkedList is something 
# that has a head Element, which is the first element in the list. If we establish 
# a new LinkedList without a head, it will default to None. '''
#         
# class LinkedList1(object):
#     def __init__(self, head=None):
#         self.head = head
#         
# '''Great! Let's add a method to our LinkedList to make it a little more useful. 
# This method will add a new Element to the end of our LinkedList.'''
#     def append(self, new_element):
#         current = self.head
#         if self.head:
#             while current.next:
#                 current = current.next
#             current.next = new_element
#         else:
#             self.head = new_element
            
# '''If the LinkedList already has a head, iterate through the next reference in every Element 
# until you reach the end of the list. Set next for the end of the list to be the new_element. 
# Alternatively, if there is no head already, you should just assign new_element to it and do nothing else.'''
#             
#             
# """The LinkedList code from before is provided below.
# Add three functions to the LinkedList.
# "get_position" returns the element at a certain position.
# The "insert" function will add an element to a particular
# spot in the list.
# "delete" will delete the first element with that
# particular value.
# Then, use "Test Run" and "Submit" to run the test cases
# at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
#LinkedList is something that has a head Element, 
#which is the first element in the list.       
class LinkedList(object):   #
    def __init__(self, head=None): #if new LinkedList is without a head, it will default to None
        self.head = head
         
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
             
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        size_linkedlist = 1
        current = self.head
        if self.head:
            while current.next:
                current = current.next
                size_linkedlist += 1
            total_size = size_linkedlist
        else:
            total_size = 0
             
         
        initial_positon = 1
        current = self.head
        if self.head:
            if position < total_size+1:
                while initial_positon != position:
                    current = current.next
                    initial_positon +=1
                return current    
            else:
                return None
        else:
            return None
     
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        size_linkedlist = 1
        current = self.head
        if self.head:
            while current.next:
                current = current.next
                size_linkedlist += 1
            total_size = size_linkedlist
        else:
            total_size = 0
             
         
        initial_positon = 1
        current = self.head
        if self.head:
            if position < total_size+1:
                while initial_positon != position-1:
                    current = current.next
                    initial_positon +=1
                current.next = new_element   
            else:
                return None
        else:
            self.head = new_element
        pass
     
     
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if self.head:
            while current.next != value:
                current = current.next
            current.next = current.next.next
        else:
            pass
 
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
 
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
 
# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value
 
# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value
 
# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value