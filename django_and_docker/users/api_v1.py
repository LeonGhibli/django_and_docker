from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
import json

class Hello_Tracker(APIView):
    def get(self, request, *args, **kw):
        # Process any get params that you may need Any URL parameters get passed in **kw
        print (self.kwargs)
        hello_message = self.kwargs['hello_message']
        print (hello_message)
        result = { 'reply':hello_message}
        response = Response(result, status=status.HTTP_200_OK)
        return response  
