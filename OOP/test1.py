class Student:
    def __init__(self,name,class_grade,marksheet):
        self.name = name
        self.class_grade = class_grade
        self.marksheet = marksheet  

    
    def full_name(self, first_name, last_name):
        fullname = first_name + " " + last_name
        return fullname


ali = Student("Ali", "2", "B")
print(ali.name)
print(ali.fullname)
fullname = ali.full_name("Ali", "Alam")

print(fullname)

student2 = Student("Azhar", "5", "C")

ali.full_name