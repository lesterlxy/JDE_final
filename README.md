# JDE_final

Final project for the JDE course by Generation

## Instructions

- Copy the `.env.example` file to `.env` and fill in the variables
  - `URI_PG` is the template for your postgresql server URI
  - Kaggle credentials seem to be optional as I could download without them, but you can fill it in just in case
- Run `nhl_etl.ipynb`
  - Refer to **FAQ** if you need an environment or packages (e.g. when not using anaconda which should have everything installed)

## FAQ

### How to install venv?

- Open terminal in project folder
- Create the venv at `.venv` using command `python -m venv ./.venv`
- Activate the venv using command `./.venv/Scripts/activate.bat` or `./.venv/Scripts/Activate.ps1` depending on shell
- Install packages using command `pip install -r requirements.txt`

### How to activate venv in VS Code?

- Select your venv in the top right corner of the UI
