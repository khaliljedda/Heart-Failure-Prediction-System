# Importing libraries
import numpy as np
import pandas as pd 

# Importing the dataset
dataset = pd.read_csv('heart.csv') 
X = dataset.iloc[:, 0:11 ].values
Y = dataset.iloc[:, 11].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X1 = LabelEncoder()
X[:, 1] = labelencoder_X1.fit_transform(X[:, 1])
labelencoder_X2 = LabelEncoder()
X[:, 2] = labelencoder_X2.fit_transform(X[:, 2])
labelencoder_X6 = LabelEncoder()
X[:, 6] = labelencoder_X6.fit_transform(X[:, 6])
labelencoder_X8 = LabelEncoder()
X[:, 8] = labelencoder_X2.fit_transform(X[:, 8])
labelencoder_X10 = LabelEncoder()
X[:, 10] = labelencoder_X10.fit_transform(X[:, 10])

#Transforming the encoded data to separate columns 

#Encoding the ChestPainType to 4 separate columns
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [2])],     remainder='passthrough')
X=np.array(columnTransformer.fit_transform(X))

#Encoding the RestingECG  to 3 separate columns

columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [9])],     remainder='passthrough')
X=np.array(columnTransformer.fit_transform(X))

#Encoding the ST_Slope to 3 separate columns 

columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [15])],     remainder='passthrough')
X=np.array(columnTransformer.fit_transform(X))

#Preventing the dummy varible trap 
X= np.delete(X, [2,5,9], 1)
X_test = X[800:918,:]
X=X[0:800,:]
Y_test = Y[800:918]
Y=Y[0:800]


# Feature Scaling (Normalisation des donnes)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
X_test = sc.transform(X_test)



# MLP for  Dataset with 10-fold cross validation
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import StratifiedKFold
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# define 10-fold cross validation test harness
kfold = StratifiedKFold(n_splits=10, shuffle=False)
cvscores = []
for train, test in kfold.split(X, Y):
  # create model
	model = Sequential()
	model.add(Dense(8, input_dim=15, activation='relu'))
	model.add(Dense(8, activation='relu'))
	model.add(Dense(1, activation='sigmoid'))
	# Compile model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy' , 'mse'])
	# Fit the model
	model.fit(X[train], Y[train], epochs=150, batch_size=10, verbose=0)
	# evaluate the model
	scores = model.evaluate(X[test], Y[test], verbose=0)
	print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	cvscores.append(scores[1] * 100)

history = model.fit(X, Y, epochs=150, batch_size=10)


# - Making the predictions and evaluating the model
y_pourcentage = model.predict(X_test)
y_pred=(y_pourcentage>0.5)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(Y_test, y_pred)

imported=X[0:1,:]

#save the model to disk
import joblib
filename = 'finalized_model.sav'
joblib.dump(model, filename)
joblib.dump(sc, 'normalisation.sav')



# from matplotlib import pyplot
# pyplot.plot(history.history['accuracy'])
# pyplot.show()





