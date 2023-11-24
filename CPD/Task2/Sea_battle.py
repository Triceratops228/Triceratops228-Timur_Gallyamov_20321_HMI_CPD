import random
import time
class GamePole():
    def __init__(self,size=10) -> None:
        self._size=size
        self._ships=[Ship(1,random.randint(1,2)),Ship(1,random.randint(1,2)),Ship(1,random.randint(1,2)),Ship(1,random.randint(1,2)),Ship(2,random.randint(1,2)),Ship(2,random.randint(1,2)),Ship(2,random.randint(1,2)),Ship(3,random.randint(1,2)),Ship(3,random.randint(1,2)),Ship(4,random.randint(1,2))]
        self.start_time = time.time()
        self._cell_bot=_cell_bot
        self._cell_hum=_cell_hum
        self.bot_game()
    def coror2(self,ship):
        if ship._tp==1:
            _s=[(x,y) for x in range(ship._x,ship._x+ship._length) for y in range(ship._y, ship._y+1)]
            
            return _s
        else:
            _s=[(x, y) for x in range(ship._x,ship._x+1) for y in range(ship._y, ship._y + ship._length)]
            
            return _s
    def bot_game(self):
        possible_coord=[(x,y) for x in range(self._size) for y in range(self._size)]
        for i in range(10):
            flag=True
            while flag == True:
                elapsed_time = time.time() - self.start_time
                if possible_coord == []:
                    break
                x, y = random.choice(possible_coord)
                self._ships[i].set_start_bot(x,y)
                if i==0:
                    break
                for j in range(0,i):
                    if self._ships[i].is_collide(self._ships[j]) == True or self._ships[i].is_out_pole(self._size) == True:
                        #print(len(possible_coord))
                        #possible_coord.remove((x,y))
                        flag = True
                        del(_bot_coord[-1])
                        break
                    else:
                        if j==i-1:
                            possible_coord.remove((x,y))
                        flag = False
            self._cell_bot.append([[1 for j in range(self._ships[i]._length)],self.coror2(self._ships[i])])
    def get_ships(self):
        return self._ships
    def checkin(self,i):
        for j in self._ships:
            if i!=j and (i.is_collide(j) or i.is_out_pole(self._size)):
                return True
    def move_ships(self):
        for i in self._ships:
            i.move_bot(1)
            if self.checkin(i):
                i.move_bot(-2)
                if self.checkin(i):
                    i.move_bot(1)
                    #print("Нельзя")
            #print("ОК")
    def show(self):
        bot_sea=[[0 for i in range(self._size)] for ii in range(self._size)]
        h_sea=[[0 for i in range(self._size)] for ii in range(self._size)]
        zalupa=False
        print(" ")
        for i in range(len(_coord)):
            if _coord[i][3]==1:
                for x in range(_coord[i][2]):
                    h_sea[_coord[i][1]][_coord[i][0]+x] = _cell_hum[i][0][x]
            else:
                for x in range(_coord[i][2]):
                    h_sea[_coord[i][1]+x][_coord[i][0]] = _cell_hum[i][0][x]

                """ if elapsed_time>10:
                    self.start_time = time.time()
                    zalupa = True
                if zalupa:
                    break
            if zalupa:
                break
            if possible_coord == []:
                    break """
            #print(possible_coord)
        for i in range(len(_bot_coord)):
            if _bot_coord[i][3]==1:
                for x in range(_bot_coord[i][2]):
                    bot_sea[_bot_coord[i][1]][_bot_coord[i][0]+x] = _cell_bot[i][0][x]
                    #print(_cell_bot[i][0])
            else:
                for x in range(_bot_coord[i][2]):
                    bot_sea[_bot_coord[i][1]+x][_bot_coord[i][0]] = _cell_bot[i][0][x]
                    #print(_cell_bot[i][0])
        for i in h_sea:
            print(*i)
        print(" ")
        for i in bot_sea:
            print(*i)


