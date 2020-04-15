import pandas as pd
import numpy as np

#for graphing purposes
import seaborn as sns
import matplotlib.pyplot as plt

bd=pd.read_csv('Data_Train (2).csv')
bd

#Editing the column variable "Name" to fill in the spaces between words of a same name
s=['Wagon R','Range Rover','Land Rover','Corolla Altis','Indica Vista','Innova Crysta','Pajero Sport','Ssangyong Rexton','Vitara Brezza','Zest Revotron','Santo Xing','B Class','Cooper Convertible','Coutryman Cooper','Grand ilo','Grand Punto']
t=['Wagon_R','Range_Rover','Land_Rover','Corolla_Altis','Indica_Vista','Innova_Crysta','Pajero_Sport','Ssangyong_Rexton','Vitara_Brezza','Zest_Revotron','Santo_Xing','B_Class','Cooper_Convertible','Coutryman_Cooper','Grand_ilo','Grand_Punto']
bd['Name']=bd['Name'].replace(s,t,regex=True)

#code to divide the 'Name' column to 3 different columns 'Namen', 'Model', and 'Version'
import warnings
warnings.filterwarnings('ignore')
bd['Namen']=""
bd['Model']=""
bd['Version']=""
import re
pat=re.compile(' ')
for i in range(len(bd['Name'])):
    res=re.split(pat,bd['Name'].iloc[i])
    bd['Namen'].iloc[i]=res[0]
    bd['Model'].iloc[i]=res[1]
    bd['Version'].iloc[i]=res[2:]

#code to convert and join the the list of elements in the column 'Version' to an object with a space(' ') in between the words
for _ in range(len(bd.Version)):
    jv=' '
    temp=jv.join(bd.Version[_])
    bd.Version[_]=temp
print(bd.Version[0])      
        
#code to remove the column 'Name' and renaming the column 'Namen' as 'Name'
bd=bd.drop(columns='Name')
bd=bd.rename(columns={"Namen": "Name"})

#code to replace the null values in the column 'Seats' with the values from other rows that have the same 'Model' and 'version'
nu=list()
for k in range(len(bd['Seats'])):
    if(bd['Seats'].isnull().iloc[k]==True):
        nu.append(k) 
        
bd['Seats']=bd['Seats'].fillna('null')      

for i in nu:
    for j in range(len(bd)):
        if((bd['Model'][j]==bd['Model'][i])&(bd['Version'][j]==bd['Version'][i])&(bd['Seats'][j]!='null')):
            bd['Seats'][i]=bd['Seats'][j]
        
for k in nu:
    if(bd['Seats'][k]=='null'):
         bd['Seats'].iloc[k]=float('nan')         
        
        
#removing all the rows that have any of the values as null
bd=bd.dropna(how='any')

#removed columns "Mileage", "Engine", "Power"
bd = bd.drop(["Mileage", "Engine", "Power"], axis = 1)

#cleaning up the owner data
bd["Owner_Type"] = bd["Owner_Type"].str.replace("First", "1")
bd["Owner_Type"] = bd["Owner_Type"].str.replace("Second", "2")
bd["Owner_Type"] = bd["Owner_Type"].str.replace("Third", "3")
bd["Owner_Type"] = bd["Owner_Type"].str.replace("Fourth & Above", "4")

#performing univariate analysis on the owner data
#basically we're just plotting a graph here
print("Number of cars sold according to type of owner: ")
owner_graph = sns.countplot(x = "Owner_Type", data = bd)

#similarly perform univariate analysis on the location data
loc_graph = sns.countplot(x = "Location", data = bd)
