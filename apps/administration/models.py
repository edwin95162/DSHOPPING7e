from django.db import models
from ckeditor.fields import RichTextField

class main(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status', default=True)
    create_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)
    modify_date = models.DateField('Modify date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Delete date', auto_now=True, auto_now_add=False)
    class Meta:
        abstract = True

class category(main):
    title = models.CharField('Category name', max_length=100)
    description = models.CharField('description', max_length=100)
    status = models.CharField('Status', max_length=100)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class country(main):
    title = models.CharField('Country name', max_length=100)
    abreviation = models.CharField('Abreviation', max_length=100)
    status = models.CharField('Status', max_length=100)
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.title

class gender(main):
    title = models.CharField('Country name', max_length=100)
    description = models.CharField('description', max_length=100)
    status = models.CharField('Status', max_length=100)
    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
    def __str__(self):
        return self.title
class clients(main):
    id_client = models.CharField('Id Client', max_length=10, unique=True)
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    id_gender = models.CharField('Gender', max_length=1)
    phone = models.CharField('phone', max_length=10, unique=True)
    email = models.EmailField('E-mail', max_length=150)
    password = models.CharField ('Password', max_length = 15)               
    id_country = models.CharField ('Id Country', max_length=20)    
    image = models.ImageField ('Author image', null= True, blank=True, upload_to='authors/')
    message = models.TextField('Status',max_length=10)
    credit_card_number = models.TextField('Number credit',max_length=15)
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return '{0}{1}{2}'.format(self.first_name," ",self.last_name)

class products(main):
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=100)
    id_category = models.ForeignKey (category, on_delete=models.CASCADE)
    id_country = models.ForeignKey (country, on_delete=models.CASCADE)
    photo = models.ImageField ('Prodcut photo', null= True, blank=True, upload_to='products/')
    quantity = models.CharField('Quantity', max_length=100)
    status = models.CharField('Status', max_length=100)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.title


class shopping(main):
    id_product = models.ForeignKey (products, on_delete=models.CASCADE)
    id_client = models.ForeignKey (clients, on_delete=models.CASCADE)
    shopping_date = models.CharField('Shopping Date', max_length=100)
    class Meta:
        verbose_name = 'Shopping'
        verbose_name_plural = 'Shoppings'
    def __str__(self):
        return self.id_product


