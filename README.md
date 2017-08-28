# ldapauthenticator

## Installation ##

You can install it from pip with:

```
```

## Requirements ##

caslib >= 1.0.0

## Usage ##

You can enable this authenticator with the following lines in your
`jupyter_config.py`:

```python
c.JupyterHub.authenticator_class = 'casauthenticator.CASAuthenticator'
```

### Required configuration ###

At minimum, the following two configuration options must be set before
the LDAP Authenticator can be used:

#### `CASAuthenticator.server_address` ####

Address of the CAS Server to contact.
