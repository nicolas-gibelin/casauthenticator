from setuptools import setup

setup(
    name='jupyterhub-casauthenticator',
    version='1.0',
    description='CAS Authenticator for JupyterHub',
    url='https://github.com/.../casauthenticator',
    author='Nicolas Gibelin',
    author_email='Nicolas.Gibelin@univ-grenoble-alpes.fr',
    license='3 Clause BSD',
    packages=['casauthenticator'],
    install_requires=[
        'caslib',
        'jupyterhub',
    ]
)
