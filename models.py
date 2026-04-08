from django.db import models

class WebsiteSetting(models.Model):
    key = models.CharField(max_length=50, unique=True)
    value = models.JSONField()

    def __str__(self):
        return self.key

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    delivery_time = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image_url = models.URLField()
    video_url = models.URLField(blank=True, null=True)
    before_image = models.URLField(blank=True, null=True)
    after_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    badge = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, blank=True)
    comment = models.TextField()
    rating = models.IntegerField(default=5)
    approved = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service_type = models.CharField(max_length=50)
    video_length = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Order Received')
    file_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} from {self.name}"

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='Scissors')

    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.IntegerField()

    def __str__(self):
        return self.code
