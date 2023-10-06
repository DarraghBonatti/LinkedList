
  
# Linked list Node
  
  
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.prev = None
  
  
class LinkedList:
    def __init__(self):
        self.head = None  # head of list
  
    def push(self, new_data):
  
        # 1 & 2: Allocate the Node &
        # Put in the data
        new_node = Node(new_data)
  
        # 3. Make next of new Node as head
        new_node.next = self.head
  
        # 4. Move the head to point to new Node
        self.head = new_node

    def printing(self):
       current = self.head
       while current != None:
           print(current.data)
           current = current.next

    def identical(self,listb):
        a = self.head
        b = listb.head

        while a != None and b != None:
            if a.data != b.data:
                return False
            else:
                a = a.next
                b = b.next

                if (a==None and b==None):
                    return True


    def getNthNode(self, n):
        current = self.head
        counter = 1

        while current:
            if counter == n:
                return current.data
            else:
                current = current.next
                counter += 1
        return 0

    def reversal(self):
        
        current = self.head
        previous = None

        while current is not None:
            #store the next node in next_node
            next_node = current.next 
            #set the current nodes next pointer to previous
            current.next = previous
            #update previous to the current node so next iteration we can assign it as a next pointer
            previous = current
            #move current node onto the next node
            current = next_node
        #the last node stored in previous is now the head
        self.head = previous


    def banish(self, value):
        current = self.head
        while current != None:
            if current.next.data == value:
                bad_node = current.next
                current.next = bad_node.next
                break
            else:
                current = current.next


        

        




        

           
           


  
  
# Driver Code
if __name__ == "__main__":
  

    list1 = LinkedList()
    list1.push(1)
    list1.push(2)
    list1.push(3)
    list1.push(4)
    list1.push(5)
    # list1.reversal()
    list1.printing()
    list1.banish(4)
    list1.printing()
    # list1.reversal()
    # list1.printing()
    # list1.reversal()
    
    # list1.printing()
    # list2 = LinkedList()
    # list2.push(1)
    # list2.push(2)
    # list2.push(3)
    # list2.push(4)
    # if list1.identical(list2) == True:
    #     print("IDENTICAL")
    # else:
    #     print("not")

    # # print(list1.getNthNode(10))
    # print(list1.printing())
    # list1.reversal()
    # print(list1.printing())
   
    
  
  
  # The constructed linked lists are :
  # llist1: 3->2->1
  # llist2: 3->2->1
 
  # Function call
  
