
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')

def predict(request):
    result = None

    if request.method == "POST":
        amount = request.POST.get('amount')

        # Dummy prediction logic
        if float(amount) > 10000:
            result = "Fraud Transaction Detected"
        else:
            result = "Normal Transaction"

    return render(request, 'predict.html', {'result': result})