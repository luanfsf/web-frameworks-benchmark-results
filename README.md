# Python Template

### Index
* [Index](#Index)
* [Description](#Description)
* [Structure](#Structure)
* [Requirementes](#Requirements)
* [Installation](#Installation)
* [Running](#Running)
* [Testing](#Testing)
* [Developing](#Developing)


### Description
Simple template to create Python apps.

### Structure
Main files and directories structure.
````shell
.
├── .coveragerc			| Configuration for coverage.
├── .env.example		| Example of a .end file.
├── .pre-commit-config.yaml	| Pre-commit configuration.
├── Pipfile			| Pipenv configuration for environment and dependencies.
├── tasks/			| Invoke tasks directory for running, developing and testing.  
├── template/			| Main app directory.
└── tests/			| Tests directory.
````

### Requirementes
* [Python](https://www.python.org/downloads) - 3.8+
* [Pypenv](https://github.com/pypa/pipenv)

Optional
* [Pyenv](https://github.com/pyenv/pyenv)

### Installation
```shell
$ pip install pipenv && pipenv install && pipenv install --dev
  ```

### Running
* Running template
```shell
$ invoke template
  ```

### Testing
> Tests are run using Python's unittest

* Run all tests
```shell
$ invoke test
```
* Run coverage
```shell
$ invoke test.coverage
```

### Developing
* Format code 
```shell
$ invoke dev.black
```