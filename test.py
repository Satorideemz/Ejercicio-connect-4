import unittest
from parameterized import parameterized
from unittest.mock import patch
from connect4 import Board
from connect4 import Player
#El metodo turn no se testea ya que es parte del programa principal


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
        self.assertDictEqual(p1.__dict__,{'player_id': 7, 'move': [], 'result': 'win'})
    #test que verifica la vitctoria por vertical
    def test_vertical(self):
        inputs=[1,1,1,1]
        b1=Board()
        p1=Player()
        for i in range(len(inputs)):
            b1.insert_chip(i+1,1)
        b1.get_result(p1)
        self.assertDictEqual(p1.__dict__,{'player_id': 12, 'move': [], 'result': 'win'})
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
        self.assertDictEqual(p1.__dict__,{'player_id': 4, 'move': [], 'result': 'win'}) 
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
        self.assertDictEqual(p1.__dict__,{'player_id': 5, 'move': [], 'result': 'win'})         

    def test_tie(self):
        b1=Board()
        p1=Player()
        for i in range(8):
            for j in range (8):
                b1.insert_chip(i,1)
        self.assertEqual(b1.tie_by_full_board(),True)      

    def test_join_player(self):
        b1=Board()
        p1=Player()
        p2=Player()
        b1.join_player(p1)
        b1.join_player(p2)
        self.assertDictEqual(b1.__dict__,{'board_id': 8,
  'matrix': [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]],
  'players': [p1,p2]})

    def test_insert_chip(self):
        b1=Board()
        b1.insert_chip(1,1)
        self.assertDictEqual(b1.__dict__,{'board_id': 7,
  'matrix': [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0]],
  'players': []})   

    def test_get_result(self):
        inputs=[1,2,3,4]
        b1=Board()
        p1=Player()
        for i in range(len(inputs)):
            b1.insert_chip(i+1,1)
        b1.get_result(p1)
        self.assertDictEqual(p1.__dict__,{'player_id': 6, 'move': [], 'result': 'win'})

    def test_add_move(self):
        b1=Board()
        p1=Player()
        p1.add_move(3)
        self.assertDictEqual(p1.__dict__,{'player_id': 3, 'move': [3], 'result': None})

    def test_set_result(self):
        p1=Player()
        p1.set_result()
        self.assertDictEqual(p1.__dict__,{'player_id': 10, 'move': [], 'result': 'win'})

    
if __name__ == '__main__':
    unittest.main()                           