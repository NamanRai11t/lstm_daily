import time
import warnings
import numpy as np
from numpy import newaxis
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import matplotlib.pyplot as plt


#warnings.filterwarnings("ignore")

def load_data(obj_set, seq_len, normalise_window):
    data = []
    for obj in obj_set:
        data.append(float(getattr(obj,"value")))

    sequence_length = seq_len + 1
    result = []
    for index in range(len(data) - sequence_length):
        result.append(data[index: index + sequence_length])

    normalising_factor = np.array(result)[-1,0]
    
    if normalise_window:
        result = normalise_windows(result)

    result = np.array(result)

    train = result

    x_test = train[-2:, 1:]
    
    train = train[:-2]
    np.random.shuffle(train)
    x_train = train[:result.shape[0]-1, :-1]
    y_train = train[:result.shape[0]-1, -1]
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))  

    return [x_train, y_train, x_test, normalising_factor]

def normalise_windows(window_data):
    normalised_data = []
    for window in window_data:
        normalised_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalised_data.append(normalised_window)
    return normalised_data

def build_model(layers):
    model = Sequential()

    model.add(LSTM(
        input_dim=layers[0],
        output_dim=layers[1],
        return_sequences=True))
    model.add(Dropout(0.2))

    model.add(LSTM(
        layers[2],
        return_sequences=False))
    model.add(Dropout(0.2))

    model.add(Dense(
        output_dim=layers[3]))
    model.add(Activation("linear"))

    start = time.time()
    model.compile(loss="mse", optimizer="rmsprop")
    return model

def predict_point_by_point(model, data):
    #Predict each timestep given the last sequence of true data, in effect only predicting 1 step ahead each time
    predicted = model.predict(data)
    predicted = np.reshape(predicted, (predicted.size,))
    return predicted

def predict_for_view(obj_set):
    X_train, y_train, X_test, normalising_factor = load_data(obj_set,50, True)
    model = build_model([1,50,100,1])
    model.fit(X_train,
        y_train,
        batch_size=512,
        nb_epoch=1,
        validation_split=0.05)
    predicted_results = model.predict(X_test)
    next_day = ((list(predicted_results[1])[0])+1)*normalising_factor
    fifty_day = list((np.reshape(X_test[1], (50,)) + 1) * normalising_factor)
    return (next_day, fifty_day)
