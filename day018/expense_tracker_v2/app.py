from flask import Flask, render_template
from expense.routes import expense_bp

app = Flask(__name__)
app.secret_key = "dev-secret-key"
app.register_blueprint(expense_bp)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5500)