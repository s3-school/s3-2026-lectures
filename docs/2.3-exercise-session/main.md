# Project setup and collaborative programming

The goal of this hands-on session is to practice using pixi for manage environments, and git and github to collaborate on a project. We will work on the [`pkoffee`](https://github.com/s3-school/pkoffee) repository, trying to refactor it into a high quality analysis project.

The session is divided in exercises, that gradually improve the quality of the `pkoffee` project. It is not expected that we complete all the exercises during the session! The goal is to practice programming with a group of people on a pixi managed project, not to focus on `python` implementation details. At the end of the session, we will have a look at an implementation that solves all the exercises. This implementation will be pushed to the `pkoffee` repository, and will be used as a basis for the next lectures so we all continue with the same state.


## Exercise 1: Set up a working environment
1. Fork the [`pkoffee`](https://github.com/s3-school/pkoffee) repository, then clone it on your laptop.
2. Use `pixi` to initialize a workspace
3. Add to the workspace the platforms you would like support: `linux-64`, `osx-64`, `osx-arm64`, ...?
4. Add the python packages required by the `pkoffee` script.
   Can you run the `pkoffee` analysis with `pixi run python main.py`?
5. Add features and environment so you can work with python versions 3.12, 3.13 and 3.14
6. Add an environment for any other development tool that you feel like using while coding: jupyter notebooks, `ipython`, ...
7. Add a package section to your pixi manifest for `pkoffee`. Move the dependencies in the package run-time dependencies and add the local `pkoffee` package to your workspace dependencies. Check that you can build a conda package with `pixi build`. Can you still run `pkoffee` analysis?

## Exercise 2: Configure your preferred IDE to work with your pixi project
1. Install the IDE of your choice and open your `pkoffee` directory.
   If you don't have an IDE in mind, you can test [`vscodium`](https://vscodium.com/) and see if you like it.
2. Configure your IDE to help you be efficient while programming:
    - python syntax highlighting and syntax checking
    - code completion and code navigation aware of the pixi managed dependencies
    - docstring generation from code and type hints
    - code formatting
    - automatic refactoring


## Exercise 3: collaborative refactoring
1. Form groups of at least 3 person: this will be your development team for this session
2. Together, lay out the organization of your code base
    - what is the `pkoffee` project even doing?
    - what concepts would make relevant abstractions?
    - How will you implement those abstractions? What are the interfaces between these abstractions?
3. Split the refactoring work that you want to perform with your team. Do you have all information to implement your part?
4. Create a branch for your development. Add your teammates forks as a remote so you can make your work available to them.
5. Start coding with your team! Implement a feature and push it on the remotes, merge regularly and keep updated with your group.

!!! tip "Don't put off until tomorrow what you can do today"

    Documentation and other metadata like python's type hints are easier to write when you have the implementation details in mind!

!!! tip "Don't wait until all your changes are implemented and merged to test"

    Finding bugs and solving issues is more difficult if several issues occurs simultaneously. Test often that your code is still working!


## Exercise 4: Command line interface
1. The initial `pkoffee` implementation had hardcoded paths for input data and output figures. Can you let the user define them?
2. Can you make other hard-coded values command line arguments?
3. Add a script section to your `pyproject.toml` to propose a command line tool to your users

## Exercise 5: Error handling/reporting
Some of your functions may fail in case of unexpected or invalid input. Should you raise an error in those cases? When yes, it is recommended to define your own error types that inherit python's built-in exceptions, so you can make your errors informative and easily selectable for others.

## Exercise 6: Control your data type and precision
`pkoffee` used `pandas` to read the `csv` data, then `numpy` arrays to fit the models using `scipy`. Do you know the precise type of those arrays? What precision is used for the operations?  
For computing intensive libraries, data and computing operations must be controlled as they can have a big impact on results, but also computing time. Can you force the usage of `float32` throughout `pkoffee`?  
Can you include this information in your type hints so type checker can help you find if your data type is preserved?

## Exercise 7: Logging
We will soon deploy `pkoffee` on a data center, where it will run on distributed machines which don't have a screen attached. Can you add [logging](https://docs.python.org/3/library/logging.html) so that we can follow what happens for each execution?

Direct usage of `print` statement are discouraged in favor of logging (which can go to standard output if no file is specified). Do you have any `print` statement you can change for logging?

## Exercise 8: Make visualization tools optional
We are deploying `pkoffee` on a computing cluster, but there is one issue: the computing nodes don't have a graphical interface, so plotting packages can't be installed. We need to make the plotting part of `pkoffee` "optional", so we can run the analysis without requiring it.

1. Factorize the plotting functionality in one module, or a few modules in a sub-repository
2. Re-organize your entry-point function to execute 2 commands: one for fitting models to the data, one to use models for making plots
3. Move the `import` of your visualization module into the "visualization path" of your script (your "plot" command)
   "Dynamic" import are usually not recommended. A cleaner solution would be to split `pkoffee` into 2 projects: one project for analysis and one for plotting, however this is a bit out of scope for this school.
4. You can now fit models and plot models, but not plot your fitted models. Implement model saving/loading to file to a simple format (for instance json or toml).
5. At the end of your analyze command: save your fitted models to file. At the beginning of your plotting command: load saved models to make predictions.
