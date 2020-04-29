# Purchase-Order-Manager-django
Django app for POs

Flow<br>
1.Create PO <br>
2.Approved by intermediate Supervisor<br>
3.Send email to the supplier<br>
4.Receive the PO and push data to Fixed Asset App<br>



<br>
For app installation
pip install purchase-order
Quick start
Add "po" to your INSTALLED_APPS setting like this:: INSTALLED_APPS = [ ... 'po', ]

Include the po URLconf in your project urls.py like this:: path('po/', include('po.urls')),

Run python manage.py migrate to create the Erp models.

Start the development server and visit http://127.0.0.1:8000/admin/to Add assets and perfom the operations (you'll need the Admin app enabled).

Visit http://127.0.0.1:8000/Erp/ to Enjoy various actions
