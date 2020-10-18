# encoding: utf-8

###########################################################################################################
#
#
#	Select Tool Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/SelectTool
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class KablammoGashTool(SelectTool):
	
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({'en': u'Gash Tool'})
		# self.generalContextMenus = [
		# 	{'name': Glyphs.localize({'en': u'Gash Tool'}), 'action': self.printInfo},
		# ]
		self.keyboardShortcut = 'g'
		self.keyboardShortcutModifier = NSControlKeyMask | NSCommandKeyMask | NSAlternateKeyMask
	
	@objc.python_method
	def start(self):
		pass
	
	@objc.python_method
	def activate(self):
		Glyphs.addCallback(self.handleClick, MOUSEDOWN)
		pass

	@objc.python_method
	def deactivate(self):
		Glyphs.removeCallback(self.handleClick, MOUSEDOWN)
		pass
	
	@objc.python_method
	def handleClick(self, sender):
		print('click', self.mousePosition())

	def mousePosition(self):
		return Glyphs.currentDocument.windowController().activeEditViewController().graphicView().getActiveLocation_(Glyphs.currentEvent())
	
	# @objc.python_method
	# def conditionalContextMenus(self):

	# 	# Empty list of context menu items
	# 	contextMenus = []

	# 	# Execute only if layers are actually selected
	# 	if Glyphs.font.selectedLayers:
	# 		layer = Glyphs.font.selectedLayers[0]
			
	# 		# Exactly one object is selected and it’s an anchor
	# 		if len(layer.selection) == 1 and type(layer.selection[0]) == GSAnchor:
					
	# 			# Add context menu item
	# 			contextMenus.append({'name': Glyphs.localize({'en': u'Randomly move anchor', 'de': u'Anker zufällig verschieben'}), 'action': self.randomlyMoveAnchor})

	# 	# Return list of context menu items
	# 	return contextMenus
	
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__