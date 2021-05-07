import  unittest
from app.models import User

class TestUser(unittest.TestCase):

    # Ensure user can register
    def test_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='Michael', email='michael@realpython.com',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Welcome to Letewaa!', response.data)
            self.assertTrue(current_user.name == "Michael")
            self.assertTrue(current_user.is_active())
            user = User.query.filter_by(email='michael@realpython.com').first()
            self.assertTrue(str(user) == '<name - Michael>')