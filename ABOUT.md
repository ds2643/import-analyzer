# About this Project

This document describes design and assumptions important in evaluating the efficacy of this tool.

## Assumptions

Several latent assumptions hinder real-world use of this tool.

- AST parsing is limited to Python files, so Python code embedded in Jupyter Notebooks is ignored. This limitation is problematic because Jupyter is a popular tool among data scientists, who are frequent users of Tensorflow.

- The tool isn't backwards compatible with Python2 codebases, as made clear by this example:
```
vagrant@vagrant:/vagrant$ a run tensorflow models
Traceback (most recent call last):
  File "/usr/lib/python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  [...]
  File "/usr/lib/python3.7/ast.py", line 35, in parse
    return compile(source, filename, mode, PyCF_ONLY_AST)
  File "/tmp/tmpmow8rr2c/models/research/cognitive_planning/viz_active_vision_dataset_main.py", line 98
    print world
              ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(world)?
```

- The CLI does not currently support searching other branches besides the default (e.g., `main`).

- The tool ignores the problem of searching large numbers of repositories on GitHub.

- The tool has only been tested with around 5 repositories, so edge cases have not been fleshed out.
	- The tool hasn't been tested on large codebases.
	- Examples are cherry picked!

Further limitations are outlined in Github Issues.

## Example Repositories

The following repositories serve as test examples:

| Organization  | Repository           |
|---------------|----------------------|
| aymericdamien | TensorFlow-Examples  |
| ibab          | tensorflow-wavenet   |
| davidsandberg | facenet              |
| golbin        | TensorFlow-Tutorials |

The output fails to consider `import tensorflow as tf`, as outlined in a Github Issue, but the output is still illustrative of the tool's current functionality:

```bash
vagrant@vagrant:/vagrant$ a run golbin TensorFlow-Tutorials
tensorflow.examples.tutorials.mnist.input_data    8
tensorflow.python.framework.graph_util            1
tensorflow.python.framework.tensor_shape          1
tensorflow.python.platform.gfile                  1
tensorflow.python.util.compat                     1
```

## How it Works

This tool clones a repository to a temporary directory. Next, Python files are recursively discovered. Each module is parsed as an abstract syntax tree, which is searched programmatically for imports. The imports are collapsed into a dataframe, and number of occurrences is printed to console in minimal, tabulated form.


## Examples

Here are some examples of the tool being used:

```
vagrant@vagrant:/vagrant$ a run davidsandberg facenet
tensorflow.python.ops.data_flow_ops       3
tensorflow.python.ops.array_ops           3
tensorflow.python.ops.control_flow_ops    3
tensorflow.python.platform.gfile          2
tensorflow.python.framework.ops           1
tensorflow.python.framework.graph_util    1
tensorflow.python.training.training       1
```

```
vagrant@vagrant:/vagrant$ a run aymericdamien TensorFlow-Examples
tensorflow.examples.tutorials.mnist.input_data                                                      46
tensorflow.contrib.rnn                                                                               4
tensorflow.contrib.boosted_trees.estimator_batch.estimator.GradientBoostedDecisionTreeClassifier     2
tensorflow.contrib.boosted_trees.proto.learner_pb2                                                   2
tensorflow.contrib.tensor_forest.python.tensor_forest                                                2
tensorflow.python.ops.resources                                                                      2
tensorflow.contrib.factorization.KMeans                                                              2
```
