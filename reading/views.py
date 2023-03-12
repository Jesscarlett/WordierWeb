from django.http import HttpResponse
from django.shortcuts import render
import json
import os
import random


def read(request):
    return render(request, 'read.html')


def alice_one(request):
    return render(request, 'alice_one.html')


def alice_two(request):
    return render(request, 'alice_two.html')


def alice_three(request):
    return render(request, 'alice_three.html')


def alice_four(request):
    return render(request, 'alice_four.html')