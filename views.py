from rest_framework import viewsets
from .models import WebsiteSetting, Service, PortfolioItem, Offer, Review, Order, Tool, Coupon
from .serializers import (
    WebsiteSettingSerializer, ServiceSerializer, PortfolioItemSerializer,
    OfferSerializer, ReviewSerializer, OrderSerializer, ToolSerializer, CouponSerializer
)

class WebsiteSettingViewSet(viewsets.ModelViewSet):
    queryset = WebsiteSetting.objects.all()
    serializer_class = WebsiteSettingSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer

class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all().order_by('id')
    serializer_class = PortfolioItemSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('id')
    serializer_class = OfferSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all().order_by('id')
    serializer_class = ToolSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all().order_by('id')
    serializer_class = CouponSerializer
