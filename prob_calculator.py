class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        panjang=len(kwargs)
        print(kwargs)
        print(panjang)
        print(type(kwargs))
        print(dir(kwargs))
    def draw(self,number_of_balls_drawed):
        pass