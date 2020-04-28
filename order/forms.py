from django import forms
from order.models import Order,Supplier
from django.contrib.auth import get_user_model

class OrderForm(forms.ModelForm):
	user=forms.ModelChoiceField(
		queryset=get_user_model().objects.all(),
		widget=forms.HiddenInput
		)

	class Meta:
		model=Order
		fields=['user','description','category','cost','quantity','supplier','comments','document']
		widgets={
			'description':forms.Textarea(attrs={'col':1,'rows':1}),
		}
class CommentUpdateForm(forms.ModelForm):
	class Meta:
		model=Order
		fields=['comments']
class NewSupplierForm(forms.ModelForm):
	class Meta:
		model=Supplier
		fields=['name','email','phonenumber','location','website']
		widgets={
		'name':forms.Textarea(attrs={'col':1,'rows':1}),
		'email':forms.Textarea(attrs={'col':1,'rows':1}),
		'phonenumber':forms.Textarea(attrs={'col':1,'rows':1}),
		'location':forms.Textarea(attrs={'col':1,'rows':1}),

		}