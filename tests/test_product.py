import unittest
from app.models import Product,User
from app import db



class ProductTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the  class
    '''
          
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_ = User(username = 'leta',password = 'banana', email = 'leta@ms.com')
          
        self.new_product = Product(product_name='vegan pizza',description="food for vegans",user = self.user_Stan)
   
    def tearDown(self):
        Product.query.delete()
        User.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_product, Product))
  
    
    # We then check if the values of variables are correctly being placed.
    def test_check_instance_variables(self):
        
        self.assertEquals(self.new_product.product_name,'vegan pizza')
        self.assertEquals(self.new_product.description,"food for vegans")
        self.assertEquals(self.new_product.user,self.user_Stan)
       
    def test_save_product(self):
        self.new_product.save_product()
        self.assertTrue(len(Product.query.all())>0)
        