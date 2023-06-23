class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        
    def show(self):
       print("Heiio my name is " + self.name+" and I " + "work in "+self.company+".")
         
obj = GFG("john", "GeeksForGeeks")
obj.show()