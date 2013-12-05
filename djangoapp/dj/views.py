from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response


# Create your views here.
from django.http import HttpResponse
from dj.models import Meetup
from dj.forms import MeetupForm

def index(request):
	context = RequestContext(request)
	meetups = Meetup.objects.extra( select={'lower_name': 'lower(name)'}).order_by('lower_name')
	return render_to_response('dj/index.html', {'meetups': meetups }, context)
def add(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = MeetupForm(request.POST)
		if form.is_valid():
			meetup = form.save(commit=False)
			if 'picture' in request.FILES:
				meetup.picture = request.FILES['picture']
			meetup.save()
			return index(request)
		else:
			print form.errors
	else:
		form = MeetupForm()

	return render_to_response('dj/add.html', {'form': form }, context)
