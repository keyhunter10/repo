from django.shortcuts import render, get_object_or_404
from .models import User
# Create your views here.
        
def user(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_form/user_detail.html', {'user': user})
