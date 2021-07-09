from django.urls import path
from .views import BbCreateView, index, BbByRubricView, BbDetailView, BbAddView, BbEditView

#app_name = 'bboard'
urlpatterns = [
path('add/save/', BbAddView.as_view(), name='add'),
path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
path( '<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),  
path('', index, name='index'),
path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
#path('add/', BbCreateView.as_view(), name='add'), 
]
