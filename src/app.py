from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/register')
def register():
    return render_template ('register.html')

@app.route('/login')
def login():
    return render_template ('login.html')


@app.route('/auth/register',methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        id = len(users) + 1

        new_user = {"name": name, "password": password}

        users[id] = new_user


    return render_template ('register.html')

if __name__ == '__main__':
    app.run(debug=True)