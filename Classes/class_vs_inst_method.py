class Human:
  default_org = "Nose"                            
  def __init__(self, eyes, ears, name):
    self.eyes = eyes
    self.ears = ears
    self.name = name

  def human_function(self):
    print(f"{self.name} has {self.eyes} eyes and {self.ears} ears")

khalid = Human(2, 2, "Khalid")
nameera = Human(1, 2, "Nameera")
print(nameera.default_org)                 
print(Human.default_org)                   
nameera.human_function()
khalid.human_function()