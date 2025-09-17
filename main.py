class car:
    def __int__(self,color,model):
        self.color = color
        self.model = model
    def my_info(self):
        print(f"my car:{self.color},model:{self.model}")
mycar=car("yellow","pejoct")
mycar.my_info()
