#MenuTitle: Delete selection in all masters
# -*- coding: utf-8 -*-
__doc__="""
Delete selected paths in all masters.
"""

import GlyphsApp

currentLayer = Font.selectedLayers[0]
glyph = currentLayer.parent
masterIds = map(lambda m: m.id, Font.masters) 

def getSelectedContourIndexes():
  indexes = []
  for i in range(len(currentLayer.paths)):
    if currentLayer.paths[i].selected:
      indexes.append(i)

  return sorted(indexes, reverse=True)

def deleteIndexesInLayer(indexes, layer):
  for i in indexes:
    del(layer.paths[i])

def main():
  selectedIndexes = getSelectedContourIndexes()

  for masterId in masterIds:
    deleteIndexesInLayer(selectedIndexes, glyph.layers[masterId])


main()

Glyphs.redraw()