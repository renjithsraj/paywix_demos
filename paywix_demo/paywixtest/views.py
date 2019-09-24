from django.shortcuts import render

# Create your views here.

def paywix_stripe_manage(request):
    print (request.POST)
    import pdb; pdb.set_trace();