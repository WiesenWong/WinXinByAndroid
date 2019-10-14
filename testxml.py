#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("uidump.xml")
collection = DOMTree.documentElement

nodes = collection.getElementsByTagName("node")

for node in nodes:
	if node.getAttribute('text'):
		print(node.getAttribute('text'))
		print(node.getAttribute('bounds'))