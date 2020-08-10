#MenuTitle: Check if Duplex
# -*- coding: utf-8 -*-
__doc__="""
In selection, alert in console if any glyphs are not duplexed, or same width across masters.
"""

# Travis Kochel. Updated August 10, 2020.

import GlyphsApp

currentLayer = Font.selectedLayers[0]
glyph = currentLayer.parent
primaryLayerNames = [m.name for m in Font.masters]


def main():
  print('Inconsistent Widths')

  for glyph in Font.selection:
    layers = [l for l in glyph.layers if l.name in primaryLayerNames]
    widths = [l.width for l in layers]
    if len(set(widths)) > 1:
      print(str(glyph.name) + ': ', widths)


main()