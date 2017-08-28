import caslib
import re
import urllib
import sys

from jupyterhub.auth import Authenticator
from tornado import gen
from traitlets import Unicode, Int, Bool, List, Union


class CASAuthenticator(Authenticator):
    server_address = Unicode(
        config=True,
        help="""
        Address of the CAS server to contact.

        Full url of the cas server.
        """
    )

    service_address = Unicode(
        config=True,
        help="""
        Address of the service for CAS login (generaly, the server where you log from).

        Full url of the server.
        """
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        password = data['password']

        self.log.debug("Server address:", self.server_address)
        self.log.debug("Service address:", self.service_address)

        # No empty passwords!
        if password is None or password.strip() == '':
            self.log.warn('username:%s Login denied for blank password', username)
            return None

        try:
            caslib.login_to_cas_service(self.server_address, username, password, self.service_address)
            return username
        except Exception as e:
            return None

    @gen.coroutine
    def add_user(self, user):
        """Hook called whenever a new user is added

        """
        yield gen.maybe_future(super().add_user(user))
