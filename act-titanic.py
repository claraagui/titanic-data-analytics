import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

st.title('Titanic')

df=pd.read_csv("train.csv")
st.dataframe(df)

st.title('Hallazgos de Titanic: ')
st.markdown('Podemos ver que existen valores nulos en tres  columnas que son: Age (177), Cabin(687) y Embarked (2).')

arr = df['Survived']
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)
st.markdown('Survived tiene dos categorias, que son 0 y 1, supuse que 1 son las personas que sobrevivieron y 0 las que no sobrevivieron. Hubo más personas que murieron en el titanic.')

st.dataframe(df['Pclass'].unique())

#Primer clase

st.title('Primera clase')
dffirstclass = df[df['Pclass']==1]
st.dataframe(dffirstclass)

arr=dffirstclass['Survived']
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)
st.markdown('SObrevivieron más de los que murieron')

st.header('Analizando la columna Age:')
fig,ax = plt.subplots()
ax.hist(x=dffirstclass['Age'].values, color='red')
st.pyplot(fig)
st.markdown('En el rango de 19 a 55 años fueron los que aproximadamente pudieron comprar un botelo de primer clase siendo las personas de entre 35 y 40 que más compraron.')

st.header('Analizando la columna sex:')
fig, ax= plt.subplots()
sextitanic=dffirstclass['Sex'].value_counts()
labelsex=sextitanic.index.to_list()
sextitanic.values
ax.pie(sextitanic.values,labels=labelsex, autopct='%1.1f%%', colors=['skyblue','blue'])
st.pyplot(fig)
st.markdown('Nos dimos cuenta que los hombres predominaron.')

st.header('Analizando la columna Embarked:')
dffirstclass['Embarked'].fillna('S',inplace=True)
fig,ax = plt.subplots()
ax.hist(x=dffirstclass['Embarked'], color='skyblue')
st.pyplot(fig)
st.markdown('Donde más abordaron fueron en Southampton primera clase también hubo varias personas que se subieron al barco en Cherbourg.')

#Segunda Clase
st.title('Segunda Clase')
dfsecondclass = df[df['Pclass']==2]
st.dataframe(dfsecondclass)

arr=dfsecondclass['Survived']
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)
st.markdown('De la segunda clase murieron más de los que sobrevivieron, pero la diferencia es un poco reducida.')

st.header('Analizando la columna Age:')
fig,ax = plt.subplots()
ax.hist(x=dfsecondclass['Age'].values, color='lavender')
st.pyplot(fig)
st.markdown('Me di cuenta que las personas en un rango de entre 22 y 35 años fueron las que más compraron esta clase.')

st.header('Analizando la columna sex:')
fig, ax= plt.subplots()
sextitanic=dfsecondclass['Sex'].value_counts()
labelsex=sextitanic.index.to_list()
sextitanic.values
ax.pie(sextitanic.values,labels=labelsex, autopct='%1.1f%%', colors=['teal','skyblue'])
st.pyplot(fig)
st.markdown('Nos dimos cuenta que los hombres predominaron.')

st.header('Analizando la columna Embarked:')
dfsecondclass['Embarked'].fillna('S',inplace=True)
fig,ax = plt.subplots()
ax.hist(x=dfsecondclass['Embarked'], color='skyblue')
st.pyplot(fig)
st.markdown('Donde más abordaron fueron en Southampton.')

#Tercer Clase
st.title('Tercera Clase')
dfthirdclass = df[df['Pclass']==3]
st.dataframe(dfthirdclass)

arr=dfthirdclass['Survived']
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)
st.markdown('En la tercer clase fue en la que más personas murieron que sobrevivieron.')

st.header('Analizando la columna Age:')
fig,ax = plt.subplots()
ax.hist(x=dfthirdclass['Age'].values, color='red')
st.pyplot(fig)
st.markdown('Me di cuenta que las peronas entre los 19 y los 30 años tuvieron más compra a estos boletos, teniendo más valor entre los 19 y 22 años.')

st.header('Analizando la columna sex:')
fig, ax= plt.subplots()
sextitanic=dfthirdclass['Sex'].value_counts()
labelsex=sextitanic.index.to_list()
sextitanic.values
ax.pie(sextitanic.values,labels=labelsex, autopct='%1.1f%%', colors=['teal','skyblue'])
st.pyplot(fig)
st.markdown('Nos dimos cuenta que los hombres predominaron.')

st.header('Analizando la columna Embarked:')
dfthirdclass['Embarked'].fillna('S',inplace=True)
fig,ax = plt.subplots()
ax.hist(x=dfthirdclass['Embarked'].values, color='skyblue')
st.pyplot(fig)
st.markdown('Donde más abordaron fueron en Southampton.')