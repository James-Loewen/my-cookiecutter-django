from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from allauth.account.decorators import verified_email_required

User = get_user_model()


class UserListView(LoginRequiredMixin, ListView):
    login_url = "/admin/login"
    model = User

@verified_email_required
def alt_users_list(request):
    template = "users/user_list.html"
    user_list = User.objects.all()
    context = {"object_list": user_list}
    return render(request, template, context)

# user_list_view = UserListView.as_view()
user_list_view = alt_users_list

