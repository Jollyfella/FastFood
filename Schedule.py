import numpy as np
import pandas as pd
import datetime

seq_list = []

def orders(param1):
    """This Function creates a schelduled list of timestamps based on orders placed"""
    now = 0
    total = 90
    lst = ['{:%H:%M:%S}'.format(datetime.datetime.now()+datetime.timedelta(seconds =now)), str(param1) + " sandwich orders placed"]
    seq_list.append(lst)
    i=1
    while i < param1+1:
        make=(i*total)-total
        seq_list.append(['{:%H:%M:%S}'.format(datetime.datetime.now()+datetime.timedelta(seconds =make)), 'make sandwich ' +str(i)])
        serve = (i*total)-30
        seq_list.append(['{:%H:%M:%S}'.format(datetime.datetime.now()+datetime.timedelta(seconds =serve)), 'serve sandwich ' +str(i)])
        i=i+1
    rest = ((param1+1)*total)-total
    seq_list.append(['{:%H:%M:%S}'.format(datetime.datetime.now()+datetime.timedelta(seconds =rest)), 'take a well earned break!'])
    
seq_matrix = np.array(seq_list)
cols = ['time', 'task']
df = pd.DataFrame(data=seq_matrix, columns=cols)


