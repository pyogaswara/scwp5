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
      contents_size=len(self.contents)
      if number_of_balls_drawn < (len(self.contents)):
        for balls in range (0,number_of_balls_drawn):    
            pop_index=random.randint(0,contents_size-1)
            self.drawn_balls.append(self.contents.pop(pop_index))
            contents_size=contents_size-1
        print(self.drawn_balls)
        return self.drawn_balls
        
      else:
        self.drawn_balls=self.contents
        return self.drawn_balls

def experiment(**kwargs):

  hat_instance=kwargs["hat"]
  expected_balls=kwargs["expected_balls"]
  num_balls_drawn=kwargs["num_balls_drawn"]
  num_experiments=kwargs["num_experiments"]

    #print(kwargs)
    #print(hat_instance)
    #print(expected_balls)
    #print(num_balls_drawn)
    #print(num_experiments)
  drawn_balls=hat_instance.draw(num_balls_drawn)
  print(expected_balls)
  print(drawn_balls.count("red"))
  print(drawn_balls.count("green"))
  if (drawn_balls.count("red") >= 2) and (drawn_balls.count("green")==1):
    print("test")
  

   # return kwargs, hat_instance, num_balls_drawn
