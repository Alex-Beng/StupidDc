from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, (photos,))



from app import routes
