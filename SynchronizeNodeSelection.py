#MenuTitle: Synchronize node selection
# -*- coding: utf-8 -*-
__doc__="""
Synchronize which nodes are selected in all of your masters/layers.
"""

# Ethan Cohen. Updated 8/8/2020.

import GlyphsApp

currentLayer = Font.selectedLayers[0]
g = currentLayer.parent
otherLayers = [l for l in g.layers if l != currentLayer]

for layer in otherLayers:
	layer.clearSelection()
for path in range(len(currentLayer.paths)):
	for node in currentLayer.paths[path].nodes:
		if node.selected:
			for layer in otherLayers:
				if path < len(layer.paths):
					if node.index < layer.paths[path].nodes:
						layer.paths[path].nodes[node.index].selected = True