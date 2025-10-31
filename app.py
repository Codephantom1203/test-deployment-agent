from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from my test deployment agent app!"

@app.route("/health")
def health():
    return {"status": "healthy", "message": "Deployment agent test app"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)' > app.py