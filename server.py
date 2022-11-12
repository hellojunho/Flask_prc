from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id' : 1, 'title' : 'html', 'body' : 'html is ...'},
    {'id' : 2, 'title' : 'CSS', 'body' : 'CSS is ...'},
    {'id' : 3, 'title' : 'javascript', 'body' : 'javascript is ...'},
] 


def template(contents, content):
    return  f'''
        <!DOCTYPE html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {contents}
                </ol>
                {content}
                <ul>
                    <li><a href="/create/">create</a></li>
                </ul>
            </body>
        </html>
        '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')


@app.route('/read/<int:id>/')
def read(id):
    title=''
    body=''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    print(title, body)
    return  template(getContents(), f'<h2>{title}</h2>{body}')

@app.route('/create/')
def create():
    content = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="input text on title..."></p>
            <p><textarea name="body" placeholder="input text on body..."></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    '''
    return template(getContents(), content)



app.run(port=5000, debug=True)