class Rectangle:
  shape = "Rectangle"

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
  
  #Get picture method
  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      output = ""
      for x in range(self.height):
        output = output + ("*" * self.width) + "\n"
      return output
  
  #Get amount inside method
  def get_amount_inside(self, cat):
    main = self.get_area()
    inside = cat.get_area()
    times = int(main / inside)
    return times

  #Return Value
  def __str__(self):
    op = self.shape + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return op

class Square(Rectangle):
  shape = "Square"

  #Initialization of constructor
  def __init__(self, s):
    self.width = s
    self.height = s

  #Set side method
  
