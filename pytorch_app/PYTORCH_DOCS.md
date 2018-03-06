PyTorch Documentation for import and export functionality:

Models built in PyTorch can currently be saved in two formats:
- .pt format (torch.save)
- .proto format (torch.onnx.export)

Building the graph:

As of now, there is no official support for graph tracing (Except in onnx format). We can get the operations in a graph by back-tracing from the output variable's gradient function, all the way to the input. 

Problems:

-> A dummy input variable is required to perform graph tracing (Even for onnx format). This means that we need to know the size of the input if we need to generate the graph of the model. Problem is, torch's sequential models don't contain the input layer's shape.

-> Torch's '.pt' format saves the model along with the actual variables. The resnet-101 model's pt file is 170MB for instance.  

-> For importing, we first open the file, and then send it to the import functionality in the backend via Django. Problem is, .pt files are in a binary format, there is no human
readable format availabe. Python's default open function doesn't work, even in 'rb' mode for torch '.pt' files. We would need to use torch.load or pickle to open it.

Solutions:

-> Get the input shape from the user (Easier, Also necessary for onnx support) or Calculate a dummy shape by backtracing from the last layer. We only need a dummy input layer, and shape such that we get an integer shape size at the output.

-> 
