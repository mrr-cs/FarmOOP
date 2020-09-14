class Animals():
    def __init__(self, growth_rate, food_need, water_need ):
        self._growth=0
        self._days_growing=0
        self._food_need = food_need
        self._water_need = water_need
        self._status = 'baby'

    def needs(self):
        return{'light need':self._light_need, 'water need':self._water_need}

    def report(self):
        return{'type':self._type,'status':self._status,'growth':self.growth,'days growing':self.days_growing}

    

    def update_status(self):
        if self._growth > 100:
            self._status='old'

        elif self._growth > 40:
            self._status='mature'

        elif self._growth > 20:
            self._status='young'
        elif self._growth > 0:
            self._status='adolecent'
        elif self._growth == 0:
            self._status='baby'

    def grow(self,light,food):
        if light>=self._food_need and water>=self._water_needs:
            self._growth += self._growth_rate
        self._days_growing += 1
        self.update_status()






def New_animal():
    new_animal = Animals(11,9,13)
    print(new_animal._status)
    print(new_animal._food_need)
    print(new_animal._water_need)
New_animal()
