from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, (photos,))

# dnn part
import keras
from keras.models import Model

model = keras.applications.VGG16(weights='imagenet', include_top=True)
feat_extractor = Model(inputs=model.input, outputs=model.get_layer("fc2").output)
feat_extractor.summary()


from app import routes
