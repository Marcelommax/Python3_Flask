import views
from flask import Flask

   
def create_app():
    app = Flask(__name__)
    views.init_app(app)
    return app
    
    
# Variavel de ambiente de desenvolvimento   
# export FLASK_ENV=development
   
   
