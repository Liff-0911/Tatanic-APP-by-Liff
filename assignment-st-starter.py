# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# show the title
st.title('Titanic APP by Liff')

# read csv and show the dataframe
df = pd.read_csv('train.csv')

# create a figure with three subplots, size should be (15, 5)
fig, ax = plt.subplots(1,3,figsize = (15,5))
df[df.Pclass == 1].Fare.plot.box(ax = ax[0]).set_xlabel('Pclass=1')
df[df.Pclass == 2].Fare.plot.box(ax = ax[1]).set_xlabel('Pclass=2')
df[df.Pclass == 3].Fare.plot.box(ax = ax[2]).set_xlabel('Pclass=3')
# show the box plot for ticket price with different classes
(df.groupby(by=[df.Pclass,df.Survived]).Survived.value_counts()/df.Pclass.value_counts()).plot.bar(figsize = (5,3))
# you need to set the x labels and y labels
# a sample diagram is shown below

