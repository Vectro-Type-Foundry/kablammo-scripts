
# -*- coding: utf-8 -*-
__doc__="""
Adds midpoints to selected segments
"""

# Modified version of this https://forum.glyphsapp.com/t/adding-points-at-specified-angle/5616/3

from GlyphsApp import *
from collections import OrderedDict

class AddMidpoints(object):

  def __init__(self, sender):
    self.run()

  def segmentSelected(self, currentNode, allNodes, i):
    nextIndex = i-1
    if nextIndex < 0:
      nextIndex = len(allNodes) - 1

    return currentNode["selected"] and allNodes[nextIndex]["selected"]
    

  def run(self):
    font = Glyphs.font
    layer = font.selectedLayers[0]

    for path in layer.paths:
      # Creates a list of indexes of oncurve nodes.
      # Only oncurve nodes can be used to sweep a path using time. 
      onCurveNodes = []
      for node in path.nodes:
        if node.type == "curve":
          onCurveNodes.append( {
            "nodeTime": node.index,
            "selected": node.selected
            } )

      times = []

      for i, onCurveNode in enumerate(onCurveNodes):
        if self.segmentSelected(onCurveNode, onCurveNodes, i):

          nodeTime = onCurveNode["nodeTime"]
          endTime = nodeTime + 1
          midTime = ((endTime - nodeTime) * .5) + nodeTime
          times.append(midTime)          

      # orderedPoints = OrderedDict( sorted(tangentPoints.items(), reverse=True) )
      times.reverse()
      for i, time in enumerate(times):
        # Insert the new nodes and profit!
        path.insertNodeWithPathTime_(time)
