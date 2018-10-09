import requests
import json



class SnapChat:
	def __init__(self, username):
		self.username = username

	
	def snapcode(self, bitmoji=False, size=None):
		url = "https://app.snapchat.com/web/deeplink/snapcode?username={}&type={}"

		if bitmoji == False:

			filetype = "PNG"

			snapcode_url = url.format(self.username, filetype)

			if size:

				if int(size) > 1000:
					raise ValueError("size cant exceed 1000")

				url_with_size = url+"&size={}"
				
				snapcode_url = url_with_size.format(self.username, filetype, size)
				size = str(size)+"x"+str(size)

				return snapcode_url, size

			return snapcode_url

		else:

			# If filetype is SVG, you will get the 
			# SnapCode with the bitmoji

			filetype = "SVG"

			# Putting all the information into the url
			snapcode_url = url.format(self.username, filetype)

			return snapcode_url

#make this into a class
#then make title, urls and previews as seperate functions
# remember to add the @ thing on each function

class PublicStory(SnapChat):

	def __init__(self):
		self._title = None
		self._urls = None
		self._previews = None
		#self.username = username


	def getData(self):
		"""
		this function allows you do get the links to all of their story in MP4
		"""
		story_url = "https://storysharing.snapchat.com/v1/fetch/{}?request_origin=ORIGIN_WEB_PLAYER"

		# This is the error that you get if the story is not valid
		# is no longer available
		story_not_found = "rpc error: code = NotFound desc = Not found."

		r = requests.get(story_url.format(self.username))

		if story_not_found in r.text:
			#return "Story not found"
			pass

		else:
			data = json.loads(r.text)


		title = data.get("story").get("metadata").get("title", "NoTitle")
		
		# Not sure why, but I get some random text instead of the emoji
		#user_emoji = str(data["story"]["metadata"]["emoji"])

		media_previews = []
		media_urls = []

		# remove the "index" and the enumerate
		if data.get("story").get("snaps"):
				for index, snap in enumerate(data.get("story").get("snaps")):
					
					media_preview = snap.get("media").get("mediaPreviewUrl")
					media_url = snap.get("media").get("mediaUrl")

					if media_preview != None:
						media_previews.append(media_preview)
					
					media_urls.append(media_url)

		else:
			#return "No stories available"
			pass

		self._title = title
		self._urls = media_urls
		self._previews = media_previews

		return self._title, self._urls, self._previews

	@property
	def title(self):
		if self._title is None:
			self._title = getData()[0]
		return self._title


	@property
	def urls(self):
		if self._urls is None:
			self._urls = getData()[1]
		return self._urls


	@property
	def previews(self):
		if self._previews is None:
			self._previews = getData()[2]
		return self._previews
