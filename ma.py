# -*- coding: utf-8 -*-
from scipy.ndimage import imread
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

import json
from pprint import pprint

filename_list = ("data/1996637038" , "data/1996636977"
    , "data/1996637042"
    , "data/1996636959"
    , "data/1996637065"
    , "data/1996637119"
    , "data/1996637118"
    , "data/1996637064"
    , "data/1996636979"
    , "data/1996637092"
    , "data/1996637132"
    , "data/1996637085"
    , "data/1996636989"
    , "data/1996637080"
    , "data/1996637144"
    , "data/1996637066"
    , "data/1996637082"
    , "data/1996637088"
    , "data/1996637068"
    , "data/1996637044"
    , "data/1996637026"
    , "data/1996637058"
    , "data/1996637019"
    , "data/1996637002"
    , "data/1996637099"
    , "data/1996637075"
    , "data/1996637003"
    , "data/1996637142"
    , "data/1996637155"
    , "data/1996637069"
    , "data/1996637063"
    , "data/1996637097"
    , "data/1996636990"
    , "data/1996636976"
    , "data/1996637129"
    , "data/1996637040"
    , "data/1996636960"
    , "data/1996637138"
    , "data/1996637007"
    , "data/1996636973"
    , "data/1996637077"
    , "data/1996637094"
    , "data/1996637098"
    , "data/1996637121"
    , "data/1996637012"
    , "data/1996636978"
    , "data/1996637024"
    , "data/1996636991"
    , "data/1996637021"
    , "data/1996637045"
    , "data/1996637095"
    , "data/1996637122", )


def load_df(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
        return pd.DataFrame(data['response']['indices'][0]['values'],
                              index=pd.to_datetime(data['response']['indices'][0]['dates'], unit='s'),
                              columns=[data['response']['indices'][0]['place']])

result_df = pd.concat((load_df(filename) for filename in filename_list), axis=1)
result_df = result_df.div(result_df.iloc[-1], axis=1)
result_df.plot(logy=True)
plt.tight_layout()
plt.show()
