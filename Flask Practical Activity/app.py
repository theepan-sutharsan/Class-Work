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
  
  
# Run the app with debug mode ON (shows errors while coding) 
if __name__ == '__main__': 
    app.run(debug=True) 