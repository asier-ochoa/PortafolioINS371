from flask import Flask
from routes.routes import routes

app = Flask(__name__)
app.testing = True

app.register_blueprint(routes)

app.run(debug=True)