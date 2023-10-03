from django.shortcuts import render, redirect

from apps.delivery.forms import DeliveryConfigForm
from apps.delivery.models import DeliveryConfig


# Create your views here.
def home(request):
    delivery_configs = DeliveryConfig.objects.filter(brand=request.user.brand)
    return render(request, "delivery/list.html", {'delivery_configs': delivery_configs})


def create(request):
    if request.method == "POST":
        form = DeliveryConfigForm(request.POST)
        if form.is_valid():
            delivery_days = ','.join(form.cleaned_data['delivery_days'])
            reminder_delivery_days = ','.join(form.cleaned_data['reminder_delivery_days'])
            instance = form.save(commit=False)
            instance.delivery_days = delivery_days
            instance.reminder_delivery_days = reminder_delivery_days
            instance.save()
            return redirect('delivery:home')
    else:
        form = DeliveryConfigForm(initial={'brand': request.user.brand})

    return render(request, 'delivery/new.html', {'form': form})