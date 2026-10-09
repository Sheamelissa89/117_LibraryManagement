from django.shortcuts import render


# Display the Library Inventory homepage
def home_view(request):
    return render(request, 'home.html')