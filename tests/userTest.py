import unittest
from app.models import User,Comments, Pitches

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = 'barida')
    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('barida'))

class CommentsModelTest(unittest.TestCase):
    def setUp(self):
       self.new_comment = Comments(id=1, user_id = 3, comment = 'awesome',pitches_id = '10',date_posted='2022-05-08')
    def test_comment_variables(self):
       self.assertEquals(self.new_comment.comment,'awesome')
       self.assertEquals(self.new_comment.date_posted,'2022-05-08')
       self.assertEquals(self.new_comment.user_id, 3)
    def test_save_comment(self):
        self.assertTrue(len(Comments.query.all())>0)
        
class PitchesModelTest(unittest.TestCase):
    def test_save_pitch(self):
        self.assertTrue(len(Pitches.query.all())>0)