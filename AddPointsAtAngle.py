# -*- coding: utf-8 -*-
__doc__="""
Adds points at specific angle
"""

# Modified version of this https://forum.glyphsapp.com/t/adding-points-at-specified-angle/5616/3

from GlyphsApp import *
from collections import OrderedDict

class AddPointsAtAngle(object):

  def __init__(self, angle):
    self.setAngles(angle)
    
    # precision
    self.timeStep = 0.005

    self.run()

  def setAngles(self, angle):
    angle1 = angle

    # reflected angles
    angle2 = angle1 + 180 if angle1 <= 90 else angle1 - 180
    angle3 = angle1 * -1 
    angle4 = angle3 + 180 if angle3 <= 90 else angle3 - 180

    self.angles = [ angle, angle2, angle3, angle4 ]

  def segmentSelected(self, currentNode, allNodes, i):
    nextIndex = i-1
    # if nextIndex >= len(allNodes):
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
        if node.type != "offcurve":
          onCurveNodes.append( {
            "nodeTime": node.index,
            "selected": node.selected
            } )

      tangentPoints = {}
      for i, onCurveNode in enumerate(onCurveNodes):
        if self.segmentSelected(onCurveNode, onCurveNodes, i):

          nodeTime = onCurveNode["nodeTime"]
          endTime = nodeTime + 1
          while nodeTime < endTime:
            # Creates a temporary path so we don't mess with the original
            # until we find the correct point.
            tempPath = layer.paths[0].copy()
            # Creates a node in our fake path at the current time...
            nearestNode = tempPath.insertNodeWithPathTime_( nodeTime )
            # ... so we can get its tangent angle.
            tangentAngle = tempPath.tangentAngleAtNode_direction_(nearestNode, 1)
            # If the tangent angle matches, store the current time in the dict 
            # and skip the rest of this segment.
            if int(tangentAngle) in self.angles:
              tangentPoints[nodeTime] = nearestNode
              break
            nodeTime += self.timeStep
      
      # Now, creates an ordered dict from the results.
      # This dict is sorted from largest to smallest time so we can simply insert 
      # the nodes, not worrying about their new indexes.
      orderedPoints = OrderedDict( sorted(tangentPoints.items(), reverse=True) )
      for time, point in orderedPoints.items():
        # Insert the new nodes and profit!
        path.insertNodeWithPathTime_( time )

