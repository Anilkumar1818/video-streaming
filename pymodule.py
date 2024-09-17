import websocket
import json
import sys
import requests

def extractStreamId(message):
  j = json.loads(message)
  m = j['message']
  message = json.loads(m)
  id = message['data']['id']

  #print('[websocket] streamId: %s' % id)

  return id

def setStreamingUrlById(id, url):
  apiUrl = ("http://localhost:8083/%s/python-wrapper-service/v1/streams/%s" % (clientId, id))
#file:///home/vaibhav/Desktop/Demo17/vs/dash.mp4
  payload = { "url": "file:///home/nakka/Desktop/sdv-ms/vs_rest/vs/dark.mp4"}
  #payload = {"url":"http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"}
  headers = {'content-type': 'application/json'}
  r = requests.post(apiUrl, data = json.dumps(payload), headers = headers)

  print(r)





def on_message(wsapp, message):
  #print("[websocket] %s\n" % message)

  id = extractStreamId(message)

  setStreamingUrlById(id, 'http://localhost/stream')

def run_app1():
  global clientId
  clientId = sys.argv[1:][0]
  wsapp = websocket.WebSocketApp("ws://localhost:8083/ws/%s/python-wrapper-service/v1" % clientId
  , on_message=on_message)

  print("Websocket Connected ...\n")
  wsapp.run_forever()

if __name__=='__main__':
  run_app1()

