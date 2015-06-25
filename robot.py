import Skype4Py
import time
import re
import requests
import json

class Robot(object):
	def __init__(self):
		self.skype = Skype4Py.Skype(Events=self)
		self.skype.FriendlyName = "Skynet v0.0.1a"
		self.skype.Attach()

	def AttachmentStatus(self, status):
		if status == Skype4Py.apiAttachAvailable:
			self.skype.Attach()

	def LogMessage(self, sender, message):
		print sender, message

	def MessageStatus(self, msg, status):
		if status == Skype4Py.cmsReceived:
			if msg.Chat.Type in (Skype4Py.chatTypeDialog, Skype4Py.chatTypeLegacyDialog):
				LogMessage(msg.FromHandle, msg.Body)
				url = 'http://spiralpower.net/files/skypebot/'
				payload = {'message': msg.Body, 'sender_handle': msg.FromHandle, 'sender_fullname': msg.FromDisplayName}
				r = requests.post(url, data=payload)
				msg.Chat.SendMessage(r.text)
				LogMessage('self', r.text)

if __name__ == "__main__":
	bot = Robot()

	while True:
		time.sleep(1.0)