import httplib
import ssl
from base64 import b64encode
import json

DEFAULT_PATH="/calendar/next/{device_id}"

class ClientException(Exception):
    pass
class BadResponse(ClientException):
    pass

class Client:
    def __init__(self, device_id, secret, server_str, cert_path):
        self.device_id = device_id
        self.auth_string = b64encode(b"{}:{}".format(device_id, secret)).decode("ascii")
        # create connection with own certificate
        self.con = httplib.HTTPSConnection(
            server_str,
            context=ssl.create_default_context(cafile=cert_path)
        )

    def _send_request(self, method, path, BODY):
        # We need to send auth string with every request
        self.con.request(method, path, BODY, headers={ 
            'Authorization' : 'Basic %s' %  self.auth_string 
            }
        )
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
            raise BadResponse("Bad http status in response {}".format(response.status))
    
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

def example():
    client = Client("hanswurst", "tQ6cJ4RTAkNpkbg4mou4S6Omlo7l87D7AjY=", "comfortaable.com:1443", "cert.pem")
    print(client.get_next_appointment_raw())

if __name__ == '__main__':
    example()