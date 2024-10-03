#app/app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

#Simulated database (vulnerable to SQL injection)
users = {
    "admin": "password123",
    "user": "mypassword"
}

@app.route('/')
def index():
    return render_template_string('''
        <h1>Login Page</h1>
        <form method="POST" action="/login">
            Username: <input type="text" name="username"></br>
            Password: <input type="password" name="password"></br>
            <button type="submit">Login</button>
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Vulnerable to SQL injection attack!
    if username in users and users[username] == password:
        return "Login successful!"
    return "Invalid credentials!"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)