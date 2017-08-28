# migrated from python 2.7
'''
Created on 26-Aug-2016
​
@author: milind
'''
​
class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south=[south,west]
        self.width_WE=width_WE
        self.width_NS=width_NS
        self.height=height
        
​
    def corners(self):
        dic={'north-west': [3, 2], 'north-east': [3, 4], 'south-west': [1, 2], 'south-east': [1, 4]}
        dic['north-west']=[self.south[0]+self.width_NS,self.south[1]]
        dic['north-east']=[self.south[0]+self.width_NS,self.south[1]+self.width_WE]
        dic['south-west']=self.south
        dic['south-east']=[self.south[0],self.south[1]+self.width_WE]
        return dic
​
    def area(self):
        return self.width_NS*self.width_WE
​
    def volume(self):
        return self.width_NS*self.width_WE*self.height
​
    def __repr__(self):
        s="Building("+str(self.south[0])+", "+str(self.south[1])+", "+str(self.width_WE)+", "+str(self.width_NS)+", "+str(self.height)+")"
        return s
​
​
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in list(d.items()))
​
    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"