# -*- coding: utf-8 -*-
__doc__="""
Brings Bracket Layers to Components, when needed
"""

from GlyphsApp import * 

class AddSpecialLayersToComponents(object):

  def __init__(self, sender):
    self.masterId = Glyphs.font.masters[0].id
    self.run()

  def getParentSpecialLayers(self, component):
    specialLayers = []
    for layer in component.component.layers:
      if layer.isSpecialLayer:
        specialLayers.append(layer)
    return specialLayers

  def addSpecialLayersToGlyph(self, glyph, specialLayers):
    for specialLayer in specialLayers:
      if not glyph.layers[specialLayer.name]:
        print('Added: ' + glyph.name + ' -> ' + specialLayer.name, specialLayer.master)
        newLayer = GSLayer()
        newLayer.name = specialLayer.name
        newLayer.associatedMasterId = specialLayer.master.id
        glyph.layers.append(newLayer)
        glyph.layers[specialLayer.name].reinterpolate()

  def run(self):
    for glyph in Glyphs.font.glyphs:
      specialLayers = []
      masterLayer = glyph.layers[self.masterId]
      for component in masterLayer.components:
        specialLayers = specialLayers + self.getParentSpecialLayers(component)
      self.addSpecialLayersToGlyph(glyph, specialLayers)

    Glyphs.redraw()