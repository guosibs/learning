# Alan and Julia's learning playground
This is a sandbox for Alan and Julia to play around with machine learning
(in Python for now).

This assumes a macOS environment.

# Setup
Make sure you have the following installed on your system:
* Python 2.7
* pip

It's strongly advised that you use a virtualenv for the Python code.
Check that you have virtualenv installed:
```
virtualenv --version
```
If you don't, you can install with
```
pip install virtualenv
```
Then, in the project folder (`/learning`), run
```
virtualenv env
```
To enter the virtualenv, run
```
. env/bin/activate
```
and to exit run
```
deactivate
```
From now on, we will assume you are doing any development in the virtualenv.
Install Python dependencies:
```
pip install -r requirements.txt
```
This includes Google's TensorFlow package.
To validate the installation, run the validation script.
```
python src/validate.py
```
