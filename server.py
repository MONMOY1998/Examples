server = {'OS': 'CentOS 7',
          'IP': '10.10.0.244',
    'hostname': 'ccs2',
    'location': 'Room 237',
       'model': '4451',
         'OEM': 'Fujitsu'
}
print(server)
server_lo = {key.lower(): value for key, value in server.items()}
print(server_lo)
