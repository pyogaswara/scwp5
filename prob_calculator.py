import random
import copy

class Hat:
    def __init__(self,**kwargs):
      self.contents=[]
      self.contents_keys=[]
      self.contents_values=[]
      self.drawn_balls=[]
      for keys in kwargs.keys():
        self.contents_keys.append(keys)
      for keys in kwargs.keys():
        ball_multiplier=kwargs[keys]
        for ball in range (0,ball_multiplier):
            self.contents.append(keys)

    def draw(self,number_of_balls_drawn):
      self.contents_copy=copy.deepcopy(self.contents)
      self.drawn_balls_copy=copy.deepcopy(self.drawn_balls)
      contents_size=len(self.contents_copy)

      if number_of_balls_drawn < (len(self.contents_copy)):
        for balls in range (0,number_of_balls_drawn):    
            pop_index=random.randint(0,contents_size-1)
            self.drawn_balls_copy.append(self.contents_copy.pop(pop_index))
            contents_size=contents_size-1
        return self.drawn_balls_copy        
      else:
        self.drawn_balls_copy=self.contents_copy
        return self.drawn_balls_copy
    

def experiment(**kwargs):
  hat_instance=kwargs["hat"]
  expected_balls=kwargs["expected_balls"]
  num_balls_drawn=kwargs["num_balls_drawn"]
  num_experiments=kwargs["num_experiments"]
  num_of_occurence=0
  for experiment in range (0,num_experiments):
    drawn_balls=hat_instance.draw(num_balls_drawn)
    expected_balls_list=[]
    for color in expected_balls.keys():
      num_color=drawn_balls.count(color)
      num_expected_color=(expected_balls[color])
      if num_color >= num_expected_color:
        expected_balls_list.append(1)
      else:
        expected_balls_list.append(0)
    if expected_balls_list.__contains__(0):
      num_of_occurence=num_of_occurence+0
    else:
      num_of_occurence=num_of_occurence+1
  print("Probability :",(num_of_occurence/num_experiments))
  
    
  


  