class Board:
    count=0
    rows=8
    cols=8
    def __init__(self): 
        Board.count+=1
        self.board_id=Board.count
        self.matrix= [([0]*Board.rows) for i in range(Board.cols)]
        self.players=[]

    def join_player(self,p):
        self.players.append(p)

    def insert_chip(self,c,p):
        c=c-1
        for i in reversed(range(Board.cols)):
            if self.matrix[i][c]==0:
                self.matrix[i][c]=p
                break
        for i in range (Board.cols):
            print(self.matrix[i])

    def turn(self):
        while self.win_condition()!= True :
            c=0
            for i in range (len(self.players)):
                a=self.players[i].make_move()
                self.insert_chip(a,self.players[i].player_id)
                self.players[i].add_move(a)
                if self.win_condition() == True:
                    #por si sirve mas adelante
                    #self.players[i].set_result()
                    break

    def get_result(self,p):
        if self.win_condition()== True:
            p.set_result()

    def win_condition(self):
        for i in range(Board.cols):
            for j in range (Board.rows-3):
                if self.matrix[i][j]== self.matrix[i][j+1] and self.matrix[i][j]== self.matrix[i][j+2] and self.matrix[i][j]== self.matrix[i][j+3] and  self.matrix[i][j]!=0 :
                    print("ganaste")
                    return True
        for i in range(Board.cols-3):
            for j in range (Board.rows):
                if self.matrix[i][j]== self.matrix[i+1][j] and self.matrix[i][j]== self.matrix[i+2][j] and self.matrix[i][j]== self.matrix[i+3][j] and  self.matrix[i][j]!=0 :
                    print("ganaste")
                    return True
        for i in range(Board.cols-3):
            for j in range (Board.rows-3):
                 if self.matrix[i][j] == self.matrix[i+1][j+1] and self.matrix[i][j] == self.matrix[i+2][j+2] and self.matrix[i][j] == self.matrix[i+3][j+3] and self.matrix[i][j]!=0:
                     print("ganaste")
                     return True
        for i in range(Board.cols-3):
            for j in range (Board.rows-3):
                 if  self.matrix[i][j] == self.matrix[i+1][j-1] and self.matrix[i][j] == self.matrix[i+2][j-2] and self.matrix[i][j] == self.matrix[i+3][j-3] and self.matrix[i][j]!=0:
                     print("ganaste")
                     return True
        return False

    #metodo que me devuelve si la matriz esta llena o no    
    def tie_by_full_board(self):
       c=0
       for i in range(Board.cols):
           for j in range (Board.rows):
               if self.matrix[i][j]!=0 :
                   c=c+1
                   if c==64:
                        return True     
          
class Player:
    count=0
    def __init__(self,result=None,turn=None):
        Player.count+=1
        self.player_id=Player.count
        self.move=[]
        self.result=result
    
    def add_move(self,m):
        self.move.append(m)

    def make_move(self):
        print("Turno del jugador"+str(self.player_id))
        a=int(input("seleccione la posicion de su jugada"))
        return a

    def set_result(self):
        self.result="win"



#main
b1=Board()
p1=Player()
p2=Player()
b1.join_player(p1)
b1.join_player(p2)

#b1.turn()


