class Hat:
    def __init__(self,**kwargs):
      self.contents=[]
      self.contents_keys=[]
      self.contents_values=[]
      print(kwargs)
      for keys in kwargs.keys():
        self.contents_keys.append(keys)
      print(self.contents_keys)
      for keys in kwargs.keys():
        ball_multiplier=kwargs[keys]
        for ball in range (0,ball_multiplier):
            self.contents.append(keys)
      print(self.contents)
      
    def draw(self,number_of_balls_drawed):
        pass