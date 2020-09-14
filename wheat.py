from WillJCropOOP import *

class Wheat(Crop):

    def __init__(self):
        super().__init__(5,7,8)
        sel._type = "Wheat"
    def grow(self,light,water):
        if light>=self._light_need and water >= self._water_need:
            if self._status == "seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status== "young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:self._growth += self._growth_rate
        self._days_growing +=1
        self._update_status()

def main():
    Wheat_crop = Wheat()
    print(Wheat_crop.report())
    manual_grow(Wheat_crop)
    print(Wheat_crop.report())
if __name__=="__main__":
    main()
        
