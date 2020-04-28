from django.db import models
from django.conf import settings
from django.urls import reverse
import datetime


# Create your models here.

class Order(models.Model):
	CATEGORY=(
		('COMPUTER','COMPUTER'),
		('FURNITURE','FURNITURE'),
		('OFFICE_EQUIPMENT','OFFICE EQUIPMENT'),
		('LINK_EQUIPMENTS','LINK_EQUIPMENTS'),
		('SERVER','SERVER'),
		)

	description=models.TextField(max_length=100)
	category=models.TextField(choices=CATEGORY)	
	cost=models.DecimalField(max_digits=10,decimal_places=2)
	quantity=models.IntegerField(default=1)
	total_cost=models.DecimalField(default=0,max_digits=10,decimal_places=2)
	order_date=models.DateField(default=datetime.date.today)
	status=models.TextField(max_length=100,default="unapproved")
	comments=models.TextField(max_length=200,default='None')
	document=models.FileField(null=True,upload_to='documents/%Y/%m/%d/')
	user=models.ForeignKey(
		to=settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE
		)
	supplier=models.ForeignKey(
		to='Supplier',
		on_delete=models.CASCADE
		)

	def approve(self):
		self.status='Approved'
		self.save()

	def reject(self):
		self.status='Rejected'
		self.save()

	def total_cost(self):
		self.total_cost=self.cost*self.quantity
		return self.total_cost
	

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('order:order-detail',kwargs={'pk':self.id})

	class Meta:
		permissions=(("can_approve_order","can_reject_order"),)

class Supplier(models.Model):
	name=models.TextField()
	location=models.TextField()
	phonenumber=models.TextField()
	email=models.EmailField()
	website=models.URLField()


	def __str__(self):
		return self.name
