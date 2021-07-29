import json
import numpy as np
import seaborn as sns
from datetime import datetime
import glob
import pandas as pd



df = pd.read_pickle('Data/RachelRomano')


class Texter:

	def __init__(self, name, df):
		self.name = name
		self.df = df

	def get_num_text(self):
		num_texts = sum(self.df['sender_name']==self.name)
		return num_texts

	def get_avg_len(self):
		
		pass




dk = Texter('Daniel Kraft', df)
rr = Texter('Rachel Romano', df)

print(dk.df['content'].str.encode("utf-8"))

print(dk.get_num_text())
print(rr.get_num_text())





