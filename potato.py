from WillJCropOOP import *

class Potato(Crop):

    def __init__(self):
        super().__init__(1,2,6)
        sel._type = "Potato"
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
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())
if __name__=="__main__":
    main()
        
        
