from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '12345'

    from app.papers.routes import papers_bp
    app.register_blueprint(papers_bp)

    return app
