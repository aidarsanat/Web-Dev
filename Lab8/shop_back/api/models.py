from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6 ,decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'count': self.count,
            # 'image': self.image,
            'category': self.category.name,
            'is_active': self.is_active
        }

    # laptop_category = Category(name="Laptops")
    # laptop_category.save()
    #
    # phone_category = Category(name="Phones")
    # phone_category.save()
    #
    # shoe_category = Category(name="Shoes")
    # shoe_category.save()
    #
    # console_category = Category(name="Consoles")
    # console_category.save()
    #
    # camera_category = Category(name="Cameras")
    # camera_category.save()
    #
    # tv_category = Category(name="TVs")
    # tv_category.save()






    # watch_category = Category(name="Watches")
    # watch_category.save()

    # product1 = Product(
    #     name="Apple MacBook Pro",
    #     description="Powerful laptop for professionals",
    #     price=1999.99,
    #     count=10,
    #     image="product_images/macbook.jpg",
    #     category=laptop_category,
    #     is_active=True
    # )
    #
    # product2 = Product(
    #     name="Samsung Galaxy S21",
    #     description="Flagship smartphone with a stunning camera",
    #     price=999.99,
    #     count=20,
    #     image="product_images/galaxy_s21.jpg",
    #     category=phone_category,
    #     is_active=True
    # )
    #
    # product3 = Product(
    #     name="Nike Air Max 90",
    #     description="Iconic sneakers with a comfortable fit",
    #     price=119.99,
    #     count=50,
    #     image="product_images/air_max.jpg",
    #     category=shoe_category,
    #     is_active=True
    # )
    #
    # product4 = Product(
    #     name="Sony PlayStation 5",
    #     description="Next-gen gaming console with ultra-fast SSD",
    #     price=499.99,
    #     count=5,
    #     image="product_images/ps5.jpg",
    #     category=console_category,
    #     is_active=True
    # )
    #
    # product5 = Product(
    #     name="Canon EOS R5",
    #     description="High-end mirrorless camera with 45MP sensor",
    #     price=3899.99,
    #     count=2,
    #     image="product_images/eos_r5.jpg",
    #     category=camera_category,
    #     is_active=True
    # )
    #
    # product6 = Product(
    #     name="LG OLED CX",
    #     description="4K OLED TV with stunning picture quality",
    #     price=1999.99,
    #     count=3,
    #     image="product_images/lg_oled.jpg",
    #     category=tv_category,
    #     is_active=True
    # )
    #
    # product7 = Product(
    #     name="Fitbit Sense",
    #     description="Advanced smartwatch with health and fitness tracking",
    #     price=299.99,
    #     count=15,
    #     image="product_images/fitbit_sense.jpg",
    #     category=watch_category,
    #     is_active=True
    # )
    #
    # product8 = Product(
    #     name="Bose QuietComfort 35 II",
    #     description="Wireless noise-cancelling headphones for immersive sound",
    #     price=299.99,
    #     count=8,
    #     image="product_images/bose_qc35.jpg",
    #     category=headphone_category,
    #     is_active=True
    # )
    # product9 = Product(
    #     name="Sony PlayStation 5",
    #     description="Next-generation gaming console",
    #     price=499.99,
    #     count=5,
    #     image="product_images/ps5.jpg",
    #     category=console_category,
    #     is_active=True
    # )
