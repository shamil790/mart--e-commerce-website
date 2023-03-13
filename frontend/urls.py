from django.urls import path
from frontend import views
urlpatterns = [
path('homehtmlpage/',views.homehtmlpage,name="homehtmlpage"),
path('aboutuspage/',views.aboutuspage,name="aboutuspage"),
path('contact/',views.contact,name="contact"),
path('categories/',views.categories,name="categories"),
path('discat/<itemcatg>/', views.discat, name="discat"),
path('singlepro/<int:dataid>/ ',views.singlepro, name="singlepro"),
path('registration/',views.registration,name="registration"),
path('savecustomer/',views.savecustomer,name="savecustomer"),
path('custemerlogin/',views.custemerlogin,name="custemerlogin"),
path('logout/',views.logout,name="logout"),
path('cntct/',views.cntct,name="cntct"),

]