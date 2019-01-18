# Fast Food Schedule

# By Richard Martin
# 14th July 2018

#standard python stuff
import numpy as np
import pandas as pd
import datetime
import sys

def orders(param1):
    """
    This Function creates a schelduled list of timestamps based on orders placed
    """
    #create a blank list
    seq_list = []
    #convert param1 argument to int from str
    param1 = int(param1)
    if param1 > 0:
        # define time deltas for timestamps
        now = 0
        total = 90
        #create 1st row in schedule indicating order was placed
        lst = ['{:%H:%M:%S}'.format(datetime.datetime.now()+datetime.timedelta(seconds =now)), str(param1) + " sandwich orders placed"]
        seq_list.append(lst)
        i=1
        while i < param1+1:
            # create "make" rows  
            make=(i*total)-total
            seq_list.append(['{:%H:%M:%S}'.format(datetime.datetime.now()+datetime.timedelta(seconds =make)), 'make sandwich ' +str(i)])
            # create "serve" rows
            serve = (i*total)-30
            seq_list.append(['{:%H:%M:%S}'.format(datetime.datetime.now()+datetime.timedelta(seconds =serve)), 'serve sandwich ' +str(i)])
            i=i+1
        # create the "rest" row
        rest = ((param1+1)*total)-total
        seq_list.append(['{:%H:%M:%S}'.format(datetime.datetime.now()+datetime.timedelta(seconds =rest)), 'take a well earned break!'])
        # create 2D numpy array from list
        seq_matrix = np.array(seq_list)
        # define column indexes of dataframe
        cols = ['time', 'task']
        df = pd.DataFrame(data=seq_matrix, columns=cols)
        return df
    else:
        # print statement if argument param1 is less than 1
        print('Number of orders should be grater then zero!')
    
def output_schedule(output):
    """
    This Function prints the fast food schedule dataframe from orders function
    """
    print(output)

if __name__ == '__main__':
    param1 = sys.argv[1]
    output_schedule(orders(param1))