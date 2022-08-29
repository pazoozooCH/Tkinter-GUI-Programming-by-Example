# tkinter by example

## Initial setup

- Install virtual env: `python -m pipenv install`
  - With `python --version` returning *3.9.6*
- Install pipenv for virtual env:
  - `python -m pipenv shell`
  - `python -m pipenv install --dev pipenv`
- Select corresponding python interpreter in IDE
  - Run a shell with out virtual env: `python -m pipenv shell` shows the virtual env name
  - The files are located in `~/.virtualenvs`

## Running scripts

- Either run a shell with `python -m pipenv shell`
  - Or use the Activate script for powershell, e.g.:
    `& c:/Users/Martin/.virtualenvs/python-tkinter-by-example-dJI9a59B/Scripts/Activate.ps1`
- Run hello world: `python Chapter01/Ch1/ch1-1.py`