import pandas as panda
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from .models import Weather

# cele trei locatii alese
first_location = (40.105106, -73.890797) # New Jersey Bight
second_location = (39.978344, -73.947308)
third_location = (39.886616, -74.016935)


# predictie temperatura, la o anumita locatie
def get_temperature_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))     # colectam tot din baza de date, sortat dupa timp
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())                      # pentru punctul curent, luam datele ca dictionare
    data_frame = panda.DataFrame(dict_weather)                      # le transformam in data frame
    data_frame = data_frame.drop(                                   # eliminam coloanele ce nu influenteaza valoarea temperaturii
        ['time', 'latitude', 'longitude', 'cloudCover', 'gust', 'seaLevel', 'swellDirection', 'swellHeight',
         'swellPeriod', 'visibility', 'waterTemperature', 'waveDirection', 'waveHeight', 'windWaveDirection',
         'windWaveHeight'], axis=1)

    temperature_x = data_frame.drop(['airTemperature'], axis=1)    # toate datele ce influenteaza temperatura
    temperature_y = data_frame.pop('airTemperature')               # valorile temperaturii

    train_x, test_x, train_y, test_y = train_test_split(temperature_x, temperature_y, test_size=0.2, random_state=4)    # impartim ca 0.2 test si 0.8 train
    regression = DecisionTreeRegressor(random_state=0)             # pe baza unui model, trasam rezultatele
    regression.fit(train_x, train_y)
    prediction = regression.predict(test_x)                        # predictia finala

    print('             Air temperature')
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))


def get_precipitation_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())  # pentru punctul curent, luam datele ca dictionare
    data_frame = panda.DataFrame(dict_weather)  # le transformam in data frame
    data_frame = data_frame.drop(               # eliminam coloanele ce nu influenteaza valoarea precipitatiilor
        ['time', 'latitude', 'longitude', 'seaLevel', 'swellDirection', 'swellHeight',
         'swellPeriod', 'visibility', 'waterTemperature', 'waveDirection', 'waveHeight', 'windWaveDirection',
         'windWaveHeight', 'windDirection', 'windSpeed'], axis=1)

    precipitation_x = data_frame.drop(['precipitation'], axis=1)   # toate datele ce influenteaza precipitatiile
    precipitation_y = data_frame.pop('precipitation')              # valorile temperaturii

    train_x, test_x, train_y, test_y = train_test_split(precipitation_x, precipitation_y, test_size=0.2, random_state=4)

    regression = DecisionTreeRegressor(random_state=0)      # pe baza unui model, trasam rezultatele

    regression.fit(train_x, train_y)

    prediction = regression.predict(test_x)

    error = np.mean((prediction - test_y) ** 2)

    print('             Precipitations')                # predictia finala
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))

    print("     ERROR: " + str(error) + "\n")

    g = plt.scatter(test_y, prediction)
    g.axes.set_yscale('log')
    g.axes.set_xscale('log')
    g.axes.set_xlabel('True Values ')
    g.axes.set_ylabel('Predictions ')
    g.axes.axis('equal')
    g.axes.axis('square')
    plt.ylabel('Precipitation prediction')
    plt.show()


def get_wind_speed_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())
    data_frame = panda.DataFrame(dict_weather)
    data_frame = data_frame.drop(
        ['time', 'latitude', 'longitude', 'airTemperature', 'cloudCover', 'gust', 'humidity', 'precipitation', 'seaLevel', 'swellDirection', 'swellHeight',
         'swellPeriod', 'visibility', 'waterTemperature', 'waveDirection', 'waveHeight'], axis=1)

    wind_speed_x = data_frame.drop(['windSpeed'], axis=1)
    wind_speed_y = data_frame.pop('windSpeed')

    train_x, test_x, train_y, test_y = train_test_split(wind_speed_x, wind_speed_y, test_size=0.2, random_state=4)

    regression = DecisionTreeRegressor(random_state=0)
    regression.fit(train_x, train_y)
    prediction = regression.predict(test_x)
    error = np.mean((prediction - test_y) ** 2)

    print('             Wind speed')
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))

    print("     ERROR: " + str(error) + "\n")


def get_wind_direction_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())
    data_frame = panda.DataFrame(dict_weather)
    data_frame = data_frame.drop(
        ['time', 'latitude', 'longitude', 'airTemperature', 'cloudCover', 'gust', 'humidity', 'precipitation', 'seaLevel', 'swellDirection', 'swellHeight',
         'swellPeriod', 'visibility', 'waterTemperature', 'waveDirection', 'waveHeight'], axis=1)

    wind_direction_x = data_frame.drop(['windDirection'], axis=1)
    wind_direction_y = data_frame.pop('windDirection')

    train_x, test_x, train_y, test_y = train_test_split(wind_direction_x, wind_direction_y, test_size=0.2, random_state=4)

    regression = DecisionTreeRegressor(random_state=0)
    regression.fit(train_x, train_y)
    prediction = regression.predict(test_x)

    print('             Wind direction')
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))



def get_wave_direction_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())
    data_frame = panda.DataFrame(dict_weather)
    data_frame = data_frame.drop(
        ['time', 'latitude', 'longitude', 'airTemperature', 'cloudCover', 'gust', 'humidity', 'precipitation', 'swellDirection', 'swellHeight',
         'swellPeriod', 'visibility', 'waterTemperature'], axis=1)

    wind_direction_x = data_frame.drop(['waveDirection'], axis=1)
    wind_direction_y = data_frame.pop('waveDirection')

    train_x, test_x, train_y, test_y = train_test_split(wind_direction_x, wind_direction_y, test_size=0.2, random_state=4)

    regression = DecisionTreeRegressor(random_state=0)
    regression.fit(train_x, train_y)
    prediction = regression.predict(test_x)

    print('             Wave direction')
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))


