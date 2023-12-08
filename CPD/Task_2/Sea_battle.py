import random
class Ship:
    def __init__(self,length=int,tp=1,x=None,y=None):
        self._x=x
        self._y=y
        self._length=length
        self._tp=tp
        self._is_move=True
        self._cells=[1 for _ in range(length)]

    def set_start_coords(self,x,y):
        self._x=x
        self._y=y
    def get_start_coords(self):
        return (self._x,self._y)
    def move(self,go):
        if self._is_move == False:
            return
        if self._tp == 1:
            self._x += go
        else:
            self._y +=go
    def is_collide(self,ship):
        if ship._tp==1:
            _s2=[(x,y) for x in range(ship._x-1,ship._x+ship._length+1) for y in range(ship._y-1, ship._y+2)]
            _s4 = [(x,y) for x in range(ship._x,ship._x+ship._length) for y in range(ship._y, ship._y+1)]
        elif ship._tp==2:
            _s2=[(x, y) for x in range(ship._x-1,ship._x+2) for y in range(ship._y-1, ship._y + ship._length+1)]
            _s4 = [(x, y) for x in range(ship._x,ship._x+1) for y in range(ship._y, ship._y + ship._length)]
        if self._tp==1:
            _s1=[(x, y) for x in range(self._x-1,self._x+self._length+1) for y in range(self._y-1, self._y+2)]
            _s3 = [(x, y) for x in range(self._x,self._x+self._length) for y in range(self._y, self._y+1)]
        elif self._tp==2:
            _s1=[(x, y) for x in range(self._x-1,self._x+2) for y in range(self._y-1, self._y+self._length+1)]
            _s3 = [(x, y) for x in range(self._x,self._x+1) for y in range(self._y, self._y+self._length)]
        if set(_s1).intersection(set(_s4)) or set(_s2).intersection(set(_s3)):
            return True
        else:
            return False
    def is_out_pole(self,size):
        if self._tp==1:
            if self._x+self._length>size or self._x>size:
                return True
            else:
                return False
        else:
            if self._y+self._length>size or self._y>size:
                return True
            else:
                return False
    def __getitem__(self,item):
        return self._cells[item]
    def __setitem__(self,key,value):
        self._cells[key] = value
class GamePole:
    def __init__(self,size=10) -> None:
        self._size = size
        self._ships = []
    def init(self):
        flag = True
        while flag:
            self._ships = [Ship(1,random.randint(1,2)),Ship(1,random.randint(1,2)),Ship(1,random.randint(1,2)),Ship(1,random.randint(1,2)),
                        Ship(2,random.randint(1,2)),Ship(2,random.randint(1,2)),Ship(2,random.randint(1,2)),
                        Ship(3,random.randint(1,2)),Ship(3,random.randint(1,2)),
                        Ship(4,random.randint(1,2))]
            for i in range(10):
                self._ships[i].set_start_coords(random.randint(0,self._size-1),random.randint(0,self._size-1))
            flag = False
            for i in self._ships:
                for j in self._ships:
                    if i!=j and (i.is_collide(j) or i.is_out_pole(self._size)):
                        flag = True
                        break
    def get_ships(self):
        return self._ships
    def move_ships(self):
        for i in range(10):
            if self._ships[i]._is_move == True:
                self._ships[i].move(1)
                for j in range(10):
                    if i!=j and (self._ships[i].is_collide(self._ships[j]) or self._ships[i].is_out_pole(self._size)):
                        self._ships[i].move(-2)
                        for k in range(10):
                            if i!=k and (self._ships[i].is_collide(self._ships[k]) or self._ships[i].is_out_pole(self._size)):
                                self._ships[i].move(1)
    def show(self):
        h_sea = [[0 for _ in range(self._size)] for _ in range(self._size)]
        b_sea = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for i in self._ships:
            if i._tp == 1:
                b_sea[i._y][i._x:i._x+i._length] = i._cells
            else:
                for j in range(i._length):
                    b_sea[i._y+j][i._x] = i._cells[j]
        for i in b_sea:
            print(*i)
    def get_pole(self):
        pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for i in self._ships:
            if i._tp == 1:
                pole[i._y][i._x:i._x+i._length] = i._cells
            else:
                for j in range(i._length):
                    pole[i._y+j][i._x] = i._cells[j]
        field = []
        for i in pole:
            field.append(tuple(i))
        return tuple(field)
class SeaBattle:
    def __init__(self,x,y,ships,shii) -> None:
        self.shot = (x,y)
        self._size = ships._size
        self._ships = ships._ships
        self._human_ships = shii
        self.coord=[]
        self.coord2=[]
        self.checkin()
        self.chekif()
    def checkin(self):
        for i in self._ships:
            if i._tp==1:
                self.coord.append([(x,y) for x in range(i._x,i._x+i._length) for y in range(i._y,i._y+1)])
            else:
                self.coord.append([(x,y) for x in range(i._x,i._x+1) for y in range(i._y,i._y+i._length)])
        for i in self.coord:
            if self.shot in i:
                korabl = self.coord.index(i)
                place = i.index(self.shot)
                self._ships[korabl]._cells[place] = 2
                self._ships[korabl]._is_move = False
    def chekif(self):
        self.bshot = (random.randint(0,self._size),random.randint(0,self._size))
        for i in self._human_ships:
            if i._tp==1:
                self.coord2.append([(x,y) for x in range(i._x,i._x+i._length) for y in range(i._y,i._y+1)])
            else:
                self.coord2.append([(x,y) for x in range(i._x,i._x+1) for y in range(i._y,i._y+i._length)])
        for i in self.coord2:
            if self.bshot in i:
                korabl2 = self.coord2.index(i)
                place2 = i.index(self.bshot)
                self._human_ships[korabl2]._cells[place2] = 2
                self._human_ships[korabl2]._is_move = False
sh1=Ship(1,1,1,1)
sh2=Ship(1,1,1,4)
sh3=Ship(1,2,1,7)
sh4=Ship(1,2,1,10)
sh5=Ship(2,1,4,5)
sh6=Ship(2,2)
sh7=Ship(2,1)
sh8=Ship(3,1)
sh9=Ship(3,2)
sh10=Ship(4,2)
sh1.set_start_coords(1,1)
sh2.set_start_coords(1,4)
sh3.set_start_coords(1,7)
sh4.set_start_coords(1,10)
sh5.set_start_coords(4,5)
sh6.set_start_coords(5,1)
sh7.set_start_coords(7,3)
sh8.set_start_coords(10,10)
sh9.set_start_coords(12,12)
sh10.set_start_coords(5,10)
Myships=[sh1,sh2,sh3,sh4,sh5,sh6,sh7,sh8,sh9,sh10]
p=GamePole(10)
p.init()
gg=False
while not(gg):
    Su=0
    Su2=0
    for i in p._ships:
        Su+=sum(i._cells)
    for i in Myships:
        Su2+=sum(i._cells)
    if (Su or Su2) == -20:
        gg=True
    
    else:
        SeaBattle(int(input()),int(input()),p,Myships)
        p.show()
        p.move_ships() 