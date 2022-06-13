import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv

#dice_result = []
#counter = []
#for i in range(0,100):
#    dice1 = random.randint(1,6)
#    dice2 = random.randint(1,6)
#    dice_result.append(dice1 + dice2)
#   counter.append(i)
#print(dice_result)

df = pd.read_csv("smartphone_data.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Rating"], show_hist =  False)
fig.show()
