# -*- coding: utf-8 -*-
__doc__="""
Delete selected paths in all masters.
"""

from GlyphsApp import *

class DeleteSelectionInAllMasters(object):

  def __init__(self, sender):
    self.currentLayer = Glyphs.font.selectedLayers[0]
    self.glyph = self.currentLayer.parent
    self.masterIds = map(lambda m: m.id, Glyphs.font.masters) 

    self.run()

  def getSelectedContourIndexes(self):
    indexes = []
    for i in range(len(self.currentLayer.shapes)):
      if self.currentLayer.shapes[i].selected:
        indexes.append(i)

    return sorted(indexes, reverse=True)

  def deleteIndexesInLayer(self, indexes, layer):
    for i in indexes:
      if (len(layer.shapes) - 1) >= i:
        del(layer.shapes[i])

  def run(self):
    selectedIndexes = self.getSelectedContourIndexes()
    for layer in self.glyph.layers:
      self.deleteIndexesInLayer(selectedIndexes, layer)

    Glyphs.redraw()


  