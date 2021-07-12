from django.urls import path
from .views import BbCreateView, index, BbByRubricView, BbDetailView, BbAddView, BbEditView, BbMonthArchiveView, BbRedirectView

#app_name = 'bboard'
urlpatterns = [
path('add/save/', BbAddView.as_view(), name='add'),
path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
path( '<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),  
path('', index, name='index'),
path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
path('detail/<int: year>/<int:month>/<int:day>/ <int:pk>/', BbDetailView.as_view(), name='detail'),
path('<int:year>/<int:month>/', BbMonthArchiveView.as_view()),
path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/', BbRedirectView.as_view(), name='old_detail' ) ,
#path('add/', BbCreateView.as_view(), name='add'), 
]
