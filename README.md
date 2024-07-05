# PyTest API Automation

## Pre-requisites
- *Install PyTest module* in **cmd/terminal**:
  - **Run :** `pip install pytest`
  - Check installation
    - `pytest --help` or `py -m pip list`
- *Install HTML Report plugin* in **cmd/terminal**:
  - **Run:** `pip install pytest-html`

## How to Run the PyTest
- **Create** a file *containing* function (`def test_bla_bla():`) and assert test code
- **Run** the file in *cmd/terminal* :
  - `pytest path/to_file.py`
  - Print to console : `pytest -s path/to_file.py` ([References](https://stackoverflow.com/questions/24617397/how-do-i-print-to-console-in-pytest))

## Create an example of a GET request
- Create file **get_list_users.py**
- Import required **libraries**
- Code ([References 1](https://www.geeksforgeeks.org/response-json-python-requests/), [References 2](https://medium.com/@qebuzzz/validating-and-asserting-responses-in-python-requests-14b40908327a), [References 3](https://github.com/Anshul-Sonpure/API-Testing-using-Python/tree/master)) and **run**
  
## Validate JSON Schema Response Body
- Configuring **files** to make *requests*
- Import required **libraries**
- **Create** a json schema response body *file/variable* to verify using [the Helper](https://github.com/mrisqiamiruladieb/REST-Assured-Java-Part-1/blob/master/README.md#helper)
- Code ([References](https://builtin.com/software-engineering-perspectives/python-json-schema)) and *run*

## HTML Report
- *To generate a report*, **go to the directory of the Pytest/test file** that needs to be run ([References](https://www.tutorialspoint.com/selenium_webdriver/selenium_webdriver_generating_html_test_reports_in_python.htm#:~:text=To%20generate%20a%20HTML%20report,html.)) or in **the root directory** is also fine
- Then **run** the command: `pytest --html=report.html` or `pytest -s path\to\test_file.py --html=report.html`
- A new file called **report.html will be created** inside the project/directory
- **Open report.html file** in browser

## Issues and Solutions
- Errors/warnings when executing **the requests**
  - ***Error/warning messages :*** RequestsDependencyWarning: urllib3 (2.2.1) or chardet (3.0.4) doesn't match a supported version! bla..bla..
  - **Solution :** install or upgrade the requests module in **pip** or **pip3** ([References](https://stackoverflow.com/questions/56155627/requestsdependencywarning-urllib3-1-25-2-or-chardet-3-0-4-doesnt-match-a-s))
- **Error** when calling **global variables** (*store* and *reuse* variables) for **end-to-end testing**
  - ***Error messages :*** UnboundLocalError: local variable 'email_request' referenced before assignment
  - **Solution :** declare the variable to be a global variable for each test or function ([References](https://youtu.be/7-uqSb83BTg?si=nKbLNzL5D5hIgHcc))
- **Resolve** *cannot import files* from *different directories*
  - **Solution :** using [Importing From Parent or Sibling Directories With Package Relative Imports](https://sentry.io/answers/import-files-from-a-different-folder-in-python/#importing-from-parent-or-sibling-directories-with-package-relative-imports)
    - **Prerequisite:** *create* `__init__.py` file in *each directory* (*to recognise the directory is a package*)
- *Get* response json **dictionary** data (*array, object*)
  - **Solution:** *Examples*
    - ([References](https://stackoverflow.com/questions/49595050/attributeerror-list-object-has-no-attribute-get)) Access data[1].last_name
      - `second_user_last_name = respJson.get('data')[1].get('last_name')`
    - Access data[0].id
      - `first_user_id = respJson['data'][0]['id']`