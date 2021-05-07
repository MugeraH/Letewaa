import unittest
from app.models import Product,User,Orders
from app import db



class OrdersTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the  class
    '''
          
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_ = User(username = 'leta',password = 'banana', email = 'leta@ms.com')
          
        self.new_orders = Orders(pizza_name='vegan pizza',pizza_size="large",price="1000",user = self.user_Stan)
   
    def tearDown(self):
        Orders.query.delete()
        User.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_orders, Orders))
  
    
    # We then check if the values of variables are correctly being placed.
    def test_check_instance_variables(self):
        
        self.assertEquals(self.new_orders.pizza_name,'vegan pizza')
        self.assertEquals(self.new_orders.pizza_size,'large')
        self.assertEquals(self.new_orders.price,'1000')
        self.assertEquals(self.new_pitch.user,self.user_Stan)
       
    def test_save_product(self):
        self.new_orders.save_orders()
        self.assertTrue(len(Orders.query.all())>0)
        