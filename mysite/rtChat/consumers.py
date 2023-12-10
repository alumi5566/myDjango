import json
from channels.generic.websocket import AsyncWebsocketConsumer

# Here we are creating a class named ChatConsumer which inherits from AsyncWebsocketConsumer and
# this is used to create, destroy and do a few more things with WebSockets.
# And here we are creating ChatSocket for the required purpose.

# This ChatConsumer which we are mapping in the routing.py is the same in this consumers.py.
# These scripts are on asynchronous mode hence we are working with async and await here.
class ChatConsumer(AsyncWebsocketConsumer):

    # async def connect(self): This function works on the websocket instance which has been created.
    # When the connection is open or created, it connects and accepts the connection.
    # It creates a group name for the chatroom and adds the group to the channel layer group.
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()
    # async def disconnect(): This just removes the instance from the group.
    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName ,
            self.channel_layer
        )
    # async def receive(): This function is triggered when we send data from the WebSocket ( the event for this to work is: send ),
    # this receives the text data which has been converted into the JSON format ( as it is suitable for the javascript ) after the text_data has been received,
    # then it needs to be spread out to the other instances which are active in the group.
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                "message" : message ,
                "username" : username ,
            })
    # async def sendMessage(self, event): This function takes the instance which is sending the data and the event,
    # basically event holds the data which was sent via the group_send() method of the receive() function.
    async def sendMessage(self , event) :
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message":message ,"username":username}))
