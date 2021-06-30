# UrcanDianaCristina_Project
Weather prediction using Django.

To add to the database, I used the response_data.py file, where I made the requests and sent the data to view.
On the predictions side, I used the predictions file - for some, I made the average error, respectively, the error for each step or the graph to highlight the difference between current and predicted values. We made predictions for the required parameters (weather conditions, wind direction and speed, direction and height
waves, visibility).
I extracted data for three different points in the NY area and did the temperature predictions part
for all three points. The data are in the range 05.06.2020-03.09.2020; more data could be retrieved, but it was difficult to train the model, given that the trained values ​​were not saved.
Execution is launched with python manage.py runserver.
