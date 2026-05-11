# Import the Flask class from the flask library 
from flask import Flask 
  
# Create the Flask application object 
app = Flask(__name__) 
  
  
# ROUTE 1 – Home Page 
# Visit: http://127.0.0.1:5000/ 
@app.route('/') 
def home(): 
    return 'Welcome to Flask Class' 
  
  
# ROUTE 2 – About Page 
# Visit: http://127.0.0.1:5000/about 
@app.route('/about') 
def about(): 
    return 'This is About Page' 
  
  
# ROUTE 3 – Contact Page 
# Visit: http://127.0.0.1:5000/contact 
@app.route('/contact') 
def contact(): 
    return 'Contact Us Page' 
  
  
# ROUTE 4 – Dynamic Route (String) 
# Visit: http://127.0.0.1:5000/student/John 
# <name> is replaced by whatever the user types in the URL 
@app.route('/student/<name>') 
def student(name): 
    return f'Hello {name}, Welcome to Flask' 
  
  
# ROUTE 5 – Dynamic Route (Integer) 
# Visit: http://127.0.0.1:5000/square/5 
# <int:number> tells Flask to expect a whole number 
@app.route('/square/<int:number>') 
def square(number): 
    result = number * number 
    return f'Square is {result}' 

#Challenge – Create Your Own Route!
#1 
@app.route('/cube/<int:number>')
def cube(number):
    result = number * number * number
    return f'Cube is {result}'
#2
@app.route('/greet/<name>/<int:age>')
def greet(name, age):
    return f'Hello {name}, you are {age} years old!'
#3
@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f'Multiple value is {result}'

# Run the app with debug mode ON (shows errors while coding) 
if __name__ == '__main__': 
    app.run(debug=True) 