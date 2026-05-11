class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_average(self):
        return sum(self.marks) / len(self.marks)
    
    def get_grade(self):
        average = self.get_average()
        if average >= 90:
            return "A+"
        elif average >= 80:
            return  "A"
        elif average >= 70:
            return "B+"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "Fail"
    
    def is_passing(self):
        return self.get_average() >= 50
    
    def __str__(self):
        return f"{self.name} | Avg: {self.get_average():.2f} | Grade: {self.get_grade()}"
    
student1 = Student("Arun", 20, [45,25,89,65,74])
print(student1) 