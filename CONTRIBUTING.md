

`poetry add $(awk -F '==' '{print $1}' requirements.txt)`

To update 
`poetry add --group dev $(awk -F '==' '{print $1}' requirements.txt)`

1. Deploy FastAPI to HuggingFace
- credentials - git login to Huggingface: https://huggingface.co/docs/huggingface_hub/en/quick-start
- Github actions to HuggingFace: https://huggingface.co/docs/hub/spaces-github-actions

2. To adjust image size with myst-parser in sphinx documentation
- Activate myst extensions called "attrs_inline": https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-images-html
- https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html


# Steps to create documentation
## Set up documentation
sphinx-quickstart doc

## convert rst file to md
- `pip install rst-to-sphinx`

- `rst2myst convert doc/**/*.rst`

## Install myst-parser to sphinx
- `pip install myst-parser`
- at doc/config.py, add `extensions=["myst-parser"]`

- `sphinx-build docs docs/_build`

