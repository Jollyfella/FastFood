import unittest
import Schedule

# capture results of funtion
# check fot expected output

class Test_Schedule(unittest.TestCase):
   
    def setUp(self):
        self.orders = 3
        #self.seq_list = ['rrer','rerer']
        self.seq_list = Schedule.orders(3)
        #self.time_format = '{:%H:%M:%S}'.format(datetime.datetime())
        self.seq_matrix = [['00:00:00' 'orders placed']]
        #self.df = pd.DataFrame(data=self.seq_matrix,)
        
    def test_orders(self):
        self.assertIsInstance(self.orders, int, msg='orders should be an int dtype')
        self.assertNotEqual(self.orders, 0, msg='number of orders placed should be greater than zero')
        self.assertIsInstance(self.seq_list, list, msg='output of orders function should be a list')
        #self.assertIsInstance(Schedule.orders(), list, msg='result of orders function is a list')
        #self.assertIsInstance(self.seq_list, datetime)
        #self.assertIsInstance(self.seq_list(0,0) is datetime)     
        #trou   self.assertTrue(self.seq_matrix, [['{:%H:%M:%S}','orders placed']])
        
    def test_output_schedule_type(self):
        # test list
        self.assertTrue(type(self.seq_list) is list)
        # test matrix
        # trou  self.assertTrue(self.seq_matrix,'<U25')
        # test df
        #self.assertTrue(types(self.df) is object)
        
if __name__ == '__main__':
    unittest.main()
#argv=['first-arg-is-ignored'], exit=False
