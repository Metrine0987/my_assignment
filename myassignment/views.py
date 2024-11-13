from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')  # Render the homepage template

def service_details(request):
    return render(request, 'service_details.html')  # Render service details page template

def portfolio_details(request):
    return render(request, 'portfolio_details.html')  # Render portfolio details page template

def starter_page(request):
    return render(request, 'starter_page.html')

def main(request):
    return render(request, "base.html")
def contacts_page(request):
    return render(request, "contacts.html")
    