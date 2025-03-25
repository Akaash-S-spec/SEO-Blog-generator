from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Route to serve the index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask server
    app.run(debug=True, port=5500)
