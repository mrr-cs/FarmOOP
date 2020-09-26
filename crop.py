import random
class Crop():

    def __init__(self,growthRate, lightNeed, waterNeed):
        self._growth_rate   =   growthRate
        self._days_growing  =   0 # defaults to zero
        self._light_need    =   lightNeed
        self._water_need    =   waterNeed
        self._status        =   'seed'
        self._type          =   'generic'

    def needs(self):
        return{'light need':self._light_need, 'water need':self._water_need}

    def report(self):
        return{'type':self._type,'status':self._status,'growth':self._growth_rate,'days growing':self._days_growing}

    def update_status(self):
        if self._growth_rate > 15:
            self._status='old'
        elif self._growth_rate > 10:
            self._status='mature'
        elif self._growth_rate > 5:
            self._status='young'
        elif self._growth_rate > 0:
            self._status='seedling'
        elif self._growth_rate == 0:
            self._status='seed'

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth_rate += self._growth_rate
        self._days_growing += 1
        self.update_status()

    def auto_grow(self, days):
        for day in range(days):
            light = random.randint(1,10)
            water = random.randint(1,10)
            self.grow(light,water)
            
    def manual_grow(self):
        valid = False
        while valid:
            try:
                light = int(input("please enter a light value (1to 10)"))
                if 1 <= light <=10:
                    valid =True
                else:
                    print("value entered is not valid")
            except ValueError:
                    print ("value entered not valid- please enter a value between 1 and 10")
                    
            valid = False
            while not valid:
                try:
                    water = int(input("please enter a water value (1-10)"))
                    if 1<= water <= 10:
                        valid =True
                    else:
                        print("value entered not valid")
                except:
                    print('blar')
