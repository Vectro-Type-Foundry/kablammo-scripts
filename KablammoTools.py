#MenuTitle: KablammoTools
# -*- coding: utf-8 -*-
__doc__="""
Brings up window with easy access to all scripts
"""
import sys; sys.dont_write_bytecode = True
from vanilla import *
from CollapseHandles import *
from CollapseShape import *
from SyncToFirstLayerSelected import *
from DuplexWarnings import *
from UseLayerForAllMasters import *
from CopySelectionToOtherMasters import * 
from DeleteSelectionInAllMasters import *
from SynchronizeNodeSelection import *
from AddPointsAtAngle import *
from AddHandlesToStraightSegments import *
from AddMidpoints import *
from GenerateReverseAlts import *
from Jiggle import *

class KablammoTools(object):

  def __init__(self):
    self.w = Window((200, 430), "Kablammo Tools", minSize=(100, 100))
    self.w.g1 = Group((10, 10, -10, -10))

    bHeight = 27
    bSize = "small"
    margin = 10 + bHeight
    y = 0

    self.w.g1.collapseHandles = SquareButton((0, y, 0, bHeight), "Collapse Handles", sizeStyle=bSize, callback=CollapseHandles)

    y+=margin

    self.w.g1.collapseShape = SquareButton((0, y, 0, bHeight), "Collapse Shape", sizeStyle=bSize, callback=CollapseShape)

    y+=margin

    self.w.g1.UseLayerForAllMasters = SquareButton((0, y, 0, bHeight), "Use Current Layer for All", sizeStyle=bSize, callback=UseLayerForAllMasters)

    y+=margin

    self.w.g1.copyFirstLayerToAllSelected = SquareButton((0, y, 0, bHeight), "Use 1st Layer for All, Selected Glyphs", sizeStyle=bSize, callback=SyncToFirstLayerSelected)

    y+=margin

    self.w.g1.CopySelectionToOtherMasters = SquareButton((0, y, 0, bHeight), "Copy Selection to All Masters", sizeStyle=bSize, callback=CopySelectionToOtherMasters)

    y+=margin

    self.w.g1.DeleteSelectionInAllMasters = SquareButton((0, y, 0, bHeight), "Delete Selection in All Masters", sizeStyle=bSize, callback=DeleteSelectionInAllMasters)

    y+=margin


    self.w.g1.SynchronizeNodeSelection = SquareButton((0, y, 0, bHeight), "Sync Node Selection", sizeStyle=bSize, callback=SynchronizeNodeSelection)

    y+=margin

    self.w.g1.duplexWarnings = SquareButton((0, y, 0, bHeight), "Duplex Warnings", sizeStyle=bSize, callback=DuplexWarnings)
    
    y+=margin

    self.addPointsAtAngleAngle = 45

    self.w.g1.addPointsAtAngleAngleInput = EditText((0, y, 40, bHeight), text=self.addPointsAtAngleAngle, callback=self.addPointsAtAngleAngleCallback)

    self.w.g1.addPointsAtAngle = SquareButton((50, y, 0, bHeight), "Add Points at Angle", sizeStyle=bSize, callback=self.addPointsAtAngleCallback)
    
    y+=margin

    self.w.g1.Jiggle = SquareButton((0, y, 0, bHeight), "Jiggle", sizeStyle=bSize, callback=Jiggle)
    
    y+=margin

    self.w.g1.GenerateReverseAlts = SquareButton((0, y, 0, bHeight), "Generate Reverse Alts", sizeStyle=bSize, callback=GenerateReverseAlts)
    
    y+=margin

    self.w.open()

  def addPointsAtAngleAngleCallback(self, sender):
    try:
      self.addPointsAtAngleAngle = int(sender.get())
    except:
      print('not a valid value for angle')

  def addPointsAtAngleCallback(self, sender):
    AddPointsAtAngle(self.addPointsAtAngleAngle)

  def test(self, v):
    DuplexWarnings()

KablammoTools()