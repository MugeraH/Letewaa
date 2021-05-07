import unittest
from app.models import Seller

class SellerModelTest(unittest.TestCase):

    def setUp(self):
        self.new_seller=Seller(password='banana')

    def test_password_setter(self):
        self.assertTrue(self.new_seller.password is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_seller.password

        def test_password_verification(self):
            self.assertTrue(self.new_seller.verify_password('banana'))