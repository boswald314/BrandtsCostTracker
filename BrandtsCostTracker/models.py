from django.db import models
from django.utils.timezone import now


def invoice_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/invoices/<year>/<month>/<day>/<filename>
    return 'invoices/{0}/{1}'.format(now().strftime("%Y/%m/%d"), filename)

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    # Additional supplier fields

class Product(models.Model):
    name = models.CharField(max_length=100)
    # Additional product fields

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    invoice_image = models.ImageField(upload_to=invoice_directory_path)
    # Additional fields like quantity, unit, etc.
