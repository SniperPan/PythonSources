#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax

file = open('ydcd.txt', 'w')

class ydcdXmlHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.word = ""
		
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		
	def endElement(self, tag):
		if self.CurrentData == "word":
			file.write(self.word+'\n')
		self.CurrentData = ""
		
	def characters(self, content):
		if self.CurrentData == "word":
			self.word = content

if (__name__ == "__main__"):
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	
	Handler = ydcdXmlHandler()
	parser.setContentHandler(Handler)
	
	parser.parse("ydcd.xml")
	
