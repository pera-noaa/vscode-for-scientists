import os
import sys
from typing import   Dict,  List, Optional
import numpy as np
from   collections import OrderedDict
import pandas



def get_data(path:str)->Dict :
    """Load data from path."""
    if path == None:
        return {}

    data    =   pandas.read_csv(  path  )
    flags = np.zeros( len(data),  dtype=np.bool   )
    counts =     np.array(data['count'].values  , dtype=np.int  )



    result   =   {}
    for i,row in   data.iterrows( ):
        result [ i ] =row.to_dict()
    return result


def      summarize(values:List[float])  ->  Optional[float]:
    if len(values)==0:return None
    return sum(values) /len(values)


def make_old_dict():
    od = OrderedDict()
    od['a']=1
    od['b']=2
    return od


if __name__=='__main__':
    print(  "hello"  )
