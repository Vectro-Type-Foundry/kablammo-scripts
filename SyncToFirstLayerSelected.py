# This copies the current layer and replaces all other masters in the glyph.

from GlyphsApp import *

class SyncToFirstLayerSelected(object):

  def __init__(self, sender):
    self.run()

  def syncGlyph(self, glyph):
    baseLayerId = Glyphs.font.masters[0].id
    baseLayer = glyph.layers[baseLayerId]

    for master in Glyphs.font.masters:
      newLayer = baseLayer.copy()
      newLayer.layerId = master.id
      newLayer.name = master.name
      glyph.layers[master.id] = newLayer

  def run(self):
    for glyph in Glyphs.font.selection:
      self.syncGlyph(glyph)  
