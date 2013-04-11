import facebook

# token generated for kwugirl@gmail.com user with permission to access interests
oauth_access_token = "AAACEdEose0cBAKtG0iZCCbj0tqj5ir8qGWD90iQZBffFLf09JDxTPb6sBlcZCXNp5an9lGre4hZA1wO9ZBGo7amxjB0x7perbj21RufoTBAZDZD"

graph = facebook.GraphAPI(oauth_access_token)
profile = graph.get_object("me")
interests_list = graph.get_connections("me", "interests") # interests is a list of dictionaries like [{u'category': u'Interest', u'created_time': u'2013-04-09T17:14:00+0000', u'name': u'Art', u'id': u'112230005457685'}, {u'category': u'Interest', u'created_time': u'2013-04-09T17:13:57+0000', u'name': u'Sports', u'id': u'106303419405901'}]

for interest in interests_list['data']: # loop through each dict in the interests list
	print interest['name'] # get the actual interests (Art,  Sports)