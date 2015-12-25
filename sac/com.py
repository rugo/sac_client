import httplib
import ssl
from base64 import b64encode
import json
import config
from socket import gaierror

DEFAULT_PATH="/calendar/next/{device_id}"
# default fields to return on get values methods
DEFAULT_VALUE_ORDER = ["time", "name", "description", "location"]

class ClientException(Exception):
    pass
class BadResponse(ClientException):
    pass
class NoInternet(ClientException):
    pass

class Client:
    def __init__(self, device_id, secret, server_str, cert_path):
        self.device_id = device_id
        self.auth_string = b64encode(b"{}:{}".format(device_id, secret)).decode("ascii")
        # create connection with own certificate
        self.con = httplib.HTTPSConnection(
            server_str,
            context=ssl.create_default_context(cafile=cert_path),
            timeout=config.REQUEST_TIMEOUT
        )

    def _send_request(self, method, path, BODY):
        # We need to send auth string with every request
        try:
            self.con.request(method, path, BODY, headers={ 
                'Authorization' : 'Basic %s' %  self.auth_string 
                }
            )
        except gaierror:
            raise NoInternet()
        return self.con.getresponse()

    def send_request(self, path, method="GET", BODY=""):
        try:
            return self._send_request(method, path, BODY)
        except httplib.NotConnected as e:
            self.con.connect() # lost connection
            return self._send_request(method, path, BODY)

    def _handle_response(self, response):
        if response.status == httplib.OK:
            return response.read()
        else:
            raise BadResponse("Bad http status in response {}, {}".format(response.status, response.read()))
    
    def connection_works(self):
        try:
            self.get_next_appointment_raw()
        except BadResponse as e:
            return False
        return True

    def get_next_appointment_raw(self):
        """
        Return next appointment as json string.
        """
        return self._handle_response(self.send_request(DEFAULT_PATH.format(device_id=self.device_id)))

    def get_next_appointment(self):
        """
        Returns next appointment as python dict.
        """
        return json.loads(self.get_next_appointment_raw())

    def get_next_appointment_values(self, sep):
        """
        Returns next appointment values as unicode string, seperated by sep
        """
        app = self.get_next_appointment()["appointment"]
        return sep.join([unicode(app[f]) for f in DEFAULT_VALUE_ORDER]).encode("utf-8")

def example():
    client = Client("dadasdasdas", "QE4x9QRfCbYb8Lhvb1ENX+j9JZM6bYBtkOk=", config.API_SERVER, config.CERT_PATH)
    print(client.get_next_appointment())

if __name__ == '__main__':
    example()
