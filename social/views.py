from django.shortcuts import render
from django.http import HttpResponse 
from social.post import SearchContentForPost
# Create your views here.

def post(request): 
    if request.method == 'POST':
        url = request.POST.get('url')
        post = SearchContentForPost(url)
        
        return render(request, 'social/create.html', {'context': post.create_info_post()})
    else: 
        return render(request, 'social/create.html', {'context':""})


