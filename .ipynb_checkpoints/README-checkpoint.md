# BigModParams

BigModParams is a Python package designed for helping you optomize the parameters you use to train or fine-tune large generative AI models. This package provides utilities and functions to efficiently manage and manipulate large-scale model parameters.  

## 

## Installation

You can install the package using pip:

```
pip install bigmodparams
```

## Usage

Here's a simple example of how to use the package:

```python
from bigmodparams import example_function

print(example_function())
```

## Features

Current:

- Model Size Reduction: Theoretically, you can reduce the size of a generative AI model to almost nothing (removing parameters), but as long as the model is the same structure, you can still determine what parameter changes improve your fine-tuning efforts.  By applying this to the model before starting a hyperparameter search, you can significantly reduce the time it takes to conduct your search.
- Supports popular fine-tuning libraries: We will start with LoRA, integrating the hyperparameter search feature directly with the LoRA package. We will identify additional packages to integrate with and add those soon as well!
- Detect and Apply Quantization: The package will automatically detect the quantization level currently applied to the generative AI model you are working with, and then allow you to apply anything less than that.
- Integrate with Huggingface Transformers: Allows you to use any model on Huggingface in your hyperparameter search.  All you have to know is the company and model name on HuggingFace, and this package will do the rest!
- Grid Search: Allows you to conduct Grid Search will a variety of options related to the other features mentioned!

Near Future:

- Select more typical hyperparameter search strategies: expanded Grid Search, Random Search, Bayesian Optimization
- Integrate with Accelerate: Automatic detection of environment, application of optimizations based on what is detected. Optimize for GPUs, any potential parallel evaluation, if Nvidia Ampere (or better) detected use flash attention to speed up training 3X automagically.  Based on the environment, can suggest other optimizations, like quantization, and explain the trade-offs for each approach.
- Optimization Wizard: Provide a wizard that helps the user determine how to reduce their hyperparameters options before starting the search
- Proxy Tasks: Can reduce the size of the data automatically to make training/fine-tuning go faster.
- Training Optimizations: Automatically detect the lowest level of training steps or epochs needed for hyperparameter search to be successful
- Early Stopping Detection: Will determine if early stopping can help speed up the process and implement it.
- Batch budgeting: starts many configurations with a smaller batch, then progressively increases the batches for promising ones


## Contributing

We welcome contributions to BigModParams! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.