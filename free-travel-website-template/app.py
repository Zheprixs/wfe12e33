from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for generating random pages
@app.route("/generate")
def generate():
    # List of pages to redirect to
    pages = ["Bali.html", "Bintan.html", "Jogja.html"]
    # Randomly select one page
    selected_page = random.choice(pages)
    # Redirect to the selected page
    return render_template(selected_page)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)