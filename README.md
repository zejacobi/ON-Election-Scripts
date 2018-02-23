[![Build Status](https://travis-ci.org/zejacobi/ON-Election-Scripts.svg?branch=master)](https://travis-ci.org/zejacobi/ON-Election-Scripts)

# Ontario Election Scripts
Scripts for parsing poll and other data for the Ontario election

# Methodology
* I'm extracting polling data from the major polling firms and parking it in JSON files, for later
  export to a database.
* I'm coding "416" as equivalent to Toronto and 905 as equivalent to GTA (even though these may
  no be exactly the same and it probably depends somewhat on individual pollsters definitions what
  is where.)

## Installing
* Install Python 3.5
* Create a virtual environment in the project folder with `virtualenv -p python3 venv`
* Activate the virtual environment with `source venv/bin/activate`
* Install packages with `pip install -r requirements.txt`


## Testing
From the top level directory: `python tests.py`

Remember to add all new tests to the `tests.py` file.

To run the unit tests with coverage, run
```bash
coverage run tests.py
coverage report
```