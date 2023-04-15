from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
topics =[
    {'id':1, 'title':'routing', 'body':'Routing is..'},
    {'id':2, 'title':'view', 'body':'view is..'},
    {'id':3, 'title':'Model', 'body':'Model is..'},
]
newId = 3
def HTMLTemplate(articleTag):
    global topics
    ol = ""
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    htmltext = f"""
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
        <a href="/create/">create</a>
    </body>
    </html>
    """
    return htmltext



def index(request):
    article = """
        <h2>Welcome</h2>
        Hello, Django
    """
    return HttpResponse(HTMLTemplate(article))
    # return HttpResponse('index')

@csrf_exempt
def create(request):
    global newId, topics
    if request.method =='GET':
        article = """
                <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        """
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newId += 1
        newTopic = {'id':newId, 'title':title, 'body':body}
        topics.append(newTopic)
        return redirect("/read/"+str(newId))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))