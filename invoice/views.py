from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice
from django.utils import timezone
from django.db.models import Sum


@login_required(login_url="/accounts/login")
def home(request):
    invoice = Invoice.objects
    return render(request,'invoices/home.html',{'invoice':invoice})

@login_required(login_url="/accounts/login")
def create(request):
    if request.method == 'POST':
        if request.POST['item_name'] and request.POST['quantity'] and request.POST['unit_price']:
            invoice = Invoice()
            invoice.item_name = request.POST['item_name']
            invoice.quantity = request.POST['quantity'] 
            invoice.unit_price = request.POST['unit_price']
            invoice.amount = int(request.POST['quantity']) * int(request.POST['unit_price'])
            # invoice.append('quantity').join(unit_price + request.POST['amount'])
            # def Numpy(Invoice):
            # def sum1(Invoice):
            #   invoice = Invoice()  
            #   total = 0
            #   for i in Invoice.objects.all():
            #           total += {{i}}
            #   return total
            invoice.total_price = Invoice.objects.annotate(total_price=Sum('amount'))
            invoice.Oracode = request.user
            invoice.save()
            return redirect('/invoices/' + str(invoice.id))
        else:
            return render(request, 'invoices/create.html',{'error':'All fields are Required'})
    else:
        return render(request, 'invoices/create.html')
    

@login_required(login_url="/accounts/login")
def detail(request,invoice_id):
    invoice = get_object_or_404(Invoice,pk=invoice_id)
    return render(request, 'invoices/detail.html',{'invoice':invoice})

@login_required(login_url="/accounts/login")
def delete(request,pk):
   items = Invoice.objects.filter(id=pk).delete()
#    itemsA = Invoice.objects.filter(Invoice,pk=invoice_id).delete()
   context = {'item':items}
   return render(request, 'invoices/home.html',context)

# def sum1(*args):
#     invoice = Invoice()
#     total = 0
#     for amount in args:
#             total += amount
#             invoice.save()
#     return total
# def total(invoice):
#         invoices = Invoice.objects.all()    
#         invoice = sum([invoice.amount for invoice in invoices])
#         return invoice
    
# def tok(lama):
#     lamaa = Invoice.objects.all()
#     return redirect('/invoices/' + str(invoice.id))

# def total2(invoice):
#     totala = 0
#     for invoice in Invoice.objects.all():
#         invoice.amount += totala 
#         return invoice
    
# def total3(request):
#     if request.method == 'POST':
#         if request.POST['total']:
#             tot = Total()
#             tot.amount = request.POST['amount']
#             tot.total = request.POST[tot.amount += la]
#             tot.save()
#     else:
#         return render(request, 'invoices/create.html')
        
    
    
# def total4(x):
#     t = Invoice.objects.all()
#     x = sum(t.amount for t in t)
#     return x   
    # for invoice in invoices:
    #     invoice = Invoice.objects.aggregate(Sum('amount'))
    # return invoice