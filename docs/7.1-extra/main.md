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

