import binascii
import random
import socket
import json
import types
import urllib.parse
import zlib
import sys
import threading
import h2.connection
import h2.events
import h2.config

testbed = sys.argv[1]
ueAuthCtx = 0
supiOrSuci = ''
supi = ''
suci = ''
nef_ipv4 = "10.69.97.79" 
nef_port = 4200
flag_Event_Notification_received = 0
#Parsing Header Frame
def decode_request(conn, event):

   
    global nef_ipv4
    global nef_port
    global flag_Event_Notification_received

    stream_id = event.stream_id
    header_data = dict(event.headers)
    header_data = {x.decode('ascii'): header_data.get(x).decode('ascii') for x in header_data.keys()}
    path = str(header_data.get(":path"))
    print(header_data)


    if (str(header_data.get(":method").replace(" ", "")) == "POST" and
            ("notify" in path)):
        flag_Event_Notification_received = 1

        print("Event Notification Received") 
        print("Sending 204 No Content")
       
        conn.send_headers(
            stream_id=stream_id,
            headers=[
                (':status', '204'),
                ('content-type', 'application/json')
            ],
        )

        
    else:
        print("Unhandled Request Received")



# Parsing DATA frame
def decode_data(conn, event):

    global supi
    global suci
    global flag_Event_Notification_received
    
    try:

        stream_id = event.stream_id

        json_data = event.data
        json_data = json.loads(json_data.decode('utf-8'))

        keys = json_data.keys()
        json_data = event.data

        if json_data == '' or json_data == b'':
            print("Empty body Received")
            return
        print("Printing the Json Body received")
        print(json_data)

        if (flag_Event_Notification_received==1):
            flag_Event_Notification_received=0
            print("No Data to send for 204")
        else:
            print("Unhandled Request Received")
    ## Enable to send Data on h2  ##
    # response_data={} #Enter Data you want to send//
    # response_data = json.dumps(response_data).encode(encoding='utf-8') #JSON Encoding of Data
    # conn.send_data(
    # stream_id=stream_id,
    # data=response_data,
    # end_stream=True
    # )
   ##-----------------------------##
    except Exception as e:
        print("Exeception caused while decoding Data")
        print(str(e))



    pass



def handle(sock):
    config = h2.config.H2Configuration(client_side=False)
    conn = h2.connection.H2Connection(config=config)
    conn.initiate_connection()

    try:
        while True:
            data = sock.recv(65535)
            if not data:
                print("Socket does not have data")
                break

            events = conn.receive_data(data)
            print(events)

            for event in events:
                if isinstance(event, h2.events.RequestReceived):
                    try:
                        decode_request(conn, event)
                        print("Request received")
                    except:
                        print("An error occurred in decode_request(conn, event)")
                if isinstance(event, h2.events.DataReceived):
                        try:
                            decode_data(conn, event)
                            print("DATA received")
                        except:
                            print("An error occurred in decode_data(conn, event)")

            data_to_send = conn.data_to_send()
            if data_to_send:
                sock.sendall(data_to_send)
                print("Sent data on socket")
            else:
                print("No data to send on socket")

    except Exception as e:
        print("Error Handling the Request from Client ")
        print(str(e))
    finally:
        print("Closing Connection...." + str(client_sock1))
        conn.close_connection()

### Code For Socket Creation and Binding ###
config = h2.config.H2Configuration(client_side=False)
conn = h2.connection.H2Connection(config=config)

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket Object Created")
print("NEF IP address is "+str(nef_ipv4)+" -Port : "+str(nef_port))
nef_port = int(nef_port)
sock.bind((nef_ipv4, nef_port))
sock.listen(2)
print("Listening on Port")


while True:
           
    ### Added a thread for Receiving Multiple request ###
    try:
        print("handle() start")
        client_sock1, client_addr1 = sock.accept()
        print(" Client Sock - " + str(client_sock1))
        print("Clinet Addr - " + str(client_addr1))
        client_handler=threading.Thread(target=handle, args=(client_sock1,))
        client_handler.start()

    except Exception as e:
            print("----*** Excepttion caused Termination of Server ***----")
            print("Exception: "+str(e))
            break
 