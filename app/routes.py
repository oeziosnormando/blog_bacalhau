from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Oézios'}
    return '''
<html>
    <head>
        <title>Home page Blog Bacalhau</title>

    </head>
    <body>
        <h1> Hello, ''' + user['username'] + '''!</h1>
    
    </body>

</html>'''
