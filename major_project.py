import pandas as pd
data=pd.read_excel('Data_Train.xlsx')
data.head(10)

#removing null values
data.dropna(inplace=True)
data=data[data['Power']!='null bhp']

#Removing unnecessary columns and making necessary changes
s=['Wagon R','Range Rover','Land Rover','Corolla Altis','Indica Vista','Innova Crysta','Pajero Sport','Ssangyong Rexton','Vitara Brezza','Zest Revotron','Santo Xing','B Class','Cooper Convertible','Coutryman Cooper','Grand ilo','Grand Punto']
t=['Wagon_R','Range_Rover','Land_Rover','Corolla_Altis','Indica_Vista','Innova_Crysta','Pajero_Sport','Ssangyong_Rexton','Vitara_Brezza','Zest_Revotron','Santo_Xing','B_Class','Cooper_Convertible','Coutryman_Cooper','Grand_ilo','Grand_Punto']
data['Name']=data['Name'].replace(s,t,regex=True)
new=data['Name'].str.split(' ',n=3,expand=True)
data['Company']=new[0]
data.drop(['Name'],axis=1,inplace=True)
data['Age']=2020-data['Year']
data.drop(['Year'],axis=1,inplace=True)

#Removing units from the columns
new=data['Mileage'].str.split(' ',expand=True)
data['Mileage']=new[0]
new=data['Engine'].str.split(' ',expand=True)
data['Engine']=new[0]
new=data['Power'].str.split(' ',expand=True)
data['Power']=new[0]
data[['Mileage','Engine','Power']]=data[['Mileage','Engine','Power']].apply(pd.to_numeric)
