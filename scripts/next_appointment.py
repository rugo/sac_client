#!/opt/sac/bin/python
from sac import com
from sac import util
from sac import config

client = com.Client(util.get_device_id(), util.get_secret(), config.API_SERVER, config.CERT_PATH)

print(client.get_next_appointment_values("\n"))
