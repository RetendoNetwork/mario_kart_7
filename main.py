import os
import logging
from pymongo import MongoClient

# Configure the logger
logger = logging.getLogger('pretendo')
logger.setLevel(logging.WARNING)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class NEXServer:
    def __init__(self):
        self.prudp_version = 0
        self.nex_version = {'major': 3, 'minor': 4, 'patch': 17}
        self.kerberos_password = os.getenv("KERBEROS_PASSWORD")
        self.access_key = "6181dff1"
        self.ping_timeout = 20
        self.data_handlers = []

    def set_prudp_version(self, version):
        self.prudp_version = version

    def set_default_nex_version(self, version):
        self.nex_version = version

    def set_kerberos_password(self, password):
        self.kerberos_password = password

    def set_access_key(self, key):
        self.access_key = key

    def set_ping_timeout(self, timeout):
        self.ping_timeout = timeout

    def on_data(self, handler):
        self.data_handlers.append(handler)

    def listen(self, address):
        print(f"Listening on {address}")
        # Simulate receiving data
        for handler in self.data_handlers:
            handler({'protocol_id': 1, 'method_id': 2})

def password_from_pid(pid):
    # Dummy function for password retrieval
    return "password"

def main():
    nex_server = NEXServer()
    nex_server.set_prudp_version(0)
    nex_server.set_default_nex_version({'major': 3, 'minor': 4, 'patch': 17})
    nex_server.set_kerberos_password(os.getenv("KERBEROS_PASSWORD"))
    nex_server.set_access_key("6181dff1")
    nex_server.set_ping_timeout(20)

    def data_handler(packet):
        request = packet
        print("==MK7 - Auth==")
        print(f"Protocol ID: {request['protocol_id']}")
        print(f"Method ID: {request['method_id']}")
        print("====================")

    nex_server.on_data(data_handler)

    # Simulate setting up authentication protocol
    secure_station_url = {
        'scheme': 'prudps',
        'address': os.getenv("SECURE_SERVER_LOCATION"),
        'port': os.getenv("SECURE_SERVER_PORT"),
        'cid': '1',
        'pid': '2',
        'sid': '1',
        'stream': '10',
        'type': '2'
    }

    # Simulate setting up authentication protocol
    authentication_protocol = {
        'secure_station_url': secure_station_url,
        'build_name': "Pretendo MK7",
        'password_from_pid_function': password_from_pid
    }

    nex_server.listen(":61000")

if __name__ == "__main__":
    main()
