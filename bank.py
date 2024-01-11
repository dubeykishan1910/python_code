class SoftwareEngineer:

    alias = "main class"
    def __init__(self,name,age,level,salary):
        self.name= name
        self.age= age
        self.level = level 
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, langguage):
        print(f"{self.name} is writing code in {langguage}")
    
    def __str__(self):
        information = f"name = {self.name}, age = {self.age} level = {self.level}"
        return information

se1 = SoftwareEngineer("maz",55,"junior",5511222)
se2 = SoftwareEngineer("kishan",53,"senior",452035)
se1.code()

print(se1)