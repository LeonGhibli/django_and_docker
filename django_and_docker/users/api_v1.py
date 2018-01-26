from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
import json
from django.http import HttpResponse  
from django.views import View
from django.views.decorators.csrf import csrf_exempt

class Hello_Tracker_1(APIView):
    def get(self, request, *args, **kw):
        # Process any get params that you may need Any URL parameters get passed in **kw
        hello_message = self.kwargs['hello_message']
        result = { 'reply':hello_message}
        response = Response(result, status=status.HTTP_200_OK)
        return response  

class Hello_Tracker_2(View):
    def post(self, request):
        if request.POST.get('hello_message'):
            sendback_message = request.POST.get('hello_message')
        else:
            sendback_message = request.POST
        return_dict = {'reply':sendback_message}       
        response = HttpResponse(json.dumps(return_dict),content_type="application/json")
        return response

