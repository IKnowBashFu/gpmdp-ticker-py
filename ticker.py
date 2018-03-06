# Defines what information our ticker has access to, and contains
# a function for writing the data to the local filesystem

from config import Config
import os

class Ticker:

	def __init__(self):
		self.playing = False
		self.title = ""
		self.artist = ""
		self.album = ""
		self.__changed = False

	@property
	def playing(self):
		return self.__playing

	@playing.setter
	def playing(self, playing):
		self.__playing = playing
		self.__changed = True

	@property
	def title(self):
		return self.__title
	
	@title.setter
	def title(self, title):
		self.__title = title
		self.__changed = True

	@property
	def artist(self):
		return self.__artist

	@artist.setter
	def artist(self, artist):
		self.__artist = artist
		self.__changed = True

	@property
	def album(self):
		return self.__album

	@album.setter
	def album(self, album):
		self.__album = album
		self.__changed = True

	def saveTickerFile(self):
		newstr = Config.outputFormat.replace('$artist', self.__artist).replace('$album', self.__album).replace('$track', self.__title)

		if self.__changed:
			with open(os.path.normpath(Config.fileLocation), 'w') as file:
				if self.__playing:
					file.write(newstr)
				else:
					file.write(Config.pausedOutput)
				self.__changed = False