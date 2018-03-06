import os
import yaml

class Config:
	fileLocation = ""
	outputFormat = ""
	pausedOutput = ""
	updateRate   = 0

	@staticmethod
	def readConfig():
		with open('./config.yaml', 'r') as f:
			config = f.read()
			configObj = yaml.load(config)
			
			Config.fileLocation = configObj['File Location']
			Config.outputFormat = configObj['Output Format']
			Config.pausedOutput = configObj['Paused Output']
			Config.updateRate   = configObj['Update Rate']