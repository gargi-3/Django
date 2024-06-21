from django.http import HttpResponse
from django.views import View

# Create your views here.
class MyView(View):
    # def getView(self, request):
    #     return HttpResponse("Hello and welcome to Django-Views session.")

    def get(self, request):
        return HttpResponse("Hello and welcome to Django Class based Views session.")

# function based view example    
def my_view(request):
    return HttpResponse("Hello and welcome to Django Function based Views session.")