from tensorflow import keras
model = keras.applications.resnet50.ResNet50(include_top=False, weights='imagenet', input_shape=(224,224,3), classes=5)
print(model.output)