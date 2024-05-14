class Person:
    def __init__(self,name):
        self.name=name
    def get_info(self):
        print("Аты:",self.name)

class Emplayee(Person):
    def job (self,job_name):
        print("Аты:"+ self.name,"Жұмысы:"+job_name)
Emplayee_obj=Emplayee("Kurmangazy")
Emplayee_obj.job("programmer")