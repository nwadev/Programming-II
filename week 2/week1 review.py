'''class Student:
    #objects is whats in the class
    #variables = attributes 
    #functions = methods
    pass
    
    
#objects outside f class so new objects dont have same attributes    
student1 = Student()
student1.name = "Harry"
student1.marks = 85

print(student1.name)
print(student1.marks)

'''


'''
class Student:
    def check_pass_fail(self):     #created a method , checks if student passes
        if self.marks >= 40:
            return True
        else:
            return False
            

student1 = Student()       #create a copy of object and give it a name student1
student1.name = "Harry"    # give that copy of object attributes / values
student1.marks = 85

did_pass = student1.check_pass_fail() #called method without passing an arguments
print(f"{student1.name}'s score was {student1.marks} passrate: {did_pass}")

student2 = Student()
student2.name = "jose"
student2.marks = 35
did_pass = student2.check_pass_fail()


    
print(f"{student2.name}'s score was {student2.marks} passrate: {did_pass}")

'''

'''
# init method is a speial method that automatically gets called everytime objects are creates


class Student:
    def check_pass_fail(self):     #created a method , checks if student passes
        if self.marks >= 40:
            return True
        else:
            return False
            
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
        
        
student1 = Student("Harry", 85)  #another class method , but uses init , so any atrributes "in" student get asiagnedthrough te init method and call outside the fuction
student2 = Student("Janet",30)    
   
student1pass_fail = student1.check_pass_fail()     
student2pass_fail = student2.check_pass_fail() 
print(f"{student1.name} has a score of {student1.marks} and their pass/fail result is:  {student1pass_fail}")
print(f"{student2.name} has a score of {student2.marks} and their pass/fail result is:  {student2pass_fail}")

'''


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)

        return result


n1 = Complex(5, 6)
n2 = Complex(-4, 2)
result = n1.add(n2)
print("real =", result.real)
print("imag =", result.imag)
