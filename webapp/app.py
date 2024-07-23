from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)

def load_common_passwords():
    with open('10-million-password-list-top-1000.txt', 'r') as file:
        common_passwords = file.read().splitlines()
    return common_passwords

common_passwords = load_common_passwords()

def is_password_safe(password):
    min_length = 10
    if len(password) < min_length:
        return False

    if not all(32 <= ord(char) <= 126 for char in password):
        return False

    if password in common_passwords:
        return False

    return True

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = request.form['password']
        if not is_password_safe(password):
            flash('Password is not safe. Please try again.')
            return redirect(url_for('home'))
        return redirect(url_for('welcome', password=password))
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    password = request.args.get('password')
    return render_template('welcome.html', password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
