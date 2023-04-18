from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import URL
from django.contrib.auth.decorators import login_required

class URLForm(modelform_factory(URL, fields=('original_url',))):
    def clean(self):
        cd = self.cleaned_data

        original_url = cd.get("original_url")
        print(original_url)
        if not str(original_url).startswith(('http:','https:')):
            raise ValidationError("Only HTTP and HTTPS URLs can be shortened.")

@login_required(login_url="/accounts/login")
def new_url(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = URLForm()
    return render(request, "URLs/new_URL.html", {'form': form})

def handle_short(request, sh_url):
    obj = URL.objects.get(short_url=sh_url)
    real_url = obj.original_url
    obj.red_counter += 1
    obj.save()
    return redirect(real_url)