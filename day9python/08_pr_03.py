class Attribute:
    a = 100


object = Attribute()
object.a = 0


print(Attribute.a)
print(object.a)
