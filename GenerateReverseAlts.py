# -*- coding: utf-8 -*-
__doc__="""
Rebuild reverse variable alternates from base glyphs
"""

from GlyphsApp import *
from Foundation import *

normalGlyphs = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'Germandbls']

specialGlyphs = [
  {
    'name': 'border_9', 
    'altName': 'border_10',
    'unicode': 'E003',
    'rotate': 180,
    'ignoreInCalt': True
  },
  {
    'name': 'border_6', 
    'altName': 'border_7',
    'unicode': 'E005',
    'rotate': 180,
    'ignoreInCalt': True
  },
  {
    'name': 'boxspiral', 
    'altName': 'boxspiral_2',
    'unicode': 'E00E',
    'rotate': 180,
    'ignoreInCalt': True,
  },
  {
    'name': 'nestedBox', 
    'altName': 'nestedDiamond',
    'unicode': 'E011',
    'rotate': 45,
    'ignoreInCalt': True,
    'width': 1019,
    'center': True
  },
]

sourceGlyphNames = normalGlyphs + map(lambda g: g['name'], specialGlyphs)  

altSuffix = '.rev'

class GenerateReverseAlts(object):

  def __init__(self, sender):
    self.setMasterVars()
    self.run()

  def setMasterVars(self):
    self.masterIds = map(lambda x: x.id, Glyphs.font.masters)
    self.reversedMasterIds = self.masterIds[:]
    self.reversedMasterIds.reverse()

    self.axisVals = map(lambda x: x.axes[0], Glyphs.font.masters)
    self.axisRange = (max(self.axisVals) - min(self.axisVals))

  def duplicatesourceGlyph(self, sourceGlyphName):
    sourceGlyph = Glyphs.font.glyphs[sourceGlyphName]
    altGlyphName = sourceGlyphName + '.rev'

    if Glyphs.font.glyphs[altGlyphName]:
      del(Glyphs.font.glyphs[altGlyphName])

    newGlyph = sourceGlyph.copy()
    newGlyph.name = altGlyphName
    newGlyph.unicode = None
    Glyphs.font.glyphs.append(newGlyph)

  def copyGlyph(self, sourceLayerMeta, sourceLayerOutlines, targetLayer):
    newLayer = sourceLayerOutlines.copy()
    newLayer.name = sourceLayerMeta.name
    newLayer.layerId = sourceLayerMeta.layerId
    newLayer.associatedMasterId = sourceLayerMeta.associatedMasterId

    targetGlyph = targetLayer.parent
    targetGlyph.layers[targetLayer.layerId] = newLayer

  def reverseMasters(self, sourceGlyphName):
    sourceGlyph = Glyphs.font.glyphs[sourceGlyphName]
    targetGlyph = Glyphs.font.glyphs[sourceGlyphName + altSuffix]

    for i, masterId in enumerate(self.masterIds):
      sourceLayerMeta = sourceGlyph.layers[masterId]
      sourceLayerOutlines = sourceGlyph.layers[self.reversedMasterIds[i]]

      self.copyGlyph(
        sourceLayerMeta, 
        sourceLayerOutlines, 
        targetGlyph.layers[masterId])

  def reverseSpecialLayers(self, sourceGlyphName):
    sourceGlyph = Glyphs.font.glyphs[sourceGlyphName]
    targetGlyph = Glyphs.font.glyphs[sourceGlyphName + altSuffix]

    for layer in targetGlyph.layers:
      if layer.isSpecialLayer:
        oldName = str(layer.name)
        
        oldAxisVal = int(oldName[oldName.find("{")+1:oldName.find("}")])
        newAxisVal = int(self.axisRange - oldAxisVal + min(self.axisVals))

        newName = oldName.replace(str(oldAxisVal), str(newAxisVal))

        oldAssociatedMasterIndex = self.masterIds.index(layer.associatedMasterId)

        newAssociatedMasterIndex = len(self.masterIds) - oldAssociatedMasterIndex - 2
        
        layer.name = newName
        layer.associatedMasterId = self.masterIds[newAssociatedMasterIndex]
        
  def updateFeatureCode(self):
    code = ""

    # classes
    code += "@skip = [" + " ".join(sourceGlyphNames) + "];\n"

    for i in range(10):
      code += self.featureDupLookup(i)

    Glyphs.font.features['calt'] = code
    Glyphs.font.updateFeatures()

  def featureDupLookup(self, skip):
    lookupName = "dup" + str(skip)
    skipCode = " ".join(map(lambda x: "@skip", range(skip)))
    code = "lookup " + lookupName + " {\n"
    ignoreList = [g for g in specialGlyphs if g['ignoreInCalt']]
    
    for sourceGlyphName in sourceGlyphNames:
      if sourceGlyphName not in ignoreList:
        code += "  sub " + sourceGlyphName + " " + skipCode + " " + sourceGlyphName + "\' by " + sourceGlyphName + altSuffix + ";\n"
    code += "} " + lookupName + ";\n"
    return code

  def rotateLayer(self, layer, degrees=0.0, xOrigin=0.0, yOrigin=0.0):
    layer.transform_checkForSelection_doComponents_( 
      rotationTransform(angle=degrees, xOrigin=xOrigin, yOrigin=yOrigin),
      False,
      True
    )

  def rotateGlyph(self, glyph, degrees):
    for layer in glyph.layers:
      x = (layer.bounds.size.width * 0.5) + layer.bounds.origin.x
      y = (layer.bounds.size.height * 0.5) + layer.bounds.origin.y
      self.rotateLayer(layer, degrees, x, y)

  def setGlyphWidth(self, glyph, width):
    for layer in glyph.layers:
      layer.width = width

  def centerGlyph(self, glyph):
    for layer in glyph.layers:
      width = layer.width
      newSB = int((layer.LSB + layer.RSB) * 0.5)
      layer.LSB = newSB
      layer.width = width

  def specialGlyphs(self):
    for specialGlyph in specialGlyphs:
      existingGlyph = Glyphs.font[specialGlyph['altName']]
      if existingGlyph:
        del(Glyphs.font.glyphs[existingGlyph.name])
        
      glyph = Glyphs.font[specialGlyph['name'] + altSuffix]
      glyph.name = specialGlyph['altName']
      glyph.unicode = specialGlyph['unicode']

      if 'rotate' in specialGlyph.keys():
        self.rotateGlyph(glyph, specialGlyph['rotate'])

      if 'width' in specialGlyph.keys():
        self.setGlyphWidth(glyph, specialGlyph['width'])

      if 'center' in specialGlyph.keys() and specialGlyph['center']:
        self.centerGlyph(glyph)


  def run(self):
    for sourceGlyphName in sourceGlyphNames:
      print sourceGlyphName
      self.duplicatesourceGlyph(sourceGlyphName)
      self.reverseMasters(sourceGlyphName)
      self.reverseSpecialLayers(sourceGlyphName)
    self.updateFeatureCode()
    self.specialGlyphs()

    Glyphs.redraw()



def rotationTransform( angle=180.0, xOrigin=0.0, yOrigin=0.0 ):
    """Returns a TransformStruct for rotating."""
    RotationTransform = NSAffineTransform.transform()
    RotationTransform.translateXBy_yBy_( xOrigin, yOrigin )
    RotationTransform.rotateByDegrees_( angle )
    RotationTransform.translateXBy_yBy_( -xOrigin, -yOrigin )
    return RotationTransform