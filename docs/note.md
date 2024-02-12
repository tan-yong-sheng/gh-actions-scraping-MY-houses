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

1. Create a Conda Environment

```
conda create -n gh-actions-scraping-MY-houses python=3.9
conda activate gh-actions-scraping-MY-houses
```

`conda install poetry`

`poetry init`

`poetry lock`

`conda env export | grep -v "^prefix: " > environment.yml`

See more here: https://medium.com/@silvinohenriqueteixeiramalta/conda-and-poetry-a-harmonious-fusion-8116895b6380


### Manage dependency

`poetry add $(awk -F '==' '{print $1}' requirements.txt)`

To update 
`poetry add --group dev $(awk -F '==' '{print $1}' requirements-dev.txt)`

1. Deploy FastAPI to HuggingFace
- credentials - git login to Huggingface: https://huggingface.co/docs/huggingface_hub/en/quick-start
- Github actions to HuggingFace: https://huggingface.co/docs/hub/spaces-github-actions

2. To adjust image size with myst-parser in sphinx documentation
- Activate myst extensions called "attrs_inline": https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-images-html
- https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html

## Add Python Testing with pytest

### Unit testing
- 

### Integration testing
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

