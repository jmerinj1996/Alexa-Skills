# Convolution Neural Network on Dog vs Cat Kaggle dataset
import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm
import matplotlib.pyplot as plt

TRAINING_DIR = 'DIRECTORY_TO_TRAIN_FOLDER'
TESTING_DIR = 'DIRECTORY_TO_TEST_FOLDER'
IMG_SIZE = 50
learning_rate = 1e-3

MODEL_NAME = 'dogsandcats-{}-{}.model'.format(learning_rate,'2conv-basic')

#extract the labels from the name of the image
def extract_label(img):
    word_label = img.split('.')[0]
    if word_label == 'cat':
        return [1,0]
    elif word_label == 'dog':
        return [0,1]

#place training image and label inside a list
def create_train_data():
    training_data = []
    for img in tqdm(os.listdir(TRAINING_DIR)):
        label = extract_label(img)
        path = os.path.join(TRAINING_DIR, img)
        img = cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE),(IMG_SIZE, IMG_SIZE ))
        training_data.append([np.array(img), np.array(label)])
    shuffle(training_data)
    np.save('train_data.npy', training_data)
#this function has to be run only once
#create_train_data()
train_data = np.load('train_data.npy')


#place testing image and label inside a list
def create_test_data():
    testing_data = []
    for img in tqdm(os.listdir(TESTING_DIR)):
        path = os.path.join(TESTING_DIR, img)
        img_id = img.split('.')[0]
        img =  img = cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE),(IMG_SIZE, IMG_SIZE ))
        testing_data.append([np.array(img), np.array(img_id)])
    shuffle(testing_data)
    np.save('test_data.npy', testing_data)

#this function has to be run only once
#create_test_data()
test_data = np.load('test_data.npy')

#5 layered convolutional neural network
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tensorflow as tf
tf.reset_default_graph()

cnn = input_data(shape = [None, IMG_SIZE, IMG_SIZE, 1], name = 'input')

cnn = conv_2d(cnn, 32, 5, activation = 'relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 64, 5, activation = 'relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 128, 5, activation = 'relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 64, 5, activation = 'relu')
cnn = max_pool_2d(cnn, 5)

cnn = conv_2d(cnn, 32, 5, activation = 'relu')
cnn = max_pool_2d(cnn, 5)

#fully connected layer
cnn = fully_connected(cnn, 1024, activation = 'relu')
cnn = dropout(cnn, 0.8)

#output layer
cnn = fully_connected(cnn, 2, activation = 'softmax' )
cnn = regression(cnn, optimizer = 'adam', learning_rate = learning_rate, loss = 'categorical_crossentropy', name = 'targets')

model = tflearn.DNN(cnn, tensorboard_dir = 'log')


train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1, IMG_SIZE, IMG_SIZE,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE, IMG_SIZE,1)
test_y = [i[1] for i in test]

if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    print('Model Loaded!!')
else:
    model.fit({'input': X}, {'targets': Y}, n_epoch=3, validation_set=({'input': test_x}, {'targets': test_y}),snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
    model.save(MODEL_NAME)

#visualize test cases
for num, data in enumerate(test_data[:12]):
    img_id = data[1]
    img = data[0]

    fig = plt.figure()
    y = fig.add_subplot(3, 4, num+1)
    orig = img
    data = img.reshape(IMG_SIZE, IMG_SIZE, 1)
    model_predict = model.predict([data])[0]

    if np.argmax(model_predict) == 1: word_label = 'Dog'
    else: word_label = 'Cat'

    y.imshow(orig, cmap = 'gray')
    plt.title(word_label)
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)
plt.show()
