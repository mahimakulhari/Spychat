from datetime import datetime

class spy:
    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.current_status_message=None
spy = spy("bond","mr.","24","4.7")
friend_one = spy("joey","mr.", "27","4.7")
friend_two = spy("rachel","ms.","21","4.39")
friend_three = spy("ross","dr.","37","4.95")

friends = (friend_one, friend_two, friend_three)

class chatmessage:

    def __init__(self,message,sent_by_me, time=None):
     self.message = message
     '''if condition only needed if the student attempts the objective to load chats'''
     if not time:
         self.time = datetime.now()
     else:
         self.time=time

     self.sent_by_me = sent_by_me
