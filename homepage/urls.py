from django.conf.urls import url
from homepage import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r"^login/", views.login_view, name='loginview'),
    url(r"^logout/", views.logout_view, name='logoutview'),
    url(r"^register/", views.register_view, name='registerview'),
    url(r"^submit/",
        views.ticket_submission_view, name="ticket_submission"),
    path('ticket/<int:ticket_id>/',
         views.ticket_detail_view, name='ticket_detail'),
    path('user/<int:user_id>/',
         views.user_detail_view, name='user_detail'),
    path('user/<int:ticket_id>/edit/',
         views.edit_ticket_view, name='edit_ticket'),
    path('assign/<int:id>/',
         views.assigned_to, name="assigned"),
    path('complete/<int:id>/',
         views.completed_by, name="completed"),
    path('invalid/<int:id>/',
         views.mark_invaild, name="invalid"),
    ]
