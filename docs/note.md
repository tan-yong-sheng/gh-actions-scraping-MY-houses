# Note

- [Set up conda environment](#set-up-environment)
  - [Manage dependency](#manage-dependency)
- [Add Python testing with pytest](#add-python-testing-with-pytest)
  - [Unit testing](#unit-testing)
  - [Integration testing](#integration-testing)
- [Documentation](#steps-to-create-documentation)
  - [Set up documentation](#set-up-documentation)
  - 

## Set up environment

1. Create a Conda Environment & Manage dependency

```
conda create -n gh-actions-scraping-MY-houses python=3.9
conda activate gh-actions-scraping-MY-houses
```

To install poetry in my conda environment
`conda install poetry`

To create a new poetry environment
`poetry init`

To activate poetry environment:
`poetry shell`

To add python packages recorded in requirements.txt into poetry environment
`poetry add $(awk -F '==' '{print $1}' requirements.txt)`

To add python packages recorded in requirements-dev.txt into poetry environment for development purpose:
`poetry add --group dev $(awk -F '==' '{print $1}' requirements-dev.txt)`

To make sure all the python packages installed in the poetry environment:
`poetry install`

To ensure reproducibility
`poetry lock`

To export the 
`conda env export | grep -v "^prefix: " > environment.yml`

See more here: https://medium.com/@silvinohenriqueteixeiramalta/conda-and-poetry-a-harmonious-fusion-8116895b6380

## Add Python Testing with pytest

### Unit testing

#### Initial configuration
- conftest.py
- pytest.ini

### fixture


### When to use mocking
![When to mock](https://enterprisecraftsmanship.com/images/2016/2016-11-15-2-1.png)
- https://enterprisecraftsmanship.com/posts/when-to-include-external-systems-into-testing-scope/

- https://chemaclass.medium.com/to-mock-or-not-to-mock-af995072b22e


### Integration testing

#### pytest-recording
- https://code.kiwi.com/articles/pytest-cassettes-forget-about-mocks-or-live-requests/

- https://til.simonwillison.net/pytest/pytest-recording-vcr


## Steps to create documentation
### Set up documentation
`sphinx-quickstart docs`

### convert rst file to md
- `pip install rst-to-sphinx`

- `rst2myst convert doc/**/*.rst`

### Install myst-parser to sphinx
- `pip install myst-parser`
- at doc/config.py, add `extensions=["myst-parser"]`

- `sphinx-build docs docs/_build`


### Add-on
#### Adjust image size
To adjust image size with myst-parser in sphinx documentation
- Activate myst extensions called "attrs_inline": https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-images-html
- https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html


## Documentation Testing with doctest

Documentation testing is useful in testing whether your code documentation is up-to-date. That’s quite some functionality, particularly in big projects: with just one command, you can check whether all examples are correct. See more [here](https://towardsdatascience.com/python-documentation-testing-with-doctest-the-easy-way-c024556313ca)

## CI/ CD with Github Actions
1. Deploy FastAPI to HuggingFace
- credentials - git login to Huggingface: https://huggingface.co/docs/huggingface_hub/en/quick-start
- Github actions to HuggingFace: https://huggingface.co/docs/hub/spaces-github-actions