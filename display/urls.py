from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), # 目录页
    path('crispr/<crispr_id>', views.crispr, name = 'CRISPR'), # CRISPR页
    path('<sea>', views.location, name = 'location'),
    # path('import-data', views.importData, name='importData'), # 仅用来创建Nordic数据
]