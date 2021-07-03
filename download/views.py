from django.http import HttpResponse
from download.forms import ImageForm
from django.shortcuts import render, redirect
from .models import Image 


def index(request):
    images = Image.objects.all() 
    print(images)
    return render(request, 'images.html', {'images': images})

def upload(request): 
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
        return redirect('images')
        #render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})



def view_image(request, image_id): 
   image = Image.objects.get(id=image_id)

   return render(request, 'image.html', {'id':image.id, 'title': image.title,'src': image.path_image,'date': image.date,   })

def delete_image(request, image_id): 
    try:
        image = Image.objects.get(id=image_id)
        image.path_image.delete(save=True) 
        image.delete() 
        return redirect('images')
    except: 
        return redirect('images')
