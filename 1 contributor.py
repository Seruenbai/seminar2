
15 lines (11 sloc) 242 Bytes
from mybox import MyBox
from myboxiterator import MyBoxIterator
from myclass import Person

box=MyBox()
box.add(Person(16,25))
box.add(Person(56,89))
box.add(Person(67,90))
box.add(Person(62,98))
box.remove(0)

for item in box:
item.info()
