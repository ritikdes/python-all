from flask import Flask, render_template
from todo.routes import todo_bp

app = Flask(__name__)
app.secret_key = "dev-secret-key"
app.register_blueprint(todo_bp)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=(True))