from django.db import models

# Create your models here.

class index_value(models.Model):
	value = models.FloatField()
	date = models.DateField()

	def publish(self, value, date):
		self.value = value
		self.date = date
		self.save()

	def __str__(self):
		return str(self.value)

class prediction_value(models.Model):
	value = models.FloatField()
	date = models.DateField()

	def publish(self, value, date):
		self.value = value
		self.date = date
		self.save()

	def __str__(self):
		return str(self.value)