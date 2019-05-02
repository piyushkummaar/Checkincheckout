from app.api.viewsets import LoactionViewSet,MessageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('location', LoactionViewSet, base_name='location')
router.register('message', MessageViewSet, base_name='message')

# for url in router.urls:
#     print(url,'/n')