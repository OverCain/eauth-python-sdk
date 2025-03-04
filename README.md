What is Eauth?
==============

https://eauth.us.to/ - Your #1 software login and authentication system, providing you with the most secure, flexible, and easy-to-use solutions.

Functions
-------------

```python
def init_request()
def login_request(username, password)
def register_request(username, password, key)
```

Configuration
-------------

Navigate to `eauth.py`, and fill these lines of code:

```python
# Required configuration
application_token = "" # Your application token goes here
application_secret = "" # Your application secret goes here
application_version = "1.0" # Your application version goes here
```