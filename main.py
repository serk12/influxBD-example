from influxdb import InfluxDBClient

client = InfluxDBClient(host='bd', port=8086, username='myuser',
                        password='secure-mypass', ssl=False, verify_ssl=False)
client.create_database('VirtusDB')
print(client.get_list_database())
print("ASDF")

point = (Point("mem")
         .tag("host", "host1")
         .field("used_percent", 23.43234543)
         .time(datetime.utcnow(), WritePrecision.NS))

write_api.write(bucket, org, point)
