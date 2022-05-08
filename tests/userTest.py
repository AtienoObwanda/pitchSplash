import unittest

from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='mish',email='mishie@gmail.com',password='new123')