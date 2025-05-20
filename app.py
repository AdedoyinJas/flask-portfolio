# Import required Flask modules
from flask import Flask, render_template, request, flash, redirect, url_for

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'hello'  # Needed for flashing messages

# Sample list of projects to display on homepage
projects = [
    {
        "title": "E-commerce Website",
        "description": "Built using Django and integrated payment gateway.",
        "link": "https://github.com/AdedoyinJas/E-commerce-APP"
    }]

# Home route — also handles contact form POST
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # For now, just flash a message (normally you'd send/store this)
        flash(f"Thank you {name}, I will get back to you soon!")

    # Pass project data to template
    return render_template('index.html', projects=projects)

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
