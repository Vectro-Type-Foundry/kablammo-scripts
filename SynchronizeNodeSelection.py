# -*- coding: utf-8 -*-
__doc__="""
Synchronize which nodes are selected in all of your masters/layers.
"""

# Ethan Cohen. Updated 8/8/2020.

from GlyphsApp import *

class SynchronizeNodeSelection(object):

  def __init__(self, sender):
    self.run()

  def run(self):
    currentLayer = Glyphs.font.selectedLayers[0]
    g = currentLayer.parent
    otherLayers = [l for l in g.layers if l != currentLayer]

    for layer in otherLayers:
      layer.clearSelection()
    for pathIndex in range(len(currentLayer.paths)):
      for node in currentLayer.paths[pathIndex].nodes:
        if node.selected:
          for layer in otherLayers:
            if (len(layer.paths) >= len(currentLayer.paths)):
              targetPath = layer.paths[pathIndex]
              if (len(targetPath.nodes) >= len(currentLayer.paths[pathIndex].nodes)):
                targetNode = targetPath.nodes[node.index]
                targetNode.selected = True