import uuid
from urllib.parse import urljoin

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from yookassa import Configuration, Payment
from yookassa.domain.exceptions.unauthorized_error import UnauthorizedError

from foodplanapp.models import Order

from .models import OrderPayment


@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.payments.filter(is_paid=True).exists():
        return HttpResponse(f"Заказ {order_id} уже оплачен")
    
    return_url = urljoin(
        request.build_absolute_uri(),
        reverse(complete_payment, kwargs={"order_id": order_id})
    )

    try:
        Configuration.account_id = settings.SHOP_ID
        Configuration.secret_key = settings.SHOP_TOKEN

        payment = Payment.create({
            "amount": {
                "value": order.total_price,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": return_url,
            },
            "capture": True,
            "description": f"Заказ №{order_id}",
            "metadata": {"order_id": order_id},
        }, uuid.uuid4())
    except UnauthorizedError as error:
        return HttpResponse(f"Ошибка авторизации в форме оплаты, обратитесь в тех. поодержку сайта: {error}")

    OrderPayment.objects.create(
        payment_id=payment.id,
        order=order,
        created_at=payment.created_at,
        description=payment.description,
        status=payment.status,
        is_test=payment.test,
        payment_amount=payment.amount.value,
        payment_currency=payment.amount.currency,
        is_paid=payment.paid,
    )
    return redirect(payment.confirmation.confirmation_url)


@login_required
def complete_payment(request, order_id):
    order_payment = Order.objects.get(id=order_id).payments.order_by("-created_at").first()
    
    Configuration.account_id = settings.SHOP_ID
    Configuration.secret_key = settings.SHOP_TOKEN
    payment = Payment.find_one(order_payment.payment_id)
    
    order_payment.status = payment.status
    order_payment.is_paid = payment.paid
    order_payment.save()
    return redirect(reverse("profile"))
