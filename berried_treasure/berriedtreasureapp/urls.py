from django.conf.urls import url
from berriedtreasureapp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^results/$', views.ResultsPageView.as_view()),
]