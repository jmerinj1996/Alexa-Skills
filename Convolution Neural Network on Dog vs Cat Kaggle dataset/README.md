
Based off of Sentdex Tutorial at https://www.pythonprogramming.net/

A Convolutional Neural Network is structured something like this:

#### input layer --> convolution -->  pooling --> fully connected layer --> output layer

The convolution + pooling make up the hidden layers

Here we use TFLearn which is a high level abstraction layer for TensorFlow. The CNN has 5 hidden layers which has seen to increase the accuracy drastically.
#### Why do we need Abstraction?
* For simplicity of code
* The code becomes a lot less error prone

To install the latest stable version of TFLearn :
#### pip install tflearn
