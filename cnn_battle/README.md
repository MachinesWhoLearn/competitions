# Battle of the Nets

A performance comparison of LeNet, VGGNet, and The All Convolutional Net architectures on CIFAR-10 implemented using Keras.

Any parameters not explicitely specified in the papers you are free to set on your own. Outdated implementations (like using a sigmoidal activation function between layers) may be replaced with more modern implementations (like ReLU). It's also possible that Keras doesn't have the functionality used in the paper. In that case approximate with a different function [or implement the missing function on your own and submit a pull request :-)]. Specific net comments below.

##LeNet
Generalize to work with RGB images. Feel free to change or simplify aspects of the network that were designed specifically with handwritten digit recognition in mind.

## VGGNet
Use ConvNet Configuration B or C as a base model. Notice that the input and output sizes in the paper (224\*224\*3 and 1000\*1) is different from CIFAR-10's inputs and outputs (32\*32\*3 and 10\*1), so you won't be able to emulate the configuration exactly. But try to preserve the spirit of the architecture (hint: go deep).

## All Convolutional Net
Replace the pooling layers using option (2). Use Model A, B, or C as a base model.
