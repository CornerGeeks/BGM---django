from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response

from bgm_app.forms import MeetupForm
from bgm_app.models import Meetup

from django.http import HttpResponse
# Create your views here.
def home(request):
    msg = ""
    msg = "This is the <a href='/'>home page</a><br>\n"
    msg += " Go to a <a href='template'>full HTML template</a><br>\n"
    msg += " Go to a <a href='page1'>page using a base template</a><br>\n" 

    return HttpResponse(msg)
def template(request):
    context = RequestContext(request)
    data = {
        'page' : '/templates/template.html',
        'array' : [1,2,3,4],
        'html' : "<a href='/'>home</a>",
    }
    return render_to_response('template.html', {'viewdata': data}, context)
def templateWithBase(request):
    return HttpResponse("This is the home page<br><a href='template'>template</a>")
def page1(request):
    context = RequestContext(request)
    data = {
        'page_name' : 'Page 1',
        'pages': [
            {'url': 'page1', 'name': 'Page 1'},
            {'url': 'page2', 'name': 'Page 2'},
        ]
    }
    return render_to_response('page1.html', {'viewdata': data}, context)
def page2(request):
    context = RequestContext(request)
    data = {
        'pages': [
            {'url': '/', 'name': 'Home'},
            {'url': 'page1', 'name': 'Page 1'},
            {'url': 'page2', 'name': 'Page 2'},
        ]
    }
    return render_to_response('page2.html', {'viewdata': data}, context)
####################
# app proper 

def index(request):
    context = RequestContext(request)
    meetups = Meetup.objects.extra( select={'lower_name': 'lower(name)'}).order_by('lower_name')
    last_5 = Meetup.objects.order_by('-created')[:5]
    return render_to_response('bgm/index.html', {'meetups': meetups, 'last': last_5}, context)

def register(request): 
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

    return render_to_response('bgm/register.html', {'form': form}, context)

def meetup(request, meetup_id): 
    context = RequestContext(request)
    context_dict = {}
    context_dict['meetup_id'] = meetup_id
    meetup = []
    try:
        meetup = Meetup.objects.get(id=meetup_id)
        context_dict['meetup'] = meetup
    except Meetup.DoesNotExist:
        pass
    try:
        members = Member.objects.filter(meetup_id=meetup_id)
        context_dict['members'] = members
    except Exception as e:
        pass
    return render_to_response('bgm/meetup.html', context_dict, context)

