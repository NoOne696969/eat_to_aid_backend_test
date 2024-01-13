from django.contrib import admin
from .models import CoupounModel, ShopModel

admin.site.register([CoupounModel,ShopModel])
