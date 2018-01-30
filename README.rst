django_and_docker
=================

A short description of steps of building django framework and basic Rest API service with cookiecutter django_ in docker_ environment. 


Basic Environment
-----------------
Ubuntu 14.04 / Python 3.5


Steps
-----

Uninstall old versions of docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To ensure Docker version and avoid library conflict, remove older versions of Docker which were called docker or docker-engine.

Install Docker CE
^^^^^^^^^^^^^^^^^
Docker CE could be installed in different ways:

* Most users set up Docker’s repositories and install from them, for ease of installation and upgrade tasks. This is the recommended approach.
* Some users download the DEB package and install it manually and manage upgrades completely manually. This is useful in situations such as installing Docker on air-gapped systems with no access to the internet.
* In testing and development environments, some users choose to use automated convenience scripts to install Docker.

Due to the limitation of network connection in China，manual approach has been chosen.

* Access to https://download.docker.com/linux/ubuntu/dists/trusty/pool/stable/amd64/ and download docker-ce_17.12.0~ce-0~ubuntu_amd64.deb 
* Use FTP to send docker download package to target server.
* Install Docker CE with dpkg.
* Verify that Docker CE is installed correctly.

Install Cookiecutter
^^^^^^^^^^^^^^^^^^^^
* Get Cookiecutter via pip.
* Run cookiecutter command against repo https://github.com/pydanny/cookiecutter-django. To ensure the activation of whitenoise and mailhog, set use_whitenoise and use_mailhog as yes. Also, use_docker should be yes.
* cd to target project path just initilized.
* Create a git repo and push it to github.

Config before development
^^^^^^^^^^^^^^^^^^^^^^^^^
* Install docker-compose via pip
* Build the stack from local.yml via docker-compose. 
* Boot up via docker-compose to initilize the django framework.
* Create django superuser via docker-compose
* Add local ubuntu server IP to ALLOWED_HOSTS for better testing via browser of another local device. 
* Test mailhog email sending via http://LOCAL_IP:8025 

Development
^^^^^^^^^^^
Two APIs have been built in api_v1.py:

* Hello_Tracker_1 is built with django_restframework, using GET request to interactive via /users/api/v1/hello_1/(?P<hello_message>.+). It will get user parameter from url and response the parameter value.
* Hello_Tracker_2 is built with native django, using POST request to interactive via /users/api/v1/hello_1/. It will try to get user parameter 'hello_message' from request and send its value back; if no such parameter, it will send all user post data back.
* Add route in users/urls.py for API class.
* Disable django.middleware.csrf.CsrfViewMiddleware in settings for anonymous API visit. 

Hello_Tracker_1 tested by broswer request from local device. Hello_Tracker_1 tested by test.py

Further improvements
^^^^^^^^^^^^^^^^^^^
* Rearrange the API route from urls.py in /users to urls in /config so that it would be more convenient to manage api structure in future development.
* Add authentication control on API calls, ex. username and password verification or token verification.
* Exception control in logic process of API class.
