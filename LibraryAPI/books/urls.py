from django.urls import path
from .views import *

urlpatterns = [
    path('allbooks/',booklistview.as_view(),name='bookdetailview'),
    # path('author/<str:name>',authorfilterview.as_view(),name='authorfilterview'),
    path('idbook/<int:id>/',bookdetailview.as_view(),name='booklistview'),
    path('createbook/',createbook.as_view(),name='createbook'),
    path('onebooks/<int:id>/',bookoneview.as_view(),name='allbooklistview')
]
