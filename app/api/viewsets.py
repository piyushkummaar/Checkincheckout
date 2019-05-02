from app.models import Location ,Message
from .serializer import LocationSerializer ,MessageSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .pagination import PostLimitoffsetPagination


class MessageFilter(filters.FilterSet):

    class Meta:
        model = Message
        fields = {
            'message': ['icontains'],
            'date': ['iexact', 'lte', 'gte'],
        }

class LocationFilter(filters.FilterSet):

    class Meta:
        model = Location
        fields = {
            'user': ['icontains'],
            'location': ['icontains'],
            'date': ['iexact', 'lte', 'gte'],
        }


class LoactionViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filterset_class = LocationFilter
    pagination_class = PostLimitoffsetPagination

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filterset_class = MessageFilter
    pagination_class = PostLimitoffsetPagination #PageNumberPagination
    

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

#filter
    # def get_queryset(self):
    #     return Message.objects.filter(message='klj')