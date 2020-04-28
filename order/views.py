from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,TemplateView
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from order.forms import OrderForm,CommentUpdateForm,NewSupplierForm
from order.models import*
import csv


# Create your views here.
@login_required
def index(request):
	template_name='base.html'
	q=Order.objects.filter(Q(user=request.user)&Q(status='unapproved'))
	user_approved=Order.objects.filter((Q(user=request.user))&((Q(status='Approved'))|(Q(status='Rejected'))))
	order_list=Order.objects.filter(status='unapproved')
	return render(request,template_name,{'q':q,'order_list':order_list,'user_approved':user_approved})

class OrderDetail(DetailView):
	model=Order


class OrderUpdate(UpdateView):
	form_class=OrderForm
	model=Order
	template_name='order/order-update.html'

class OrderDelete(DeleteView):
	model=Order
	success_url=reverse_lazy('order:index')

class NewOrder(CreateView):
	form_class=OrderForm
	template_name='order/order.html'

	def get_initial(self):
		return {'user':self.request.user}

	def form_valid(self,request):
		if self.request.method=='POST':
			form=OrderForm(self.request.POST,self.request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponse("order created!!!")
			return render(request,self.template_name,{'form':form})
		else:
			return render(request,self.template_name)

class NewSupplier(CreateView):
	form_class=NewSupplierForm
	template_name='order/add-supplier.html'	

	def form_valid(self,request):
		if self.request.method=='POST':
			form=NewSupplierForm(self.request.POST)
			if form.is_valid():
				form.save()
				return HttpResponse("Supplier created successfully")
			return render(request,self.template_name,{'form':form})
		else:
			return render(request,self.template_name)


def all_order_per_user(request,pk):
	order_per_user=Order.objects.filter(user=request.user)
	return render(request,'order/order-list.html',{'order_per_user':order_per_user})
			
def search(request):
	template_name='order/search.html'
	if request.method=='GET':
		query=request.GET.get('q')
		submitbutton=request.GET.get('submit')

		if query is not None:
			results=Order.objects.filter(description__icontains=query)
			return render(request,template_name,{'results':results,'submitbutton':submitbutton})
		else:
			return render(request,template_name)


def order_approve(request,pk):
	orders=Order.objects.get(pk=pk)
	orders.approve()
	return redirect('/')

def order_reject(request,pk):
	orders=Order.objects.get(pk=pk)
	orders.reject()
	return redirect('/')



def orders_download(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename="all_orders.csv"'
	query=Order.objects.all()

	writer=csv.writer(response)
	writer.writerow(['DESCRIPTION','COST','QUANTITY','TOTAL_COST','CATEGORY','STATUS','DATE_ORDERED'])
	
	for rows in query:
		writer.writerow([rows.description,rows.cost,rows.quantity,rows.total_cost(),rows.category,rows.status,rows.order_date])
	return response

def approved_download(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename="approved_orders.csv"'
	query=Order.objects.filter(status='approved')

	writer=csv.writer(response)
	writer.writerow(['DESCRIPTION','COST','QUANTITY','TOTAL_COST','CATEGORY','STATUS','DATE_ORDERED'])
	
	for rows in query:
		writer.writerow([rows.description,rows.cost,rows.quantity,rows.total_cost,rows.category,rows.status,rows.order_date])
	return response

def rejected_download(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename="rejected.csv"'
	query=Order.objects.filter(status='rejected')

	writer=csv.writer(response)
	writer.writerow(['DESCRIPTION','COST','QUANTITY','TOTAL_COST','CATEGORY','STATUS','DATE_ORDERED'])
	
	for rows in query:
		writer.writerow([rows.description,rows.cost,rows.quantity,rows.total_cost,rows.category,rows.status,rows.order_date])
	return response
