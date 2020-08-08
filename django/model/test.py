from keras.models import Sequential, Model
from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D, Dropout
from keras.layers import Input, concatenate
from keras.layers.advanced_activations import LeakyReLU, ReLU
from keras_contrib.layers.normalization.instancenormalization import InstanceNormalization
from keras.optimizers import Adam
from keras.models import model_from_json
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

file = open('C://Users//user//Desktop//jh//model//generator_final.json','r')
g_model = file.read()
file.close()
generator = model_from_json(g_model,custom_objects={'InstanceNormalization':InstanceNormalization})
generator.load_weights("C://Users//user//Desktop//jh//model//generator_final.h5")


s = sys.argv[1]
s="C:/Users/user/Desktop/jh/website"+s
image = cv2.imread(s)
image = cv2.resize(image, dsize=(128,128))
b,g,r = cv2.split(image)
image = cv2.merge([r,g,b])
image = image/127.5-1
image = image.reshape(1,128,128,3)

fig = plt.figure()
ax = plt.subplot(121)
ax.set_title('Image You Uploaded')
ax.imshow((((image)+1)*127.5).astype(np.uint8).reshape(128,128,3))
ax.axis('off')

ax = plt.subplot(122)
ax.set_title('Style Transferred Image')
ax.imshow(((generator.predict(image)+1)*127.5).astype(np.uint8).reshape(128,128,3))
ax.axis('off')
fig.savefig('C://Users//user//Desktop//jh//website//media//new.png')
plt.close()
print('/media/new.png') #해당 출력물을 view.py에 전달