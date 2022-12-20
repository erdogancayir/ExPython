class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

name = getattr(person, 'name')

print(name)

#------------------------------------------
class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

# set value of name to Adam
setattr(person, 'name', 'Adam')

print(person.name)
