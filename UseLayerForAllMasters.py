# This copies the current layer and replaces all other masters in the glyph.

from GlyphsApp import *

class UseLayerForAllMasters(object):

  def __init__(self, sender):
    self.run()

  def run(self):
    currentLayer = Glyphs.font.selectedLayers[0]
    currentGlyph = currentLayer.parent
    for master in Glyphs.font.masters:
      newLayer = currentLayer.copy()
      newLayer.layerId = master.id
      newLayer.name = master.name
      currentGlyph.layers[master.id] = newLayer
