import smbus2

def write_file(file, sensor1, page_update_interval_ms = 2500):
    file.write('<html>' +
               '<body>' +
               '<script>' +
               'setTimeout( function() {' +
               'window.location.reload();' +
               '},' + str(page_update_interval_ms) + ');' +
               '</script>' +
               'querhio ' + str(sensor1) +
               '</body>' +
               '</html>')

# with open('waaa.html', 'w') as f:
#     write_file(f, 123456)

bus = smbus2.SMBus(1)
while True:
    # antag att master har address 0...
    # och jag har address 10
    data = bus.read_i2c_block_data(10, 0, length=4)
    print(str(data))