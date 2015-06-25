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
		print sender, "::", message

	def MessageStatus(self, msg, status):
		print msg.Sender.Language
		if status == Skype4Py.cmsReceived:
			if msg.Chat.Type in (Skype4Py.chatTypeDialog, Skype4Py.chatTypeLegacyDialog):
				self.LogMessage(msg.FromHandle, msg.Body)
				url = 'http://spiralpower.net/files/SkypeBot/server/'
				payload = {'message': msg.Body, 'sender_handle': msg.FromHandle, 'sender_fullname': msg.FromDisplayName, 'sender_country': msg.Sender.CountryCode, 'sender_language': msg.Sender.Language}
				r = requests.post(url, data=payload)
				msg.Chat.SendMessage(unicode(r.text))
				self.LogMessage("ROBOT", unicode(r.text))

if __name__ == "__main__":
	bot = Robot()

	while True:
		time.sleep(1.0)