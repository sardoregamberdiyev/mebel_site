from django.urls import path
from .tg_log.views import LogViews
from .tg_user.views import UserViews
from .site_category.views import CategoryViews
from .site_product.views import ProductViews


urlpatterns = [
    path("log/<pk>/", LogViews.as_view(), name='user_log'),

    path("prod/", ProductViews.as_view(), name='product_log'),
    path("prod/<pk>/", ProductViews.as_view(), name='product_one'),

    path("user/", UserViews.as_view(), name='user_log'),
    path("user/<pk>/", UserViews.as_view(), name='user_one'),

    path("ctg/", CategoryViews.as_view(), name='ctg_log'),
    path("ctg/<pk>/", CategoryViews.as_view(), name='ctg_one'),

]
