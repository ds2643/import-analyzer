# Import Analyzer

This utility counts `import`s of the `tensorflow` module within Python codebases hosted remotely within public GitHub repositories.

The tool analyzes one repository at a time.

## Use
This section describes how to use the tool.

### Virtual Machine

Vagrant serves the purpose of virtual machine (VM) provisioning in order to maximize portability among development environments and to reduce overhead associated with environmental configuration.

Vagrant uses an infrastructure-as-code approach, where the VM is described declaratively in the `Vagrantfile` stored at root.

The virtual machine is configured with filesystem transparency with respect to the host (i.e., your machine), meaning changes made to the local filesystem are reflected on the VM and vise versa. In other words, any changes you make to the repository will persist on the host.

All necessary dependencies (e.g., Python) are included in a dynamically built Linux virtual machine.

#### Requirements

Development dependencies are limited to [vagrant](https://www.vagrantup.com) and [virtualbox](https://www.virtualbox.org) 6.1. Both required to be installed on the host machine.

#### Virtual Machine Provisioning and Use

This section highlights some useful Vagrant commands. **All commands are intended to run from repository root**. For a more exhaustive list, see the official [documentation](https://www.vagrantup.com/docs/cli) or simply run `vagrant` without any arguments.

Provision a VM using VirtualBox as the default VM manager by running the following command from repository root:

```bash
vagrant up  # Installs dependencies as specified in `bootstrap.sh`.
```

Once the VM is booted, connect as follows:

```bash
vagrant ssh
exit  # disconnect from session, leaving machine running
```

Turn off the VM:

```bash
vagrant halt
```

Destroy the VM:

```bash
vagrant destroy -f
```

### Installing project dependencies

An alias installs Python dependencies when run from repository root:

```bash
i
```

### Running the tool

The tool's functionality is exposed via an `Invoke` interface, aliased as `a` to reduce typing necessary to leverage the necessary dependency manager (`pipenv`).

```bash
a --list
# Available tasks:
#
#  run    Run repository analysis.
#  test   Run repository tests.
```

Run `a --help [task]` to see which arguments are expected.

#### Count `tensorflow` Imports

This example uses a repository featuring `tensorflow` imports in Python code. The arguments are passed explicitly, but may also be referenced positionally:

```bash
a run --organization=aymericdamien --repository=TensorFlow-Examples

# tensorflow.examples.tutorials.mnist.input_data                                                      46
# tensorflow.contrib.rnn                                                                               4
# tensorflow.contrib.boosted_trees.estimator_batch.estimator.GradientBoostedDecisionTreeClassifier     2
# tensorflow.contrib.boosted_trees.proto.learner_pb2                                                   2
# tensorflow.contrib.tensor_forest.python.tensor_forest                                                2
# tensorflow.python.ops.resources                                                                      2
# tensorflow.contrib.factorization.KMeans                                                              2
```

The output shows modules sorted by count in the specified repository.

#### Run tests

Run repository tests as follows:

```bash
a test
```
