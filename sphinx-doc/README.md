# MFD Const SPHINX DOCUMENTATION

## HOW TO GENERATE DOCS
### 1. Download or use system embedded Python in version at least 3.7
### 2. Create venv
- Create Python venv from MFD Const requirements for Sphinx (`<mfd_const_folder>/requirements-docs.txt`) 
- Link how to do this: `https://python.land/virtual-environments/virtualenv`
### 3. In Activated venv go to MFD Const directory `<mfd_const_folder>/sphinx-doc`
### 4. Run command:
```shell
$ python generate_docs.py
```
### 5. Open `<mfd_const_folder>/sphinx-doc/build/html/index.html` in Web browser to read documentation