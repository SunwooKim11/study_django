from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
topics =[
    {'id':1, 'title':'routing', 'body':'Routing is..'},
    {'id':2, 'title':'view', 'body':'view is..'},
    {'id':3, 'title':'Model', 'body':'Model is..'},
]
newId = 3
def HTMLTemplate(articleTag, id=None):
    global topics
    ol = ""
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    contextUI = ''
    if id!=None:
            contextUI = f"""
                    <li>
                    <form action="/delete/" method="post">
                        <input type="hidden" name="id" value={id}>
                        <input type="submit" value="delete">
                    </form>
                    </li>
                    <li><a href="/update/{id}">update</a></li>
            """
    
    htmltext = f"""
    <html>
        <body>
            <h1>Django</h1>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
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
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = int(request.POST['id']) # get id from POST
        print(id)
        # del topics[id] # delete topics[id] -> INDEX로 하는게 아니라 id로 하는것임
        # directory로 id가 설정되어있기 때문에, 다시 다 돌아서 새로 만들어주는 수 밖에 없다.
        newTopics = []
        for topic in topics:
            if topic['id'] != id:
                newTopics.append(topic)
        topics = newTopics
    return redirect("/")

@csrf_exempt        
def update(request, id):
    global topics
    tmp = {}
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                tmp = topic
                break
        print(tmp)
        article = f"""
            <form action="/update/{id}/" method="post">
            <p><input type="text" name="title" placeholder="title" value={tmp['title']}></p>
            <p><textarea name="body" placeholder="body" >{tmp['body']}</textarea></p>
            <p><input type="submit"></p>
        </form>
    """
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method =='POST':
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = request.POST['title']
                topic['body'] = request.POST['body']
                break
        return redirect("/read/"+str(id))


