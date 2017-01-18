#EXPLANATION OF CODE 
This README.md only explains how to the codes in .prototxt files work. If you like to make these code run, please
attach the right data path into layer definition and prepare data in the right format 

### mnist_siamese_train_test.prototxt
In order to be able to train siamese network which has 2 sub-nets with [identical weights](http://stats.stackexchange.com/questions/154652/how-does-the-back-propagation-work-in-a-siamese-neural-network)

1. We first added a layer right before data layer to slice image pair into 2 individual images 
2. We have to name the parameters in each layer so that it can share parameters with corresponding layer 
 
