from django.shortcuts import render

def profile(request):
    """
    Display the users profile 
    """
    context = {}
    return render(request, 'profiles/profile.html', context)