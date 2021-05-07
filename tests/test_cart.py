import unittest
from app.models import Product,User,Cart
from app import db



class CartTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the  class
    '''
          
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_ = User(username = 'leta',password = 'banana', email = 'leta@ms.com')
          
        self.new_cart = Cart(product='vegan pizza',size="large",user = self.user_Stan,amount="1000")
   
    def tearDown(self):
        Cart.query.delete()
        User.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_cart, Cart))
  
    
    # We then check if the values of variables are correctly being placed.
    def test_check_instance_variables(self):
        
        self.assertEquals(self.new_cart.product,'vegan pizza')
        self.assertEquals(self.new_cart.price,"food for vegans")
        self.assertEquals(self.new_cart.size,"large")
        self.assertEquals(self.new_cart.amount,"1000")
        self.assertEquals(self.new_cart.user,self.user_Stan)
        
    def test_save_product(self):
        self.new_cart.save_cart()
        self.assertTrue(len(Cart.query.all())>0)
        