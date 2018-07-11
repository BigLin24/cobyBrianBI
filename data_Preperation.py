import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline



from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold

# Laden die Daten ein und erstellen einen Übersicht der Daten
data = pd.read_csv('data.csv')
print(data.shape)
print(data.head())
data.describe()# in dieser Schritt finden wir ,dass die missing Value in der Spalte shot_made_flag.

 
#Teilen die Daten in training data und test data ein
import numpy as np
data = pd.read_csv('data.csv')
train_kobe=data[pd.notnull(data['shot_made_flag'])]
test_kobe=data[pd.isnull(data['shot_made_flag'])]
test_kobe=test_kobe.drop('shot_made_flag',1)
print(train_kobe.shape)
print(test_kobe.shape)

#DATA PREPARATION

nona =  data[pd.notnull(data['shot_made_flag'])]
#We want to prepare the data. In order to do that we look for integer that belong to 
#the category "Place" and we will normalize them.

#We want to understand what the variables loc_x, loc_y, lat and lon mean, so we perform 
#the following code, to get confirmed that they represent location_x, location_y, latitude and longitude:
alpha = 0.02
plt.figure(figsize=(10,10))

# loc_x and loc_y
plt.subplot(121)
plt.scatter(nona.loc_x, nona.loc_y, color='red', alpha=alpha)
plt.title('loc_x and loc_y')

# lat and lon
plt.subplot(122)
plt.scatter(nona.lon, nona.lat, color='orange', alpha=alpha)
plt.title('lat and lon') 
#So, when perform the plot, we see that these plots are shaped like basketball courts. 
#So loc_x, loc_y, lat and lon are the position from which the ball was tossed. 
#However, since the region under the net is half-circle-shaped, 
#it would be more suitable to transform the variable into polar coodinates. In the end, we
#we'll not need lat and lon anymore. See drop function below later).To do such we give 
#the program following commands:
data['dist'] = np.sqrt(data['loc_x']**2 + data['loc_y']**2)

loc_x_zero = data['loc_x'] == 0
data['angle'] = np.array([0]*len(data))
data['angle'][~loc_x_zero] = np.arctan(data['loc_y'][~loc_x_zero] / data['loc_x'][~loc_x_zero])
data['angle'][loc_x_zero] = np.pi / 2  #Since some of loc_x values cause an error by 
#zero-division, we set just np.pi / 2 to the corresponding rows.

#We now normalize the time and merge together remaining minutes and seconds:
data['remaining_time'] = data['minutes_remaining'] * 60 + data['seconds_remaining']

#•	Always in order to normalize the data, we now need to transform the categorial 
#values into ordinal ones. This regards following variables: action_type, 
#combined_shot_type, shot_type, which represent how Kobe Bryant shot the ball.
print(nona.action_type.unique())
print(nona.combined_shot_type.unique())
print(nona.shot_type.unique())

#We analyze Season:
nona['season'].unique()
# Season consists of ID and year, and we decided that only ID can be useful for us, therefore:
data['season'] = data['season'].apply(lambda x: int(x.split('-')[1]) )
data['season'].unique()

#We now delete all unnecessary variables:
drops = ['shot_id', 'team_id', 'team_name', 'shot_zone_area', 'shot_zone_range', 'shot_zone_basic', \
         'matchup', 'lon', 'lat', 'seconds_remaining', 'minutes_remaining', \
         'shot_distance', 'loc_x', 'loc_y', 'game_event_id', 'game_id', 'game_date']
for drop in drops:
    data = data.drop(drop, 1)

