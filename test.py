import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Set friendly name for API connection
skype.FriendlyName = "Jordan's Skype Bot"

# Connect the Skype object to the Skype client
skype.Attach()

# Obtain some information from the client and print it out.
print 'Your full name: ', skype.CurrentUser.FullName
print 'Your contacts:'
for user in skype.Friends:
	if len(user.FullName) < 1:
		print '    ', user.Handle
	else:
		print '    ', user.Handle, '(', user.FullName, ')'

# Attempt to create a chat

mychat = skype.CreateChatWith("markribz")
mychat.SendMessage("skype4py test two")


# First element in messages is the most recent message
for message in mychat.Messages:
	print message.Body
