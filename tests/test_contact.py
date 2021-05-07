import unittest
from app.models import User


class TestUser(unittest.TestCase):

def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = Phone("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        found_contact = Phone.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.emai