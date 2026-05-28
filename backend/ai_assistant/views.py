import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from transactions.models import Transaction


def chat_page(request):
    return render(request, 'ai_assistant/chat.html')


@csrf_exempt
def chatbot(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        user_message = data.get('message', '').lower()

        total = Transaction.objects.count()
        fraud = Transaction.objects.filter(is_fraud=True).count()
        safe = total - fraud

        # AI Logic
        if (
            'fraud' in user_message or
            'unsafe' in user_message or
            'scam' in user_message
        ):
            reply = f"There are {fraud} fraud transactions."

        elif (
            'safe' in user_message or
            'good' in user_message or
            'secure' in user_message
        ):
            reply = f"There are {safe} safe transactions."

        elif (
            'total' in user_message or
            'all' in user_message
        ):
            reply = f"Total transactions are {total}."

        elif (
            'hello' in user_message or
            'hi' in user_message
        ):
            reply = "Hello! I am FraudShield AI Assistant."

        else:
            reply = (
                "Sorry, I did not understand. "
                "Ask me about fraud, safe, or total transactions."
            )

        return JsonResponse({
            "user_message": user_message,
            "reply": reply,
            "total": total,
            "fraud": fraud,
            "safe": safe
        })

    return JsonResponse({
        "error": "POST request required"
    })