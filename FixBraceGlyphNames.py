#MenuTitle: Fix Brace Layer Names

# -*- coding: utf-8 -*-
__doc__="""
Reset glyph Names to based on brace values. Fixes annoying bug generating in fontmake from Glyphs file.
"""

from GlyphsApp import *
from Foundation import *
import re

class FixBraceGlyphNames(object):

  def __init__(self, sender):
    self.axisId = Glyphs.font.axes[0].axisId

    self.run()
    

  def makeLayerNotSpecial(self, layer):
    if layer.isSpecialLayer:
      oldName = layer.name
      coords = str(layer.attributes['coordinates'])
      layer.attributes['coordinates'] = None
      if oldName != layer.name:
        layer.name = oldName

  def makeNotSpecial(self):
    for glyph in Glyphs.font.glyphs:
      glyph.beginUndo()
      for layer in glyph.layers:
        self.makeLayerNotSpecial(layer)        
      glyph.endUndo()

  def makeLayerSpecial(self, layer):
    if layer.name.startswith("{"):
      layerName = str(layer.name)
      coordVal = layerName.replace('{', '').replace('}', '') 
      layer.attributes['coordinates'] = {self.axisId: int(coordVal)}

  def makeSpecialAgain(self):
    for glyph in Glyphs.font.glyphs:
      glyph.beginUndo()
      for layer in glyph.layers:
        self.makeLayerSpecial(layer)
      glyph.endUndo()

  def run(self):
    self.makeNotSpecial()
    self.makeSpecialAgain()
    
FixBraceGlyphNames('')