class Ship:
    def __init__(self,length=int,tp=1,x=None,y=None) -> None:
        self._length=length
        self._tp=tp
        self._cell_hum=_cell_hum
        self._is_move=True
        self._coord=_coord
        self._bot_coord=_bot_coord
        #self._sea=[[0 for i in range(10)] for ii in range(10)]
    def coror(self):
        if self._tp==1:
            _s=[(x,y) for x in range(self._x,self._x+self._length) for y in range(self._y, self._y+1)]
            
            return _s
        else:
            _s=[(x, y) for x in range(self._x,self._x+1) for y in range(self._y, self._y + self._length)]
            
            return _s
    def set_start_coords(self,x,y):
        if (x<=0 or y<=0):
            print("Начинай с 1")
            return
        self._x=x
        self._y=y
        self._coord.append((self._x,self._y,self._length,self._tp))
        self._cell_hum.append([[1 for i in range(self._length)],self.coror()])
        
    def set_start_bot(self,x,y):
        self._x=x
        self._y=y
        self._bot_coord.append((self._x,self._y,self._length,self._tp))
        
    def get_start_coords(self):
        return (self._x,self._y)
    def move_bot(self,go):
        if self._is_move==False:
            return
        if self._tp==1:
            self._bot_coord[self._bot_coord.index((self._x,self._y,self._length,self._tp))] = (self._x+go,self._y,self._length,self._tp)
            self._x+=go
        else:
            self._bot_coord[self._bot_coord.index((self._x,self._y,self._length,self._tp))] = (self._x,self._y+go,self._length,self._tp)
            self._y+=go
    def move(self,go):
        if self._is_move==False:
            return
        if self._tp==1:
            self._coord[self._coord.index((self._x,self._y,self._length,self._tp))] = (self._x+go,self._y,self._length,self._tp)
            self._x+=go
        else:
            self._coord[self._coord.index((self._x,self._y,self._length,self._tp))] = (self._x,self._y+go,self._length,self._tp)
            self._y+=go
        
    def is_collide(self,ship):
        if ship._tp==1:
            _s2=[(x,y) for x in range(ship._x-1,ship._x+ship._length+1) for y in range(ship._y-1, ship._y+2)]
        elif ship._tp==2:
            _s2=[(x, y) for x in range(ship._x-1,ship._x+2) for y in range(ship._y-1, ship._y + ship._length+1)]

        if self._tp==1:
            _s1=[(x, y) for x in range(self._x-1,self._x+self._length+1) for y in range(self._y-1, self._y+2)]
        elif self._tp==2:
            _s1=[(x, y) for x in range(self._x-1,self._x+2) for y in range(self._y-1, self._y+self._length+1)]

        if set(_s1).intersection(set(_s2)):
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
class SeaBattle(GamePole):
    def __init__(self,x,y,shiper,shii) -> None:
        self.shoot = (x,y)
        self._ships=shiper._ships
        self._shii = shii
        self.checksh()
        self.killsh()
        
    def checksh(self):
        for i in _cell_bot:
            for j in i[1]:
                if j==self.shoot:
                    i[0][i[1].index(j)] = -1
                    print("Попал")
                    self._ships[_cell_bot.index(i)]._is_move = False
                    return
    def killsh(self):
        #print(_cell_hum)
        for i in _cell_hum:
            #print(i[1])
            for j in i[1]:
                if i[0][i[1].index(j)]!=-1:
                    i[0][i[1].index(j)] = -1
                    print("Попал")
                    #print(self._shii[_cell_hum.index(i)])
                    self._shii[_cell_hum.index(i)]._is_move = False
                    return
            

_cell_hum=[]
_cell_bot=[]
_coord=[]
_bot_coord=[]
_cell=[]
p=GamePole(15)
p.__init__

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
#sh3.is_collide(sh2)
#sh1.is_out_pole(10)
#print(_coord)
#print(_cell_bot)
#print(_cell_hum)
p.show()
#p.get_ships()
gg=False
while not(gg):
    Su=0
    Su2=0
    for i in _cell_hum:
        Su+=sum(i[0])
    for i in _cell_bot:
        Su2+=sum(i[0])
    if (Su or Su2) == -20:
        gg=True
    
    else:
        SeaBattle(int(input()),int(input()),p,Myships)
        p.show()
        p.move_ships()
#p.move_ships()
#p.show()
