#MenuTitle: Copy First Layer to Other Masters Selected Glyphs

# This copies the current layer and replaces all other masters in the glyph.

import GlyphsApp

def syncGlyph(glyph):
  baseLayerId = Glyphs.font.masters[0].id
  baseLayer = glyph.layers[baseLayerId]

  for master in Glyphs.font.masters:
    newLayer = baseLayer.copy()
    newLayer.layerId = master.id
    newLayer.name = master.name
    glyph.layers[master.id] = newLayer

def main():
  for glyph in Glyphs.font.selection:
    syncGlyph(glyph)  

main()