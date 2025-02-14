from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return "Hello, Flask Web Server running in Docker! by jatin dayal it is running on port 5000"
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
