# Day 7 - extra stuff


Day 7 ? wait ! there was a day 7 ?

This is the hidden section for things not covered during the school ;-)

## Jupyter notebooks

Some of you probably use jupyter notebooks.
They are a great tool for data exploration and visualisation, as well as for documenting your analysis.
We don't recommend to use them for more than that though, keep your core analysis in `.py` files and packages, it makes it much easier to maintain and reuse.

To ease notebooks maintenance and review, we recommend to clear the output before pushing them to the repository. This will avoid add binary files such as images every time you rerun the notebook, and generally makes git diff much more readable:
```
pixi add nbconvert
jupyter nbconvert --clear-output --inplace notebook.ipynb
```

You may also use [reviewNb](https://www.reviewnb.com/) for pull request reviews.


## YAML and GitHub action linter

To validate your yaml file before pushing it into production and trying to debug with github error messages, there are third party tools that can do that for you:
- actionlint - https://github.com/rhysd/actionlintyamlls 
- https://github.com/redhat-developer/yaml-language-server
    - it also has a nice VSCode extension (and probably for other IDE) that will auto detect errors


## MyBinder

MyBinder is an open-source service that turns Git repositories into interactive computing environments. It allows users to run Jupyter notebooks, RStudio, and other tools in the cloud without local installation.

### Key Features
- **No Setup Required:** Access environments directly from a web browser.
- **Reproducibility:** Share consistent, pre-configured environments.
- **Collaboration:** Ideal for workshops, teaching, and team projects.
- **Multi-Language Support:** Compatible with Python, R, Julia, and more.

### How to Use
1. Host your notebooks and environment files (e.g., `requirements.txt`) on GitHub.
2. Generate a MyBinder link using the repository URL.
3. Share the link for instant access to a live environment.

### Example
Try 
```
https://mybinder.org/v2/gh/s3-school/pkoffee/main
```

In our case, it builds the environment thanks to the `Dockerfile` as pixi is too recent and not supported by mybinder. A `requirements.txt` or conda `environment.yml` [would be used to build the environment](https://mybinder.readthedocs.io/en/latest/examples/sample_repos.html#managing-languages).

### Resources
- [MyBinder Documentation](https://mybinder.org/)
- [Example Gallery](https://mybinder.org/examples)