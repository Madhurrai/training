class train:

    def __init__(self,name,age,team):
            self.name=name
            self.age=age 
            self.team=team

    def show(self):
        print(self.name)
        print(self.age)
        print(self.team)


def create(name,age,team):
    p=train(name,age,team)
    return p


c=create("Madhur",22,"INS")
c.show()






