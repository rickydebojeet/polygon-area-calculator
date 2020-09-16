class Rectangle:
  
  #Initialization constructor
  def __init__(self, w, h):
    self.width = w
    self.height = h

  #Set width method
  def set_width(self, w):
    self.width = w

  #Set height method
  def set_height(self, h):
    self.height = h

  #Get Area method
  def get_area(self):
    return (self.width * self.height)

  #Get Perimeter method
  def get_perimeter(self):
    return ((2 * self.width) + (2 * self.height))

  #Get diagonal method
  def get_diagonal(self):
    return(((self.height ** 2) + (self.width ** 2)) ** 0.5)
  
  #




class Square:
