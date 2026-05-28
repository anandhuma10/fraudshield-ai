from django.shortcuts import render
from django.http import JsonResponse
from transactions.models import Transaction

# Create your views here.






def assistant_home(request):

    total = Transaction.objects.count()

    fraud = Transaction.objects.filter(
        is_fraud=True
    ).count()

    safe = total - fraud

    if fraud > 5:
        risk = "High Risk"
    elif fraud > 0:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    response = {
        "assistant": "FraudShield AI",
        "status": "ACTIVE",

        "analytics": {
            "total_transactions": total,
            "fraud_transactions": fraud,
            "safe_transactions": safe,
            "risk_level": risk
        },

        "ai_message": (
            f"Detected {fraud} suspicious "
            f"transactions out of {total}."
        )
    }

    return JsonResponse(response)