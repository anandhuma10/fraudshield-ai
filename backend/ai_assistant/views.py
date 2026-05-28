import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from transactions.models import Transaction

# Create your views here.

def chat_page(request):

    return render(
        request,
        'ai_assistant/chat.html'
    )

@csrf_exempt
def chatbot(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        user_message = data.get(
            'message',
            ''
        ).lower()

        total = Transaction.objects.count()

        fraud = Transaction.objects.filter(
            is_fraud=True
        ).count()

        safe = total - fraud

        # AI Responses

        if 'fraud' in user_message:
            reply = (
                f"There are {fraud} "
                f"fraud transactions."
            )

        elif 'safe' in user_message:
            reply = (
                f"There are {safe} "
                f"safe transactions."
            )

        elif 'total' in user_message:
            reply = (
                f"Total transactions are {total}."
            )

        else:
            reply = (
                "I am FraudShield AI Assistant. "
                "Ask me about fraud, safe, "
                "or total transactions."
            )

        return JsonResponse({
            'user_message': user_message,
            'reply': reply
        })

    return JsonResponse({
        'error': 'POST request required'
    })




