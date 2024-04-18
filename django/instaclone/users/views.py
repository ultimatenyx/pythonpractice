from django.http import HttpResponse;

# Create your views here.
def index(request):
    # message = f'{request.method} -- {request.path_info} -- {request.META}'
    my_fav_color = request.GET["my_fav_color"]
    message = "I dont have anything to say about your favourite color"
    if my_fav_color=='blue':
        message = "Sky is Blue"
    elif my_fav_color=="yellow":
        message= "The sub is yellow"
    return HttpResponse(message)