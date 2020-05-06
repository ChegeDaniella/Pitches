import unittest
from app.main.models import Comments
from app import db

class CommentsModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comments=Comments( comment_content='new',pitches_id ='I love darkness',user_id = 123)

    def tearDown(self):
        Comments.query.delete() 

    def test __init__(self):
        self.assertEquals(self.new_comments.comment_content,'new')    
        self.assertEquals(self.new_comments.pitches_id,'I love darkness',) 
        self.assertEquals(self.new_comments.user_id, 123)     

    # def test_save_pitch(self):
    #     self.new_pitch.save_pitch()
    #     self.assertTrue(len(Pitches.query.all())>0)   
               
