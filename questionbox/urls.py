"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from questionbox import views as q_views

from api.rest import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
	path('', q_views.homepage, name = 'home'),
    path('question/<int:pk>/', q_views.view_question, name = 'view_question'),
    path('question/ask/', q_views.post_question, name = "post_question"),
    path('question/<int:question_pk>/answer/', q_views.post_answer, name = "post_answer"),
    path('search/', q_views.search, name = 'search'),
    path('profile/', q_views.profile, name = 'myprofile'),
    path('profile/<str:username>/', q_views.profile, name = 'profile'),
    path('ajax/answer/<int:pk>/is_correct', q_views.is_correct, name = 'ajax_is_correct'),
    path('ajax/answer/<int:pk>/toggle_correct', q_views.toggle_correct, name = 'ajax_toggle_correct'),
    path('ajax/answer/<int:pk>/is_star/', q_views.is_star_answer, name = 'ajas_is_star_a'),
    path('ajax/question/<int:pk>/is_star/', q_views.is_star_question, name = 'ajax_is_star_q'),
    path('ajax/answer/<int:pk>/star/', q_views.star_answer, name = 'ajax_star_a'),
    path('ajax/question/<int:pk>/star/', q_views.star_question, name = 'ajax_star_q'),
    path('api/', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