def get_wave_height_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())  # pentru punctul curent, luam datele ca dictionare
    data_frame = panda.DataFrame(dict_weather)  # le transformam in data frame
    data_frame = data_frame.drop(
        ['time', 'latitude', 'longitude', 'swellDirection', 'swellHeight',
         'swellPeriod', 'visibility', 'waterTemperature'], axis=1)

    precipitation_x = data_frame.drop(['waveHeight'], axis=1)
    precipitation_y = data_frame.pop('waveHeight')

    train_x, test_x, train_y, test_y = train_test_split(precipitation_x, precipitation_y, test_size=0.2, random_state=4)

    regression = DecisionTreeRegressor(random_state=0)      # pe baza unui model, trasam rezultatele

    regression.fit(train_x, train_y)

    prediction = regression.predict(test_x)

    print('             Wave height')                # predictia finala
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))


#                   PREDICTING USING TORCH
# def get_visibility_prediction(coordinates):
#     weather_data = list(Weather.objects.all().order_by('time'))
#     dict_weather = []
#     for w in weather_data:
#         if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
#             dict_weather.append(w.data_dict())
#     data_frame = panda.DataFrame(dict_weather)
#     data_frame = data_frame.drop(
#         ['time', 'latitude', 'longitude', 'seaLevel', 'swellDirection', 'swellHeight',
#          'swellPeriod', 'waterTemperature', 'waveDirection', 'waveHeight', 'windWaveDirection',
#          'windWaveHeight', 'windDirection', 'windSpeed'], axis=1)
#
#     visibility_x = data_frame.drop(['visibility'], axis=1)
#     visibility_y = data_frame.pop('visibility')
#
#     train_x, test_x, train_y, test_y = train_test_split(visibility_x, visibility_y, test_size=0.2, random_state=4)
#
#     sc = MinMaxScaler(feature_range=(0, 1))
#     training_set = train_x
#     training_set_scaled = sc.fit_transform(training_set)
#
#     train_x = np.array(train_x)
#     train_y = np.array(train_y)
#
#     train_x = np.reshape(train_x, (train_x.shape[0], train_x.shape[1], 1))
#     regressor = Sequential()
#     regressor.add(Bidirectional(LSTM(units=30, return_sequences=True, input_shape=(train_x.shape[1], 1))))
#     regressor.add(Dropout(0.2))
#     regressor.add(LSTM(units=30, return_sequences=True))
#     regressor.add(Dropout(0.2))
#     regressor.add(LSTM(units=30, return_sequences=True))
#     regressor.add(Dropout(0.2))
#     regressor.add(LSTM(units=30))
#     regressor.add(Dropout(0.2))
#     regressor.add(Dense(units=7, activation='linear'))  # pentru urmatoarele 7 zile
#     regressor.compile(optimizer='adam', loss='mean_squared_error', metrics=['acc'])
#     regressor.fit(train_x, train_y, epochs=500, batch_size=32)


def get_visibility_prediction(coordinates):
    weather_data = list(Weather.objects.all().order_by('time'))
    dict_weather = []
    for w in weather_data:
        if w.latitude == coordinates[0] and w.longitude == coordinates[1]:
            dict_weather.append(w.data_dict())  # pentru punctul curent, luam datele ca dictionare
    data_frame = panda.DataFrame(dict_weather)  # le transformam in data frame
    data_frame = data_frame.drop(               # eliminam coloanele ce nu influenteaza valoarea precipitatiilor
        ['time', 'latitude', 'longitude', 'seaLevel', 'swellDirection', 'swellHeight',
         'swellPeriod', 'waterTemperature', 'waveDirection', 'waveHeight', 'windWaveDirection',
         'windWaveHeight', 'windDirection', 'windSpeed'], axis=1)

    visibility_x = data_frame.drop(['visibility'], axis=1)   # toate datele ce influenteaza precipitatiile
    visibility_y = data_frame.pop('visibility')              # valorile temperaturii

    train_x, test_x, train_y, test_y = train_test_split(visibility_x, visibility_y, test_size=0.2, random_state=4)

    regression = DecisionTreeRegressor(random_state=0)      # pe baza unui model, trasam rezultatele
    regression.fit(train_x, train_y)
    prediction = regression.predict(test_x)
    error = np.mean((prediction - test_y) ** 2)

    print('             Visibility')                # predictia finala
    print(panda.DataFrame({
        'actual': test_y,
        'prediction': prediction,
        'error': (test_y - prediction)
    }))

    print("     ERROR: " + str(error) + "\n")



def coordinate_prediction():
    print("First location - \n")
    get_temperature_prediction(first_location)
    print("Second location - \n")
    get_temperature_prediction(second_location)
    print("Third location - \n")
    get_temperature_prediction(third_location)
    get_precipitation_prediction(first_location)
    print("Wind speed -       \n")
    get_wind_speed_prediction(first_location)
    print("Wind direction -    \n")
    get_wind_direction_prediction(first_location)
    print("Wave direction -    \n")
    get_wave_direction_prediction(first_location)
    print("Wave height  - \n")
    get_wave_height_prediction(first_location)
    print("Visibility - \n")
    get_visibility_prediction(first_location)
