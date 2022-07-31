from inspect import _Object


class Appliction:
    def __init__(slf,name):
        slf.name = name()
        

object = Appliction("Gaurav")
print(object.name)
              