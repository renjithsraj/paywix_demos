from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Home page
def home(request):
    return render(request, 'home.html', {})


# Payu checkout page
@csrf_exempt
def payu_checkout(request):
    return render(request, 'payu.html', {})


# Payu success return page
@csrf_exempt
def payu_success(request):
    return JsonResponse(request.POST.GET)


# Payu failure page
def payu_failure(request):
    return JsonResponse(request.POST.GET)
