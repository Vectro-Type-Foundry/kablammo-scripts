# encoding: utf-8

###########################################################################################################
#
#
#	Palette Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Palette
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
import vanilla

class KablammoPalette (PalettePlugin):
	
	# dialog = objc.IBOutlet()
	# textField = objc.IBOutlet()
	
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({'en': u'Kablammo'})
		self.min = 200
		self.initInterface()
	
	@objc.python_method
	def initInterface(self):
		self.w = vanilla.Window((200, 70), "Window Demo")
		self.w.textBox = vanilla.TextBox((10, 10, -10, 17), "A TextBox")
		self.w.open()

	@objc.python_method
	def start(self):
		print("start")
	
	@objc.python_method
	def __del__(self):
		print("close")
	


	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	
	# Temporary Fix
	# Sort ID for compatibility with v919:
	_sortID = 0
	@objc.python_method
	def setSortID_(self, id):
		try:
			self._sortID = id
		except Exception as e:
			self.logToConsole( "setSortID_: %s" % str(e) )
	
	@objc.python_method
	def sortID(self):
		return self._sortID
	