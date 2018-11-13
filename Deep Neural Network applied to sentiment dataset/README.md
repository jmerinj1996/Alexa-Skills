A deep neural network as far as I understand it, is a neural network with more than one hidden layer.
There are certain challenges we face in neural networks, hence it's safe to say it is not as simple as a Support Vector Machine
* The first reason for this is that the optimization graph of a neural network is not as simple as an SVM. SVM has convex optimization.
* Secondly, unlike SVM in which we had to optimize only w and b, here we have a lot of unique weights to optimize
* Finally, in order for a neural network to work efficiently, we need a lot and I mean a looot of data

#### Tensorflow
This would be a good time to introduce y'all to Tensorflow- a matrix/array manipulation library
A Tensor is a array like object.(If you can convert any problem to a function on an array, you can most likely manipulate it using tensorflow)
We will be doing 2 things when we create a neural network using Tensorflow: 

1. We will build a computation graph
2. We will build a session

We are creating a simple feed-forward neural network

#### Feed-forward + Backward propagation = 1 epoch

#### Natural Language Processing of sentiment data
Lets address the more obvious issue. The dataset is word data/strings
1. We need to first convert it to numerical form
2. We need to send the same length vector input everytime into our neural network

creating_featuresets.py helps us get the data into the required format 
sentiment_neural_network.py contains the actual TensorFlow code

#### Note:
It you get a MemoryError, it's most likely you've run out of CPU ram

## Installation
####  pip install tensorflow
####  pip install nltk 
#### > import nltk
#### > nltk.download()
