from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # import requests
    # import json
    # api_request = requests.get('https://api.github.com/users?since=135')
    # api = json.loads(api_request.content)
    return render(request, 'home.html', {})


def search(request):
    import requests
    import json

    if request.method=='POST':
        text = request.POST['search'].replace(' ', '')
        if text != '':
            # user_request = requests.get("http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={"+user+"}&type=1&offset=0&total=true&limit=15")
            user_request = requests.get("https://musicapi.leanapp.cn/search?keywords="+text+"&type=1&limit=100")
            results = json.loads(user_request.content)
            results = results['result']['songs']
            lresult=[]
            # for j in results:
            #     if text[0]==j['name'][0]:
            #         lresult.append(j)
            return render(request, 'search.html', {'text':text, 'result':results, 'lenth':len(results)})

    return render(request, 'search.html', {'notfound':'please input'})

def creat(request):
    if request.method == 'POST':
        import requests
        import json
        juzi = request.POST['juzi'].replace(' ', '')
        res=[]
        for i in juzi:
            re = requests.get("https://musicapi.leanapp.cn/search?keywords="+i+"&type=1&limit=10")
            ree = json.loads(re.content)
            results = ree['result']['songs']
            # for j in results:
            #     if i != j.name[0]:
            #         pass
            res.append(results[0])

        return render(request, 'creat.html', {'juzi':juzi,'res':res})
    else:
        return render(request, 'creat.html', {})

def creat2(request):
    if request.method == 'POST':
        import requests
        import json
        import random
        juzi = request.POST['juzi'].replace(' ', '')
        res=[]
        for i in juzi:
            re = requests.get("https://musicapi.leanapp.cn/search?keywords="+i+"&type=1&limit=15")
            ree = json.loads(re.content)
            ree = ree['result']['songs']
            res.append(ree[random.randint(0,len(ree)-1)])

        return render(request, 'creat.html', {'juzi':juzi,'res':res})
    else:
        return render(request, 'creat.html', {})


def share_html(request):
    return render(request, 'share.html', {})


def share(request):
    request.encoding = 'utf-8'
    if 'id' in request.GET and request.method=='GET':
        # id = request.GET.get('id', default='110')
        id = request.GET['id']
        return HttpResponse(id)

def gethtml(request):
    return render(request, 'get.html')
