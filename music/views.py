from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Album
from django.shortcuts import render



def index(request):
    #return HttpResponse("<div><h1>Hello World!<br>I am Music URL.......</h1></div>")
     
    #through this line I remove error yeee
    all_albums = Album.objects.all() # pylint: disable=maybe-no-member 
    template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums,
    }
    return HttpResponse(template.render(context,request))

def detail(request,album_id):
    #return HttpResponse("<h1>Details for Album id:"+str(album_id)+"</h1>")

    try:
        album = Album.objects.get(pk=album_id)  # pylint: disable=maybe-no-member
    except Album.DoesNotExist: # pylint: disable=maybe-no-member
        raise Http404("Album Does Not Exist")
    return render(request,'music/detail.html',{'album':album})
