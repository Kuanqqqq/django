from django.shortcuts import render
from .models import GPU
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
def gpu(request):
    return render(request, 'gpu/gpu.html')


def get_all_gpus(request):
    gpu_list = GPU.objects.all()
    columns_ordering = {
        "0": "id",
        "1": "name",
        "2": "chipset",
        "3": "memory",
        "4": "core_clock",
        "5": "boost_clock",
        "6": "color",
        "7": "length",
        "8": "rating",
        "9": "price",
    }
    order = {
        'asc': '',
        'desc': '-'
    }
    total_qty = len(gpu_list)
    if request.is_ajax():
        order_column = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]')
        if order_column in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            gpu_list = gpu_list.order_by(order[order_dir] + columns_ordering[order_column])
    data = []
    for gpu in gpu_list:
        row = {
            'id': gpu.id,
            'name': gpu.__str__(),
            'chipset': gpu.chipset.__str__(),
            'memory': gpu.memory.__str__(),
            'core_clock': gpu.core_clock.__str__(),
            'boost_clock': gpu.boost_clock.__str__(),
            'color': gpu.color.__str__(),
            'length': gpu.length.__str__(),
            'rating': None,
            'price': None,
            'action': "<a class='btn btn-success' role='button', href='/build/add_component/gpu/" + str(gpu.id) + "/'>Add</a>",
        }
        data.append(row)
    obj = {
        'recordsFiltered': total_qty,
        'recordsTotal': total_qty,
        'data': data,
        }
    return JsonResponse(obj, safe=False)