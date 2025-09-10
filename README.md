# Ad Astra

A simple **Flask** web application. Can be used as a fun project to run locally or for **CI/CD** learning.

## Overview
The app displays a welcome page and a button. When button is clicked, a random quote from a Sci-Fi book is shown.
The quotes currently kept in the app "/quotes" route python dictionary. A few sample quotes are provided.
The project contains pytest test that can be used as a part of your CI/CD pipeline.

## Requirements
- python 3.12.3
- flask 3.2.1
- pytest 8.4.2
- pytest_playwright 0.7.1
- playwright 1.55.0
- requests 2.32.5
- bootstrap 5

## Installation
1. Clone repository
```bash
git clone https://github.com/TheTuna/Ad_Astra.git
cd Ad_Astra
```
2. Create and activate virtual environment
```bash
python3 -m venv <virtual_env_name>
sudo chmod +x <virtual_env_name>/bin/activate
source <virtual_env_name>/bin/activate
```
3. Install requirements
```bash
pip3 install -r requirements.txt
```
4. Run the app
```bash
export FLASK_APP=ci_site.py
flask run
```
5. Run tests
```bash
pytest -v
```

## License

MIT License. See LICENSE
