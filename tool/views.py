from django.shortcuts import render,redirect

# Create your views here.
from .models import Info

def title_list(request):
    title_content = Info.objects.all()
    return render(request,'title_list.html',{'titles':title_content})

def make_title(request):
    title_content = Info.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        info = Info(title=title)
        info.save()
        return render(request,'title_list.html',{'titles':title_content})
    return render(request,'make_title.html')

def delete_title(request,title_number):
    document = Info.objects.filter(number=int(title_number))
    document.delete()
    return redirect('/')

def get_details(request,title_number):
    document = Info.objects.filter(number=int(title_number))
    for each in document:
        titles = each
    for each in document:
        contents = each.content
    return render(request, 'get_details.html',{'titles':titles,'contents':contents})

def make_content(request,title_number):
    title_number = title_number
    document = Info.objects.filter(number=int(title_number))
    for each in document:
        content_list = each.content
    if request.method == 'POST':
        question = request.POST.get('question')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        option_C = request.POST.get('option_C')
        option_D = request.POST.get('option_D')
        new_list=[]
        new_list.append(question)
        new_list.append(option_A)
        new_list.append(option_B)
        new_list.append(option_C)
        new_list.append(option_D)
        content_list.append(new_list)
        # 实例化对象
        text = document.update_one(content=content_list)
        # 调用save方法保存数据
        #text.save()
        #为get_details方法
        document = Info.objects.filter(number=int(title_number))
        for each in document:
            titles = each
        for each in document:
            contents = each.content
        return render(request, 'get_details.html',{'titles':titles,'contents':contents})
    return render(request, 'make_content.html',{'title_number':title_number})

def delete_content(request,title_number):
    text = Info.objects.filter(number=int(title_number))
    text.delete()
    return redirect('/')
