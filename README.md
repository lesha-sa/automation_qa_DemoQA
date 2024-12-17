## Test automation framework for testing UI web site - https://demoqa.com/

## Table of contents
1. [Test framework configuration and setup](#test-framework-configuration-and-setup)
2. [Preparation before running tests](#preparation-before-running-tests)
3. [Tests](#tests)

### Test framework configuration and setup

In this project used 'pip-tools'. All used Python packages for the current project are generates in requirements.txt
Below is the list of main packages with references

### **For test itself**
### pytest

related info: https://docs.pytest.org/en/latest/
```bash
    pip install pytest
```    
## **For ui/web testing**

### selenium

related info: https://selenium-python.readthedocs.io/
```bash
    pip install selenium
```
### webdriver-manager

related info:https://github.com/bonigarcia/webdrivermanager
```bash
    pip install webdriver-manager
```

## **Logging**

### loguru

pypi.org docs: https://pypi.org/project/loguru/
related info: https://loguru.readthedocs.io/
```bash
pip install loguru
```
## **REQUESTS**
pypi.org docs: https://pypi.org/project/requests/
```bash
pip install requests
```
## **Data generators**

### Faker

related info: http://faker.rtfd.org/
```bash
pip install Faker
```

## Preparation before running tests
Create virtual environment.
To create a virtual environment, execute the following commands in the command line:
```bash
pip install virtualenv
```
To activate the virtual environment:

```bash
venv\Scripts\activate
```

All used packages are stored in requirements.txt
```bash
pip install -r requirements.txt
```

## Tests

All tests are located in  ***tests*** folder

To run all the tests from the root directory, you can use the following command:
For the command to work, you need to perform the following steps:
1. Clone the project
2. Create and activate virtual environment
3. Install all dependencies from the file requirements.txt
4. Open the folder with the project and copy the path to it
5. In the pytest.ini paste the previously copied path into the line pythonpath
```shell
 pytest
```
   

To run a specific test, use the command, where * this is the name of the test.:
```bash
pytest tests/elements_test/*.py
```