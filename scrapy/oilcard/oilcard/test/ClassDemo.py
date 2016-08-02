# -*- coding: utf-8 -*-

class ClassDemo:

    def __init__(self):
        self.name="test"


    def setAge(self, age):
        self.age = age
        print "age:" , self.age

    def getAge(self):
        print 'age:'  ,  self.age


obj = ClassDemo()
obj.setAge(100)

obj.getAge()