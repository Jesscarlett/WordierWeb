from django.http import HttpResponse
from django.shortcuts import render
import json
import os
import random


def read(request):
    return render(request, 'read.html')


def alice_one(request):
    return render(request, 'alice_one.html')
