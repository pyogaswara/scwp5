import random
import copy

class Hat:
    def __init__(self,**kwargs):
      self.contents=[]
      self.contents_keys=[]
      self.contents_values=[]
      self.drawn_balls=[]
      print(kwargs)
      for keys in kwargs.keys():
        self.contents_keys.append(keys)
      #print(self.contents_keys)
      for keys in kwargs.keys():
        ball_multiplier=kwargs[keys]
        for ball in range (0,ball_multiplier):
            self.contents.append(keys)
      print(self.contents)
      
    def draw(self,number_of_balls_drawn):
      self.contents_copy=copy.deepcopy(self.contents)
      self.drawn_balls_copy=copy.deepcopy(self.drawn_balls)
      contents_size=len(self.contents_copy)
      #self.contents_copy=copy.deepcopy(self.contents)
      if number_of_balls_drawn < (len(self.contents_copy)):
        for balls in range (0,number_of_balls_drawn):    
            pop_index=random.randint(0,contents_size-1)
            self.drawn_balls_copy.append(self.contents_copy.pop(pop_index))
            contents_size=contents_size-1
        #print(self.drawn_balls_copy)
        print("bola di topi ada:",len(self.contents_copy),self.contents_copy)
        return self.drawn_balls_copy        
      else:
        self.drawn_balls_copy=self.contents_copy
        return self.drawn_balls_copy
      #print("waduuuuh",self.contents)
    

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
  
  print("diinginkan")
  print(expected_balls)
  print("yang terambil")
 

  keinginan_terpenuhi=0
  #hat_instance_copy=copy.deepcopy(hat_instance)
  for percobaan in range (0,100):
    print("percobaan ke",percobaan+1)
    drawn_balls=hat_instance.draw(num_balls_drawn)
    print("jumlah bola diambil:",num_balls_drawn,drawn_balls)
    daftar_permintaan=[]
    for color in expected_balls.keys():
      z=drawn_balls.count(color)
      mintanya=(expected_balls[color])
      print(color,"ada",z,"padahal mintanya",mintanya)
      if z >= mintanya:
        daftar_permintaan.append(1)
      else:
        daftar_permintaan.append(0)
    print(daftar_permintaan)
    if daftar_permintaan.__contains__(0):
      print("huhu")
      keinginan_terpenuhi=keinginan_terpenuhi+0
    else:
      print("haha")
      keinginan_terpenuhi=keinginan_terpenuhi+1
  print("yang sesuai keinginan ada:",keinginan_terpenuhi)
  
    
  


  