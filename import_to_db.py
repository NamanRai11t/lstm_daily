import csv
import datetime
import django
import os

f = open("SENSEX.csv", "r")
csv_reader = csv.reader(f)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prediction.settings')
django.setup()
print('Setup complete.')
from lstm.models import index_value
for row in csv_reader:
	date_str = row[0]
	value = float(row[1])
	date_list = date_str.split('-')
	date = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
	index = index_value()
	index.publish(value, date)

