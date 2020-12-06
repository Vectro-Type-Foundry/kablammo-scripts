# -*- coding: utf-8 -*-
__doc__="""
Jiggles Selected Dots and Spots
"""

from GlyphsApp import *
import random

class Jiggle(object):

  def __init__(self, sender):
    self.anchorRange = 0.2
    self.handleRange = 0.2

    self.run()

  def selectedPaths(self): 
    return filter(lambda x: x.selected , Glyphs.font.selectedLayers[0].paths)

  def getAnchorIndexes(self, path):
    indexes = []
    for node in path.nodes:
      if node.type != 'offcurve':
        indexes.append(node.index)

    return indexes

  def randomPosNeg(self):
    return 1 if random.random() < 0.5 else -1


  def getReferenceNode(self, node):
    if node.type == 'offcurve':
      return self.getHandleReference(node)
    else: 
      return self.getAnchorReference(node)

  def getAnchorReference(self, node):
    direction = self.randomPosNeg()

    if direction > 0:
      return node.nextNode
    else:
      return node.prevNode

  def getHandleReference(self, node):
    if node.nextNode.type != 'offcurve':
      return node.nextNode
    else:
      return node.prevNode

  def jigglePath(self, path):
    for node in path.nodes:
      self.jiggleNode(node)

  def jiggleNode(self, node):
    refNode = self.getReferenceNode(node)
    randX = self.anchorRange * random.random()
    randY = self.anchorRange * random.random()

    x = ((node.position.x - refNode.position.x) * randX) + node.position.x
    y = ((node.position.y - refNode.position.y) * randY) + node.position.y

    node.position = (x, y)

  def run(self):
    for path in self.selectedPaths():
      self.jigglePath(path)

