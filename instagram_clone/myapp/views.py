from django.shortcuts import render
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        return render(request, 'main.html')
    
class Test(APIView):
    def get(self, request):
        return render(request, 'test.html')