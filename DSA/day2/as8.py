#DSA-Assgn-8
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

class BakeHouse:
    def __init__(self):
        self.__occupied_table_list=LinkedList()
    #Implement other methods here
    def get_occupied_table_list(self):
        return self.__occupied_table_list
    
    def allocate_table(self):
        for element in range(1,11):
            if not self.__occupied_table_list.find_node(element):
                self.__occupied_table_list.add(element)
                break
        
        temp_list = []
        temp = self.__occupied_table_list.get_head()
        while temp:
            temp_list.append(temp.get_data())
            temp = temp.get_next()

        temp_list.sort()
        self.__occupied_table_list = LinkedList()
        for element in temp_list:
            self.__occupied_table_list.add(element)

    def deallocate_table(self,table_number):
        temp = self.__occupied_table_list.find_node(table_number)
        if temp:
            self.__occupied_table_list.delete(temp.get_data())

    
bakehouse=BakeHouse()
bakehouse.get_occupied_table_list().add(1)
bakehouse.get_occupied_table_list().add(5)
bakehouse.get_occupied_table_list().add(6)
bakehouse.get_occupied_table_list().add(7)
bakehouse.allocate_table()
bakehouse.get_occupied_table_list().display()
#Invoke the methods of BakeHouse class and test the program
                                                    