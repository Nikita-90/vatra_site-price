from django.shortcuts import render, redirect
import xlrd

from .models import LoadingFile, Price


def index(request):
    return render(request, 'price/index.html', {})


def load_price(request):
    if request.method == 'POST':
        f = LoadingFile(file=request.FILES['price'])
        f.save()
        name, cost = proc_file(str(LoadingFile.objects.order_by()[len(LoadingFile.objects.order_by())-1]))
        errors = []
        if len(name) == len(cost):
            errors = save_price_to_db(name, cost, f)
        print(errors)
        return redirect('/')
    return render(request, 'price/load_price.html', {})


def search_position(request):
    price = []
    if request.method == 'POST':
        search_ = request.POST['search']
        search = search_.lower().strip()
        search = option_minus(search)
        for pos in search:
            price.extend(search_engine(pos))
        return render(request, 'price/search_position.html', {'price': price, 'search': search_})
    else:
        return render(request, 'price/search_position.html', {})


def search_engine(search):
    price = []
    for position in Price.objects.filter(name__contains=search):
        price.append((position.name_views, round(position.cost, 2), position.loadingfile))
    return price


def save_price_to_db(name, cost, file):
    error = []
    for i in range(len(name)):
        price = Price(loadingfile=file, name=name[i].lower(), name_views=name[i], cost=cost[i])
        try:
            price.save()
        except ValueError:
            error.append((name[i], cost[i]))
    return error


def proc_file(fname):
    name = []
    cost = []
    rb = xlrd.open_workbook(fname, formatting_info=True)
    nsheet = rb.nsheets
    for n in range(nsheet):
        sheet = rb.sheet_by_index(n)
        for col in range(sheet.ncols):
            if sheet.row_values(0)[col] == 'name':
                name.extend(sheet.col_values(col))
            if sheet.row_values(0)[col] == 'cost':
                cost.extend(sheet.col_values(col))
    return name, cost


def option_minus(search):
    search = list(search)
    for s in range(len(search)):
        if search[s].isdigit() and (search[s-1] in [' ', '-'] or search[s-1].isalpha()):
            if not search[s-1].isalpha():
                del search[s-1]
                s -= 1
            print(search, s)
            search1 = search_option(s, search[:], '-')
            search2 = search_option(s, search[:], ' ')
            search3 = search_option(s, search[:], '')
            print(search1, search2, search3)
            return search1, search2, search3
    search = ''.join(search),
    print(search)
    return search


def search_option(i, search, sign):
    search.insert(i, sign)
    s = ''.join(search)
    return s
