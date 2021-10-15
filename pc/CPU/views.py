from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import CPU
# Create your views here.

def cpu(request):
    #need to make the table to dynamic
    return render(request, 'cpu/cpu.html')


def get_all_cpus(request):
    cpu_lst = CPU.objects.all()
    columns_ordering = {
        "0": "id",
        "1": "name",
        "2": "core_count",
        "3": "core_clock",
        "4": "boost_clock",
        "5": "TDP",
        "6": "integrated_graphics",
        "7": "SMT",
        "8": "rating",
        "9": "price",
    }
    order = {
        'asc': '',
        'desc': '-'
    }
    total_qty = len(cpu_lst)
    if request.is_ajax():
        order_column = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]')
        if order_column in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            cpu_lst = cpu_lst.order_by(order[order_dir] + columns_ordering[order_column])
    data = []
    for cpu in cpu_lst:
        row = {
            'id': cpu.id,
            'name': ("<img src=" + cpu.image.url + " with='100' height='100'>" + cpu.table_name()) if cpu.image else cpu.table_name(),
            'core_count': cpu.core_count.__str__(),
            'core_clock': cpu.core_clock.__str__(),
            'boost_clock': cpu.boost_clock.__str__(),
            'TDP': cpu.tdp.__str__(),
            'integrated_graphics': cpu.integrated_graphics.__str__(),
            'SMT': cpu.smt.__str__(),
            'rating': None,
            'price': None,
            'action': "<a class='btn btn-success' href='#' role='button'>Add</a>",
        }
        data.append(row)
    obj = {
        'recordsFiltered': total_qty,
        'recordsTotal': total_qty,
        'data': data,
        }
    return JsonResponse(obj, safe=False)
    
