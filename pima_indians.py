import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import os

datafile = "pima-indians-diabetes.csv"

#check for dataset.
if not os.path.exists(datafile):
    raise FileNotFoundError(datafile + " not found in currdir" )

dataset = np.loadtxt("pima-indians-diabetes.csv",delimiter=",")
X = dataset[:,0:8]
y = dataset[:,8]

# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
trials = 10
n_epochs = 150
batch_size = 10

# fit the keras model on the dataset
model.fit(X, y, epochs=n_epochs, batch_size=batch_size,verbose=True)

# evaluate the keras model
_, accuracy = model.evaluate(X, y,verbose=True)

# make class predictions with the model
predictions = model.predict_classes(X)

# summarize the first 5 cases
for i in range(5):
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     pass
