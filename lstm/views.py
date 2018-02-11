from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from .lstm_new import *
import datetime
import matplotlib.pyplot as plt

# Create your views here.
def update(request):
	if(request.method == "POST"):
		#Add vlue to database.
		Update = UpdateForm(request.POST)
		if Update.is_valid():
			new_value = index_value()
			new_value.publish(Update.cleaned_data['value'], datetime.date.today())
			index_values = index_value.objects.all()
			predicted, fifty_day = predict_for_view(index_values)
			fig = plt.figure(facecolor='white')
			ax = fig.add_subplot(111)
			ax.plot(fifty_day, label="data so far")
			padding = [None for i in range(len(fifty_day))]
			plt.plot(padding + [predicted], label="predicted data")
			plt.savefig('C:\\Users\\naman\\Desktop\\lstm_daily\\lstm_daily\\lstm\\static\\lstm\\plot.png')
			return HttpResponseRedirect('/predictions/')
	else:
		Update = UpdateForm()
		return render(request, "lstm/update.html", {"UpdateForm":Update})

def predictions(request):
	return render(request, "lstm/predictions.html", {})