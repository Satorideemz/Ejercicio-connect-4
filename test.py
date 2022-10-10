import unittest
from parameterized import parameterized

from connect4 import Board
from connect4 import Player

class TestConnect4(unittest.TestCase):
    #test que verifica la victoria por horizontal
    def test_horizontal(self):
        inputs=[1,2,3,4]
        b1=Board()
        p1=Player()
        #dejo esto por si sirve mas adelante
        #b1.join_player(p1)
        #b1.join_player(p2)
        for i in range(len(inputs)):
            b1.insert_chip(i+1,1)
        b1.get_result(p1)
        self.assertDictEqual(p1.__dict__,{'player_id': 5, 'move': [], 'result': 'win'})
    #test que verifica la vitctoria por vertical
    def test_vertical(self):
        inputs=[1,1,1,1]
        b1=Board()
        p1=Player()
        for i in range(len(inputs)):
            b1.insert_chip(i+1,1)
        b1.get_result(p1)
        self.assertDictEqual(p1.__dict__,{'player_id': 7, 'move': [], 'result': 'win'})
    def test_diagonal(self):
        inputs=[1,2]
        inputs2=[1,2,3]
        inputs3=[1,2,3,4]
        b1=Board()
        p1=Player()
        for i in range(len(inputs)):
            b1.insert_chip(i+1,1)
        for i in range(len(inputs2)):
            b1.insert_chip(i+1,2)
        b1.insert_chip(1,2)
        for i in range(len(inputs3)):
            b1.insert_chip(i+1,1)        
        b1.get_result(p1)
        self.assertDictEqual(p1.__dict__,{'player_id': 3, 'move': [], 'result': 'win'}) 
    def test_diagonal_2(self):
        inputs=[5,7,8]
        inputs2=[6,7,8]
        inputs3=[5,6,7,8]
        b1=Board()
        p1=Player()
        for i in range(len(inputs)):
            b1.insert_chip(i+1,1)
        for i in range(len(inputs2)):
            b1.insert_chip(i+1,2)
        b1.insert_chip(8,1)
        for i in range(len(inputs3)):
            b1.insert_chip(i+1,1)        
        b1.get_result(p1)
        self.assertDictEqual(p1.__dict__,{'player_id': 4, 'move': [], 'result': 'win'})         

    def test_tie(self):
        b1=Board()
        p1=Player()
        for i in range(8):
            for j in range (8):
                b1.insert_chip(i,1)
        self.assertEqual(b1.tie_by_full_board(),True)      

    def test_join_player(self):
        pass
    
    def insert_chip(self,c,p):
        pass
    def turn(self):
        pass
    def get_result(self,p):
        pass
    def add_move(self,m):
        pass
    def make_move(self):
        pass
    def set_result(self):
        pass
    
if __name__ == '__main__':
    unittest.main()                           