import serial
import struct

def write_html_boilerplate(file, content, page_update_interval_ms):
    file.write('<html>' +
               '<body>' +
               '<script>' +
               'setTimeout( function() {' +
               'window.location.reload();' +
               '},' + str(page_update_interval_ms) + ' );' +
               '</script>' +
               content +
               '</body>' +
               '</html>')

def write_error_html(file):
    write_html_boilerplate(file, '<span style="color: red;">ERROR</span>')

def write_html(file, sensor1, page_update_interval_ms = 2500):
    write_html_boilerplate(file,
                           'Sensor1: ' + str(sensor1),
                           page_update_interval_ms )


# < indikerar little-endian för hela formatet
# följt av en float (f)
DATA_FORMAT = '<f'

ser = serial.Serial('/dev/ttyAMA0',baudrate=9600)
while True:
    try:
        raw_data = ser.read(struct.calcsize(DATA_FORMAT))
        data = struct.unpack(DATA_FORMAT, raw_data)
        (sensor1,) = data
        print(str(data) + '  ' + raw_data.hex(sep=' '))
        with open('stream.html', 'w') as f:
            write_html(f, sensor1)
    except:
        with open('stream.html', 'w') as f:
            write_error_html(f)
