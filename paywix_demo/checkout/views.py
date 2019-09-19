from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from paywix.payu import PAYU
payu = PAYU()


# Home page
def home(request):
    return render(request, 'home.html', {})


# Payu checkout page
@csrf_exempt
def payu_checkout(request):
    if request.method == 'POST':
        data = dict(zip(request.POST.keys(), request.POST.values()))
        data['txnid'] = payu.generate_txnid()
        payu_data = payu.initate_transaction(data)
        print ("payu data us", payu_data)
        return render(request, 'payu_checkout.html', {"posted": payu_data})
    return render(request, 'payu.html', {})


# Payu success return page
@csrf_exempt
def payu_success(request):
    return JsonResponse(request.POST.GET)


# Payu failure page
def payu_failure(request):
    return JsonResponse(request.POST.GET)
