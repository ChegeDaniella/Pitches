import unittest
from app.main.models import Pitches
from app import db

class PitchesModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch=Pitches(pitch='new',comment='I love darkness', category='sports',user_id = 123)

    def tearDown(self):
        Pitches.query.delete()

    def test __init__(self):
        self.assertEquals(self.new_pitch.pitch,'new')    
        self.assertEquals(self.new_pitch.comment,'I love darkness') 
        self.assertEquals(self.new_pitch.category='sports') 
        self.assertEquals(self.new_pitch.user_id, 123) 
       

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitches.query.all())>0)   

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch
        got_pitch = Pitches.get_pitch(12345)
        self.assertTrue(len(got_pitch) == 1)     

                 
