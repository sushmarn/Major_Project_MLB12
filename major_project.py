import pandas as pd
data=pd.read_excel('Data_Train.xlsx')
test_data=pd.read_excel('Data_Test.xlsx')

#CLEANING THE TRAIN DATA
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


#CLEANING THE TEST DATA
#removing null values
test_data.dropna(inplace=True)
test_data=test_data[test_data['Power']!='null bhp']

#Removing unnecessary columns and making necessary changes
s=['Wagon R','Range Rover','Land Rover','Corolla Altis','Indica Vista','Innova Crysta','Pajero Sport','Ssangyong Rexton','Vitara Brezza','Zest Revotron','Santo Xing','B Class','Cooper Convertible','Coutryman Cooper','Grand ilo','Grand Punto']
t=['Wagon_R','Range_Rover','Land_Rover','Corolla_Altis','Indica_Vista','Innova_Crysta','Pajero_Sport','Ssangyong_Rexton','Vitara_Brezza','Zest_Revotron','Santo_Xing','B_Class','Cooper_Convertible','Coutryman_Cooper','Grand_ilo','Grand_Punto']
test_data['Name']=test_data['Name'].replace(s,t,regex=True)
new=test_data['Name'].str.split(' ',n=3,expand=True)
test_data['Company']=new[0]
test_data.drop(['Name'],axis=1,inplace=True)
test_data['Age']=2020-test_data['Year']
test_data.drop(['Year'],axis=1,inplace=True)

#Removing units from the columns
new=test_data['Mileage'].str.split(' ',expand=True)
test_data['Mileage']=new[0]
new=test_data['Engine'].str.split(' ',expand=True)
test_data['Engine']=new[0]
new=test_data['Power'].str.split(' ',expand=True)
test_data['Power']=new[0]
test_data[['Mileage','Engine','Power']]=test_data[['Mileage','Engine','Power']].apply(pd.to_numeric)

#ANALYSIS OF TEST DATA
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.regplot('Engine','Price',data=data)
sns.regplot('Mileage','Price',data=data)
sns.regplot('Power','Price',data=data)
sns.regplot('Kilometers_Driven','Price',data=data)

#removing the Kilometers_Driven column as the analysis shows there is no correlation between it and the Price
data.drop(['Kilometers_Driven'],axis=1,inplace=True)
test_data.drop(['Kilometers_Driven'],axis=1,inplace=True)

#OneHotEncoding the categorical columns
data=pd.get_dummies(data, columns=['Fuel_Type','Transmission','Owner_Type','Company','Location'],prefix_sep='_')
test_data=pd.get_dummies(test_data, columns=['Fuel_Type','Transmission','Owner_Type','Company','Location'],prefix_sep='_')

#Removing outliers in the train data using Z-Score
from scipy import stats
import numpy as np
z = np.abs(stats.zscore(data))
data=data[(z < 3).all(axis=1)]

#Making necessary changes to columns in test data as columns change after OneHotEncoding
for i in test_data.columns.tolist():
    if i not in data.columns.tolist():
        test_data.drop(i,axis=1,inplace=True)

for i in data.columns.tolist():
    if i not in test_data.columns.tolist() and i!='Price':
        test_data[i]=0

#Checking the accuracy of our model by splitting the train data as we have no price column in the test data
#Note: This is just for checking accuracy
X=data.loc[:,data.columns!='Price']
y=data.loc[:,data.columns=='Price']
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#Fitting the model
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(X_train, np.ravel(y_train))
#Predictions and accuracy of the model
pred=rf.predict(X_test)
errors = abs(pred-np.ravel(y_test))
mape = 100 * (errors / np.ravel(y_test))
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')


#Fitting the whole train data to predict price from the given test data
X_train=data.loc[:,data.columns!='Price']
y_train=data.loc[:,data.columns=='Price']
X_test=test_data.loc[:,:]
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(X_train, np.ravel(y_train))
#Prediction
pred=rf.predict(X_test)
print(pred)

