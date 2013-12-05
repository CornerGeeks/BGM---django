Django Tech Demo at Brunei Geek Meet #1 - 6th December 2013
-----------------------------------------------------------

Files provided
-------------
requirements.txt
	Packages needed to run the projects

djangoapp
	The project created in the video. I blame the bad naming convention on QuickTime that failed to save my previous video which I thought was pretty good but it/I messed up.

bgm_project
	Initially the project I wanted to show but due to time constraints, I thought building something from scratch would be better. This project can be used as a quick reference guide to somethings that were mentioned in the video

Django admin login
------------------
admin/pass


Virtualenv Commands
-------------------
http://www.virtualenv.org/
	Isolated Python environments
		virtualenv environmentName
		source environmentName/bin/activate
		pip install ...
		pip install ...
		deactivate

Pip commands
------------
	pip install django
	pip list
	pip freeze > requirements.txt
	pip install -r requirements.txt

I tried it on Windows 8.1 and it seems installing some packages will cause it to compile it from source. It failed for me in Windows and reading online said that it required the Windows 7 SDK which was ~1.7GB. I downloaded it but it did not install / did not work so I'm not too sure what's wrong. I believe in OSX and Ubuntu/Linux it worked all fine
