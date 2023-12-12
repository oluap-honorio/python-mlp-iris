import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
#
# Import Keras modules
#
from keras import models
from keras import layers
from keras.utils import to_categorical

class IrisMLP:
    
    def __init__(self):
        self.network = models.Sequential()
        self.test_loss = None
        self.test_acc = None 

    def training(self):
        #
        # Create the network
        #
        
        self.network.add(layers.Dense(512, activation='relu', input_shape=(4,)))
        self.network.add(layers.Dense(3, activation='softmax'))
        #
        # Compile the network
        #
        self.network.compile(optimizer='rmsprop',
                        loss='categorical_crossentropy',
                        metrics=['accuracy'])
        #
        # Load the iris dataset
        #
        iris = datasets.load_iris()
        X = iris.data
        y = iris.target
        #
        # Create training and test split
        #
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
        #
        # Create categorical labels
        #
        train_labels = to_categorical(y_train)
        test_labels = to_categorical(y_test)
        #
        # Fit the neural network
        #
        self.network.fit(X_train, train_labels, epochs=20, batch_size=40)

        #
        # Get the accuracy of test data set
        #
        self.test_loss, self.test_acc = self.network.evaluate(X_test, test_labels)
           
    def getMetrica(self):
        return self.test_acc