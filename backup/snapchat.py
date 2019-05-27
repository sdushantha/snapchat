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