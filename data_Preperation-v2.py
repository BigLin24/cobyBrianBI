#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(data)
dropped = data.dropna(subset=['shot_made_flag'])

dropped.to_csv('testfileDropped.csv')
dropped['remaining_time'] = dropped['minutes_remaining'] * 60 + dropped['seconds_remaining']
dropped['dist'] = np.sqrt(dropped['loc_x']**2 + dropped['loc_y']**2)


dropped.to_csv('testfileTiming.csv')