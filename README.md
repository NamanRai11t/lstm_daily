#LSTM Daily

A django server to predict BSE and update everyday.

Run the server with:

    python manage.py runserver

And head to:

    http://localhost:8000/update/

To add today's closing value to the database, and re-plot the prediction for the next day. You can see the plot at:

    http://localhost:8000/predictions/

Requirements are in requirements.txt, and can be quickly installed with:

    pip install -r requirements.txt