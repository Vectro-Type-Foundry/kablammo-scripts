#MenuTitle: Copy Layer to Other Masters Current Glyph

# This copies the current layer and replaces all other masters in the glyph.

import GlyphsApp

currentLayer = Glyphs.font.selectedLayers[0]
currentGlyph = currentLayer.parent

def main():
  for master in Glyphs.font.masters:
    newLayer = currentLayer.copy()
    newLayer.layerId = master.id
    newLayer.name = master.name
    currentGlyph.layers[master.id] = newLayer

main()