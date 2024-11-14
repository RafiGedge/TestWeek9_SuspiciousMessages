from flask import Flask
from blueprints import app_bp

app = Flask(__name__)

app.register_blueprint(app_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
