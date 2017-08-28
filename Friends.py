'''
Created on 26-Aug-2016
​
@author: milind
'''
class Friends:
    def __init__(self, connections):
        self.connections=[]
        for x in connections:
            y=set(sorted(x))
            if y not in self.connections:
                self.connections.append(y)
            
    def add(self, connection):
        c=set(sorted(connection))
        if c in self.connections:
            return False
        else:
            self.connections.append(c)
            return True
            
    def remove(self, connection):
        c=set(sorted(connection))
        if c not in self.connections:
            return False
        else:
            self.connections.remove(c)
            return True
​
    def names(self):
        SetUnion=set
        for x in self.connections:
            SetUnion=SetUnion.union(x)
        return SetUnion
​
    def connected(self, name):
        conn=set()
        for (x,y) in self.connections:
            if x==name:
                conn.add(y)
            elif y==name:
                conn.add(x)
        return conn
​
​
​
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    
​