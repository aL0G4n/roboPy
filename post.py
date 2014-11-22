import http.client, urllib.parse, alsaaudio

def hello(conn):
    params = urllib.parse.urlencode({})
    headers = {"Content-type": "text/plain", "ROBOT_ID":"4"}
    conn.request("POST", "/hello", params,headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    
def sound(conn,duration,length):
    params = urllib.parse.urlencode({})
    headers = {"robot_id":4,"timecode":1,"durations":duration,"size_bytes":length}
    conn.request("POST", "/soundRecorded", params,headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)

conn = http.client.HTTPConnection("192.168.43.1:8080")

stream = alsaaudio.PCM(type=PCM_CAPTURE, mode=PCM_NORMAL, card='default')
stream.setrate(16000)
stream.setformat(PCM_FORMAT_U16_BE)
stream.setperiodsize(8000)

runflag = 1
while runflag:
    # read data from audio input
    [length, data]=stream.read()
    duration = length/16000
    sound(conn,duration,length)
    
conn.close()
