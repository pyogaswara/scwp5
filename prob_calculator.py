import random
class Hat:
    def __init__(self,**kwargs):
      self.contents=[]
      self.contents_keys=[]
      self.contents_values=[]
      self.drawn_balls=[]
      print(kwargs)
      for keys in kwargs.keys():
        self.contents_keys.append(keys)
      print(self.contents_keys)
      for keys in kwargs.keys():
        ball_multiplier=kwargs[keys]
        for ball in range (0,ball_multiplier):
            self.contents.append(keys)
      print(self.contents)
      
    def draw(self,number_of_balls_drawn):
      print(len(self.contents))
      if number_of_balls_drawn >= (len(self.contents)):
        self.drawn_balls=self.contents
        return self.drawn_balls
      else:
        for balls in range (number_of_balls_drawn):      
          self.drawn_balls.append(self.contents.pop(random.randint(0,len(self.contents))))

        
        print(self.drawn_balls)
        print(self.contents)
        return self.drawn_balls
      
      