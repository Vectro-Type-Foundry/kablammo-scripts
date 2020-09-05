# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from vanilla import *

class KablammoDashGrid(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.name = u'Kablammo Dash Grid'
		self.menuName = Glyphs.localize({'en': self.name})
		self.keyboardShortcut = 'k'
		self.keyboardShortcutModifier = NSControlKeyMask | NSCommandKeyMask | NSAlternateKeyMask
		self.numRows = 9
		self.rowWidth = 100
		self.marginTop = 79
		self.marginBottom = 69
		self.onColor = ( 0.0, 1.0, 0.0, 0.15 )
		self.offColor = ( 1.0, 0.0, 0.0, 0.15 )
	
	@objc.python_method
	def foreground(self, layer):
		rowHeight = (layer.master.capHeight - self.marginTop - self.marginBottom) / float(self.numRows)

		for i in range(int(self.numRows)):
			y = i * rowHeight + self.marginBottom
			c1 = self.offColor
			c2 = self.onColor			

			if (i % 2 == 0):
				c1 = self.onColor
				c2 = self.offColor

			self.drawRow(0, y, self.rowWidth, rowHeight, c1)
			self.drawRow(layer.width - self.rowWidth, y, self.rowWidth, rowHeight, c2)

	@objc.python_method
	def drawRow(self, x, y, w, h, c):
		NSColor.colorWithCalibratedRed_green_blue_alpha_(*c).set()
		rect = NSRect()
		rect.origin = NSPoint(x, y)
		rect.size = NSSize(w, h)
		NSBezierPath.fillRect_(rect)
		
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
