from flask import Flask, render_template, redirect, request, url_for # url for helps with the linking of dynamic pages
app = Flask(__name__)

User = [] 
# python list, this needs to be defined in the route

# user the app.route decorator to define a route/endpoint
@app.route('/')
def Users():
    return render_template('index.html', title='Home')

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("signup.html")
 
@app.route("/confirmation", methods=["POST"])
def form():
 
    req = request.form
    username = req.get("username")
    email = req.get("email")
    password = req.get("password")
    
    User.append(f"Your Username: {username}\n"
                f"\nEmail is: {email}\n"
                   f"Your Password: {password}\n")
 
    submission = (f"Username is:{username}\n"
                  f"Email is: {email}\n"
                  f"password is: {password}\n")
 
    print(submission)


    return render_template("confirmation.html", User=User, username=username, email=email, password=password)


if __name__ == '__main__':
    app.run(debug=True)



