class point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def sqSum(self):
        print("squre :", self.x**2, self.y**2, self.z**2)
        print("square_sum :",self.x**2+self.y**2+self.z**2)          


obj = point(1,3,5)  
obj.sqSum()