from unittest import result

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def helloworld():
    return '<h1>Hello World</h1>'

@app.route('/demo')
def demo():
    return render_template('demo.html')

# http://127.0.0.1:5000/demo1/Kishan
@app.route('/demo1/<name>')
def demo1(name):
    return render_template('demo1.html', hname=name)

#app.add_url_rule('/','name', name)
@app.route('/name')
def name():
    return '<h1>Hello I am Kishan Patel</h1>'

#http://127.0.0.1:5000/sum?a=50&b=10
@app.route('/sum')
def sum():
    a = request.args.get('a')
    b = request.args.get('b')
    sum = int(a) + int(b)
    return '<h1>Sum: '+ str(sum)+'</h1>'


@app.route('/data', methods=['POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        result = '''
                <h1>First name: {}</h1>
                <h1>Last name: {}</h1>
        '''
        return result.format(first_name, last_name)

    return 'No GET method allowed, Only POST method accepted.'


@app.route('/user')
def form():
    return '''
    <form method="POST" action="http://127.0.0.1:5000/data">
           <div><label>First Name: <input type="text" name="fname"></label></div><br>
           <div><label>Last Name: <input type="text" name="lname"></label></div><br>
           <input type="submit" value="Submit">
    </form>
    '''

if __name__ == '__main__':
    app.run()