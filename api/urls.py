from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.park_views import Parks, ParkDetail
from .views.meet_up_views import MeetUpIndex, MeetUpCreate, MeetUpDetailsShow, MeetUpDetailsDeleteUpdate

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('park/', Parks.as_view(), name='park'),
    path('park/<int:pk>/', ParkDetail.as_view(), name='park_detail'),
    path('meetup/', MeetUpIndex.as_view(), name='meetup'),
    path('meetup/create/', MeetUpCreate.as_view(), name='meetup_create'),
    path('meetup/<int:pk>/', MeetUpDetailsShow.as_view(), name='meetup_detail_show'),
    path('meetup/<int:pk>/edit', MeetUpDetailsDeleteUpdate.as_view(), name='meetup_detail_edit'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
