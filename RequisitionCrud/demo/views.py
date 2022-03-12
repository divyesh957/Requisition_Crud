from django.contrib import messages
from django.shortcuts import render, redirect
from demo.models import User, Catogory, Subcatogory

def register(request):
    """
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        con_opass = request.POST["password2"]
        age = request.POST["age"]
        mobileNo = request.POST["mobileNo"]
        address = request.POST["address"]
        try:
            if password == con_opass:
                User(username=username, email=email, password=password,  mobileNo=mobileNo,
                        address=address, age=age).save()
                messages.success(request, 'The New User ' + request.POST["username"] + ' is saved Successful...!')
                return render(request, 'login.html')
            else:
                messages.success(request, "password don't match")
                return redirect("register")
        except:
            messages.success(request, "Enter Valid Email")
            return render(request, 'register.html')
    return render(request, 'register.html')


def login(request):
    """
    :param request:
    :return:
    """
    if request.method == "POST":
        try:
            userdetail = list(User.objects.filter(email=request.POST["email"], password=request.POST["password"]))
            if userdetail:
                messages.success(request, "login success...!!!")
                return redirect('index')
            else:
                messages.success(request, "User Not Found...please register first!!!")
                return render(request, 'register.html')
        except User.DoesNotExist as e:
            messages.success(request, 'username/password Invalid')
    return render(request, 'login.html')


def index(request):
    """
    :param request:
    :return:
    """
    get_sub_category_data = Subcatogory.objects.filter()
    sub_data = []
    for j in get_sub_category_data:
        sub_data.append({
            "id": j.id,
            "name": j.name,
            "description": j.description,
        })

    get_data = Catogory.objects.filter()
    data = []
    for i in get_data:
        abc = list(Subcatogory.objects.filter(id=i.subcategory_id))
        for j in abc:
            data.append({
                "id": i.id,
                "name": i.name,
                "description": i.description,
                "subcategory": j.name,
            })

    return render(request, 'index.html', context={"data": data, "subcatdata":sub_data})

def changepasswordform(request):
    """
    :param request:
    :return:
    """
    return render(request, 'changepassword.html')

def changepassword(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    try:
        count = User.objects.get(id=id, password=request.POST["oldpassword"]).count()
        print(count)
        if count == 1:
            abc = User.objects.filter(id=id).update(password=request.POST["newpassword"])
            messages.info(request, 'ok')
        else:
            messages.info(request, 'Invalid Old Password.')
        return render(request, 'index.html')
    except:
        return render('/index')


def addCategory(request):
    """
    :param request:
    :return:
    """
    try:
        abc = list(Subcatogory.objects.all())
        sddsd = []
        for i in abc:
            json_data = {
                "id": i.id,
                "name": i.name
            }
            sddsd.append(json_data)

        get_emp = []
        get_empl_data = Subcatogory.objects.filter()
        for i in get_empl_data:
            get_emp.append({
                "id": i.id,
                "name": i.name,
                "description": i.description,
            })
        return render(request, 'addCategory.html', context={"sddsd": sddsd, "get_emp": get_emp})
    except Exception as e:
        return render('/index')

def Category(request):
    """
    :param request:
    :return:
    """

    try:
        name = request.POST["name"]
        description = request.POST["description"]
        subcategory = request.POST["subcategory"]

        catogory = Catogory.objects.create(name=name, description=description, subcategory_id=subcategory)
        catogory.save()

        get_category_data = Catogory.objects.filter()

        data = []
        for i in get_category_data:
            abc = list(Subcatogory.objects.filter(id=i.subcategory_id))
            for j in abc:
                data.append({
                    "id": i.id,
                    "name": i.name,
                    "description": i.description,
                    "subcategory": j.name,
                })

        return redirect('/index')
    except Exception as e:
        return redirect('/index')


def deleteCategory(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    try:
        Catogory.objects.filter(id=id).delete()
        data = []
        get_data = Catogory.objects.filter()
        for i in get_data:
            data.append({
                "id": i.id,
                "name": i.name,
                "description": i.description,
            })
        messages.success(request, "delete category data")
        return redirect('/index')
    except Exception as e:
        return redirect('/index')


def updateCategory(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    try:
        data_req = Subcatogory.objects.all()
        get_Requisition_data = Catogory.objects.filter(id=id)

        for i in get_Requisition_data:
            id = i.id
            name = i.name
            description = i.description
            subcategory = i.subcategory_id


        return render(request, 'updateCategory.html', context={"id": id, "name": name, "description": description,
                                                               "subcategory_by": subcategory, "subcategory": data_req})
    except Exception as e:
        return render(request, 'updateCategory.html')

def updateCategoryData(request, id):
    """
    :param request:
    :param id:
    :return:
    """
    try:
        name = request.POST["name"]
        description = request.POST["description"]
        subcategory = request.POST["subcategory"]

        Catogory.objects.filter(id=id).update(
            name=name, description=description,  subcategory= subcategory)
        data = []
        get_data = Catogory.objects.filter()
        for i in get_data:
            abc = list(Subcatogory.objects.filter(id=i.subcategory_id))
            for j in abc:
                data.append({
                    "id": i.id,
                    "name": i.name,
                    "description": i.description,
                    "subcategory": j.name
                })
        messages.success(request, "update category data")
        return redirect('/index')
    except Exception as e:
        messages.success(request, "failed to update Category")
        return redirect('/index')



def addsubCategory(request):
    """
    :param request:
    :return:
    """
    try:
        abc = list(Subcatogory.objects.all())
        sddsd = []
        for i in abc:
            json_data = {
                "id": i.id,
                "name": i.name
            }
            sddsd.append(json_data)

        get_emp = []
        get_empl_data = Subcatogory.objects.filter()
        for i in get_empl_data:
            get_emp.append({
                "id": i.id,
                "name": i.name,
                "description": i.description,
            })
        return render(request, 'addsubcategory.html', context={"sddsd": sddsd, "get_emp": get_emp})
    except Exception as e:
        return render('/index')

def subCategory(request):
    """
    :param request:
    :return:
    """

    # try:
    name = request.POST["name"]
    description = request.POST["description"]

    catogory = Subcatogory.objects.create(name=name, description=description)
    catogory.save()

    get_category_data = Subcatogory.objects.filter()

    data = []
    for i in get_category_data:
        data.append({
            "id": i.id,
            "name": i.name,
            "description": i.description,
        })

    return redirect('/index')
    # except Exception as e:
    #     return redirect('/index')