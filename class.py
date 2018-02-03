class Parent:

  def __init__(self):
    print("Calling parent constructor")

  def parentMethod(self):
    print( 'Calling parent method')

class Child(Parent):
    counter = 0
    def __init__(self):
        Child.counter += 1
        print("Calling child constructor")

    def childMethod(self):
     print( 'Calling child method')

c = Child()
d = Child()
c.childMethod()
c.parentMethod()
print(c.counter)