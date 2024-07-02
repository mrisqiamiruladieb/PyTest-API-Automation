# PyTest API Automation

## Pre-requisites
- *Install PyTest module* in **cmd/terminal**:
  - **Run :** `pip install pytest`
- Check installation
  - `pytest --help` or `py -m pip list`

## How to Run the PyTest
- **Create** a file *containing* function and assert test code
- **Run** the file in *cmd/terminal* :
  - `pytest path/to_file.py`
  - Print to console : `pytest -s path/to_file.py` ([References](https://stackoverflow.com/questions/24617397/how-do-i-print-to-console-in-pytest))

## Create an example of a GET request
- Create file **get_list_users.py**
- Import required **libraries**
- Code ([References 1](https://www.geeksforgeeks.org/response-json-python-requests/), [References 2](https://medium.com/@qebuzzz/validating-and-asserting-responses-in-python-requests-14b40908327a)) and **run**
  
## Validate JSON Schema Response Body
- Configuring **files** to make *requests*
- Import required **libraries**
- **Create** a json schema response body *file/variable* to verify using [the Helper](https://github.com/mrisqiamiruladieb/REST-Assured-Java-Part-1/blob/master/README.md#helper)
- Code ([References](https://builtin.com/software-engineering-perspectives/python-json-schema)) and *run*

## Issues and Solutions
- Errors/warnings when executing **the requests**
  - ***Error/warning messages :*** RequestsDependencyWarning: urllib3 (2.2.1) or chardet (3.0.4) doesn't match a supported version! bla..bla..
  - **Solution :** install or upgrade the requests module in **pip** or **pip3** ([References](https://stackoverflow.com/questions/56155627/requestsdependencywarning-urllib3-1-25-2-or-chardet-3-0-4-doesnt-match-a-s))