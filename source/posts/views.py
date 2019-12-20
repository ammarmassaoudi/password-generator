from django.shortcuts import render
from .models import Post
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


@csrf_exempt
def home(request):
    number = request.POST["content"]
    password = ''
    chrs = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJMNHGBVFDCXSAZ123456789009876543210987654321!@#$%^&**&^%$#@!'
    for i in range(int(number)):
        password += random.choice(chrs)
    return render(request, "home.html", {
        "passwords": password
    })
