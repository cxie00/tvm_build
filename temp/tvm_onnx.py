import onnx
import numpy as np
import tvm
from tvm import te
import tvm.relay as relay
import mlflow

# Load a previously converted model. This model was converted from skl to ONNX with Hummingbird.
onnx_model = mlflow.onnx.load_model("0/b81d20537a9345cf9126d7c8bdc7a2c6/artifacts/onnx_model")
ml_model = mlflow.onnx.Model.load("0/b81d20537a9345cf9126d7c8bdc7a2c6/artifacts/onnx_model")
input_example =  ml_model.load_input_example("0/b81d20537a9345cf9126d7c8bdc7a2c6/artifacts/onnx_model")
input_shape = input_example.shape
print(f'input_shape: {input_shape}')
print(f'input_shape type: {type(input_shape)}')

# Code below is from TVM ONNX example in their official docs 
# https://tvm.apache.org/docs/how_to/compile_models/from_onnx.html#compile-the-model-with-relay
target = "llvm"
input_name = "input_0"
shape_dict = {input_name: input_shape}

mod, params = relay.frontend.from_onnx(onnx_model, shape_dict, dtype='float64')
# print(mod)
# print(params)

# Gets stuck in create_executor
with tvm.transform.PassContext(opt_level=1):
    executor = relay.build_module.create_executor(
        "graph", mod, tvm.cpu(0), target, params
    ).evaluate()

dtype = "float64"
tvm_output = executor(tvm.nd.array(input_example.astype(dtype))).numpy()
    