from django.shortcuts import render, redirect

from apps.delivery.forms import DeliveryConfigForm


# Create your views here.
def home(request):
    return render(request, "delivery/home.html", {})


def create(request):
    if request.method == "POST":
        form = DeliveryConfigForm(request.POST)
        if form.is_valid():
            delivery_days = ','.join(form.cleaned_data['delivery_days'])
            instance = form.save(commit=False)
            instance.delivery_days = delivery_days
            instance.save()
            return redirect('delivery:home')
    else:
        form = DeliveryConfigForm()

    return render(request, 'delivery/new.html', {'form': form})
