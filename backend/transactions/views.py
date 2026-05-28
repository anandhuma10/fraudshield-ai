from django.shortcuts import render
from .models import Transaction
from django.http import HttpResponse

# Create your views here.


def transaction_list(request):
    return HttpResponse("Transactions Page")

def home(request):

    total = Transaction.objects.count()

    fraud = Transaction.objects.filter(
        is_fraud=True
    ).count()

    safe = total - fraud

    context = {
        'total': total,
        'fraud': fraud,
        'safe': safe
    }

    return render(request, 'home.html', context)