import pandas as pd
import numpy as np
import json
from pandas import DataFrame as DF
import glob

def jsons_to_df(dir):
  json_files = glob.glob(dir+'/message_*.json')
  print(json_files)

  df_list = []

  for file_name in json_files:
    with open(file_name) as f:
       data = json.load(f)
       data_mess = data['messages']
       df_mini = pd.DataFrame(data_mess)
       df_list.append(df_mini)

  df = pd.concat(df_list)

  return df


#df = jsons_to_df('Data/facebook-danielkraft104/messages/inbox/rachelromano_wu7vlys6yg')
#df.to_pickle('Data/RachelRomano')

# You could pretty easily turn this into a function where you enter a name and it returns the dataframe

def get_dataframe(name):
  name = name.replace(" ","").lower()
  return(name)

print(get_dataframe('Daniel Kraft'))
