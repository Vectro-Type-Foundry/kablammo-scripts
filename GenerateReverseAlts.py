# -*- coding: utf-8 -*-
__doc__="""
Rebuild reverse variable alternates from base glyphs
"""

from GlyphsApp import *
from Foundation import *

normalGlyphs = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Oslash', 'OE', 'Thorn', 'Schwa', 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'A-cy', 'Be-cy', 'Ve-cy', 'Ge-cy', 'De-cy', 'Ie-cy', 'Iegrave-cy', 'Io-cy', 'Zhe-cy', 'Ze-cy', 'Ii-cy', 'Iigrave-cy', 'Iishort-cy', 'Ka-cy', 'El-cy', 'Em-cy', 'En-cy', 'O-cy', 'Pe-cy', 'Er-cy', 'Es-cy', 'Te-cy', 'U-cy', 'Ef-cy', 'Ha-cy', 'Tse-cy', 'Che-cy', 'Sha-cy', 'Shcha-cy', 'Hardsign-cy', 'Yeru-cy', 'Softsign-cy', 'Ereversed-cy', 'Iu-cy', 'Ia-cy', 'I-cy', 'Yi-cy', 'Ushort-cy', 'Fita-cy', 'Izhitsa-cy', 'Yat-cy', 'E-cy', 'Gje-cy', 'Gheupturn-cy', 'period', 'comma', 'exclam', 'exclamdown', 'question', 'questiondown', 'periodcentered', 'asterisk', 'slash', 'backslash', 'parenleft', 'parenright', 'braceleft', 'braceright', 'bracketleft', 'bracketright', 'hyphen', 'endash', 'emdash', 'underscore', 'quotesinglbase', 'quotedblbase', 'quotedblleft', 'quotedblright', 'quoteleft', 'quoteright', 'guillemetleft', 'guillemetright', 'guilsinglleft', 'guilsinglright', 'currency', 'dollar', 'euro', 'plus', 'equal', 'greater', 'less', 'percent', 'upArrow', 'northEastArrow', 'rightArrow', 'southEastArrow', 'downArrow', 'southWestArrow', 'leftArrow', 'northWestArrow', 'leftRightArrow', 'upDownArrow', 'at', 'ampersand']

glyphGroups = [
  {
    'key': 'A',
    'glyphs': ['Aacute', 'Abreve', 'Abreveacute', 'Abrevedotbelow', 'Abrevegrave', 'Abrevehookabove', 'Abrevetilde', 'Acircumflex', 'Acircumflexacute', 'Acircumflexdotbelow', 'Acircumflexgrave', 'Acircumflexhookabove', 'Acircumflextilde', 'Adblgrave', 'Adieresis', 'Adotbelow', 'Agrave', 'Ahookabove', 'Ainvertedbreve', 'Amacron', 'Aogonek', 'Aring', 'Aringacute', 'Atilde']
  },
  {
  	'key': 'C',
  	'glyphs': ['Cacute', 'Ccaron', 'Ccedilla', 'Ccedillaacute', 'Ccircumflex', 'Cdotaccent']
  },
  {
    'key': 'D',
    'glyphs': ['Eth', 'Dcaron', 'Dcroat', 'Ddotbelow', 'Dlinebelow']
  },
  {
    'key': 'E',
    'glyphs': ['Eacute', 'Ebreve', 'Ecaron', 'Ecedillabreve', 'Ecircumflex', 'Ecircumflexacute', 'Ecircumflexdotbelow', 'Ecircumflexgrave', 'Ecircumflexhookabove', 'Ecircumflextilde', 'Edblgrave', 'Edieresis', 'Edotaccent', 'Edotbelow', 'Egrave', 'Ehookabove', 'Einvertedbreve', 'Emacron', 'Emacronacute', 'Emacrongrave', 'Eogonek', 'Etilde']
  },
  {
    'key': 'G',
    'glyphs': ['Gbreve', 'Gcaron', 'Gcircumflex', 'Gcommaaccent', 'Gdotaccent', 'Gmacron']
  },
  {
    'key': 'H',
    'glyphs': ['Hbar', 'Hbrevebelow', 'Hcircumflex', 'Hdotbelow']
  },
  {
    'key': 'I',
    'glyphs': ['Iacute', 'Ibreve', 'Icircumflex', 'Idblgrave', 'Idieresis', 'Idieresisacute', 'Idotaccent', 'Idotbelow', 'Igrave', 'Ihookabove', 'Iinvertedbreve', 'Imacron', 'Iogonek', 'Itilde']
  },
  {
    'key': 'J',
    'glyphs': ['Jacute', 'Jcircumflex']
  },
  {
    'key': 'K',
    'glyphs': ['Kcommaaccent']
  },
  {
    'key': 'L',
    'glyphs': ['Lacute', 'Lcaron', 'Lcommaaccent', 'Ldot', 'Ldotbelow', 'Llinebelow', 'Lslash']
  },
  {
    'key': 'M',
    'glyphs': ['Mdotbelow']
  },
  {
    'key': 'N',
    'glyphs': ['Nacute', 'Ncaron', 'Ncommaaccent', 'Ndotaccent', 'Ndotbelow', 'Nlinebelow', 'Ntilde']
  },
  {
    'key': 'O',
    'glyphs': ['Oacute', 'Obreve', 'Ocircumflex', 'Ocircumflexacute', 'Ocircumflexdotbelow', 'Ocircumflexgrave', 'Ocircumflexhookabove', 'Ocircumflextilde', 'Odblgrave', 'Odieresis', 'Odieresismacron', 'Odotaccentmacron', 'Odotbelow', 'Ograve', 'Ohookabove', 'Ohorn', 'Ohornacute', 'Ohorndotbelow', 'Ohorngrave', 'Ohornhookabove', 'Ohorntilde', 'Ohungarumlaut', 'Oinvertedbreve', 'Omacron', 'Omacronacute', 'Omacrongrave', 'Oogonek', 'Otilde', 'Otildeacute', 'Otildedieresis', 'Otildemacron']
  },
  {
    'key': 'Oslash',
    'glyphs': ['Oslashacute']
  },
  {
    'key': 'R',
    'glyphs': ['Racute', 'Rcaron', 'Rcommaaccent', 'Rdblgrave', 'Rdotbelow', 'Rinvertedbreve', 'Rlinebelow']
  },
  {
    'key': 'S',
    'glyphs': ['Sacute', 'Sacutedotaccent', 'Scaron', 'Scarondotaccent', 'Scedilla', 'Scircumflex', 'Scommaaccent', 'Sdotaccent', 'Sdotbelow', 'Sdotbelowdotaccent']
  },
  {
    'key': 'T',
    'glyphs': ['Tbar', 'Tcaron', 'Tcedilla', 'Tcommaaccent', 'Tdotbelow', 'Tlinebelow']
  },
  {
    'key': 'U',
    'glyphs': ['Uacute', 'Ubreve', 'Ucircumflex', 'Udblgrave', 'Udieresis', 'Udotbelow', 'Ugrave', 'Uhookabove', 'Uhorn', 'Uhornacute', 'Uhorndotbelow', 'Uhorngrave', 'Uhornhookabove', 'Uhorntilde', 'Uhungarumlaut', 'Uinvertedbreve', 'Umacron', 'Umacrondieresis', 'Uogonek', 'Uring', 'Utilde', 'Utildeacute']
  },
  {
    'key': 'W',
    'glyphs': ['Wacute', 'Wcircumflex', 'Wdieresis', 'Wgrave']
  },
  {
    'key': 'Y',
    'glyphs': ['Yacute', 'Ycircumflex', 'Ydieresis', 'Ydotaccent', 'Ydotbelow', 'Ygrave', 'Yhookabove', 'Ymacron', 'Ytilde']
  },
  {
    'key': 'Z',
    'glyphs': ['Zacute', 'Zcaron', 'Zdotaccent', 'Zdotbelow']
  },
]

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
    'width': 2040,
    'center': True
  }
]

ignoreInCaltList = [g['name'] for g in specialGlyphs if g['ignoreInCalt']]
specialGlyphsNameList = [g['name'] for g in specialGlyphs]

sourceGlyphNames = normalGlyphs + map(lambda g: g['name'], specialGlyphs)
sourceGlyphNamesFromGroups = [g for glyphGroup in glyphGroups for g in glyphGroup['glyphs']]

sourceGlyphNamesIncludingGroups = sourceGlyphNames + sourceGlyphNamesFromGroups

caltGlyphNames = [g for g in sourceGlyphNames if (g not in ignoreInCaltList)]
caltGlyphNamesIncludingGroups = caltGlyphNames + sourceGlyphNamesFromGroups

altSuffix = '.rev'

# build feature code
#  if in groups list, use class syntax
#  add to ignore glyphs


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
    altGlyphName = sourceGlyphName + altSuffix

    if Glyphs.font.glyphs[altGlyphName]:
      del(Glyphs.font.glyphs[altGlyphName])

    newGlyph = sourceGlyph.copy()
    newGlyph.name = altGlyphName
    newGlyph.unicode = None
    newGlyph.color = 11

    Glyphs.font.glyphs.append(newGlyph)

  def copyGlyph(self, sourceLayerMeta, sourceLayer, targetLayer):
    newLayer = sourceLayer.copyDecomposedLayer()
    # newLayer.decomposeComponents()
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
      sourceLayer = sourceGlyph.layers[self.reversedMasterIds[i]]

      self.copyGlyph(
        sourceLayerMeta, 
        sourceLayer, 
        targetGlyph.layers[masterId])

  def reverseSpecialLayers(self, sourceGlyphName):
    sourceGlyph = Glyphs.font.glyphs[sourceGlyphName]
    targetGlyph = Glyphs.font.glyphs[sourceGlyphName + altSuffix]

    for layer in targetGlyph.layers:
      if layer.isSpecialLayer:
        oldName = str(layer.name)
        
        oldAxisVal = int(oldName[oldName.find("{")+1:oldName.find("}")])
        newAxisVal = int(self.axisRange - oldAxisVal + min(self.axisVals))
        if newAxisVal == 167:
          newAxisVal = 166
        elif newAxisVal == 834:
          newAxisVal = 833

        newName = oldName.replace(str(oldAxisVal), str(newAxisVal))

        oldAssociatedMasterIndex = self.masterIds.index(layer.associatedMasterId)

        newAssociatedMasterIndex = len(self.masterIds) - oldAssociatedMasterIndex - 2
        
        layer.name = newName
        layer.associatedMasterId = self.masterIds[newAssociatedMasterIndex]

  def getAltName(self, name):
    if name in specialGlyphsNameList:
      specialGlyph = filter(lambda sg: sg['name'] == g, specialGlyphsNameList)[0]
      return specialGlyph['altname']
    else:
      return name + altSuffix

  def alt1ClassList(self):
    return [g for g in sourceGlyphNames if (g not in ignoreInCaltList)]

  def alt2ClassList(self):
    return [self.getAltName(g) for g in self.alt1ClassList()]

  def skipClassList(self):
    normalGlyphs = [g for g in sourceGlyphNames if (g not in ignoreInCaltList)]
    altGlyphs = []
    for g in sourceGlyphNames:
      if g not in ignoreInCaltList:
        altGlyphs.append(self.getAltName(g))
    return normalGlyphs + altGlyphs

  def glyphsNotInGroup(self, glyphName):
    matchingGroups = filter(lambda glyphGroup: glyphGroup['key'] == glyphName, glyphGroups)
    excludeList = []
    if len(matchingGroups) > 0:
      excludeList = [matchingGroups[0]['key']] + matchingGroups[0]['glyphs']
    else:
      excludeList = [glyphName]
    
    return filter(lambda g: g not in excludeList, caltGlyphNamesIncludingGroups)

  def skipClasses(self):
    code = ""
    for glyph in caltGlyphNames:
      glyphs1 = self.glyphsNotInGroup(glyph)
      glyphs2 = [self.getAltName(g) for g in glyphs1]
      code += "@skip" + glyph + " = [" + " ".join(glyphs1) + " " + " ".join(glyphs2) + "];\n"
    return code

  def groupClasses(self):
    code = ""
    for group in glyphGroups:
      code += "@" + group['key'] + "1 = [" + group['key'] + " " + " ".join(group['glyphs']) + "];\n"
      
      altGlyphs = [self.getAltName(g) for g in group['glyphs']]
      code += "@" + group['key'] + "2 = [" + self.getAltName(group['key']) + " " + " ".join(altGlyphs) + "];\n"

    return code

  def generateClasses(self):
    code = ""
    code += self.skipClasses()
    code += self.groupClasses()
    # put them in prefix
    Glyphs.font.featurePrefixes['caltClasses'] = code


  def generateGlobalLookups(self):
    code = ""
    # lookup lookup_0 {
    #   sub A by A.rev;
    #   sub Aacute by Aacute.rev;
    #   ...
    # } lookup_0;

    # lookup lookup_1 {
    #   sub A.rev by A;
    #   sub Aacute.rev by Aacute;
    # ...
    # } lookup_1;

    code += "lookup calt1 {\n"
    for glyphName in caltGlyphNames:
      code += "sub " + glyphName + " by " + self.getAltName(glyphName) + ";\n"
    code += "} calt1;\n"

    code += "lookup calt2 {\n"
    for glyphName in caltGlyphNames:
      code += "  sub " + self.getAltName(glyphName) + " by " + glyphName + ";\n"
    code += "} calt2;\n"
    Glyphs.font.featurePrefixes['caltLookups'] = code

  def updateFeatureCode(self):
    code = ""
    self.generateClasses()
    self.generateGlobalLookups()

    contextRange1 = 10
    contextRange2 = 10

    for i in range(contextRange1):
      code += self.featureDupLookup(i, False)

    for i in range(contextRange2):
      code += self.featureDupLookup(i, True)

    Glyphs.font.features['calt'] = code
    Glyphs.font.updateFeatures()


  def classOrBaseSub(self, glyphName, position):
    matchingGroups = filter(lambda glyphGroup: glyphGroup['key'] == glyphName, glyphGroups)
    if len(matchingGroups) > 0:
      return "@" + glyphName + str(position)
    else:
      if position == 1:
        return glyphName
      else:
        return self.getAltName(glyphName)

  def chunkifyList(self, l, n):
    for i in range(0, len(l), n): 
      yield l[i:i + n]

  def featureDupLookup(self, skip, rev):
    code = ""
    revTag = 'r' if rev else ''
    maxSubGroupSize = 1000
    glyphNameChunks = self.chunkifyList(caltGlyphNames, maxSubGroupSize)

    for i, glyphNameChunk in enumerate(glyphNameChunks):
      tagName = "skip" + str(skip) + revTag
      code += "lookup " + tagName + " useExtension {\n"

      for sourceGlyphName in glyphNameChunk:
        
        skipCode = " ".join(map(lambda x: "@skip" + sourceGlyphName, range(skip)))
        targetGlyph = self.classOrBaseSub(sourceGlyphName, 1)
        # replacementGlyph = self.classOrBaseSub(sourceGlyphName, 2)
        replacementLookup = 'calt1'

        if rev:
          targetGlyph = self.classOrBaseSub(sourceGlyphName, 2)
          # replacementGlyph = self.classOrBaseSub(sourceGlyphName, 1)
          replacementLookup = 'calt2'

        code += "  sub " + targetGlyph + " " + skipCode + " " + targetGlyph + "\' lookup " + replacementLookup + ";\n"

      code += "} " + tagName + ";\n"

    return code

  def rotateLayer(self, layer, degrees=0.0, xOrigin=0.0, yOrigin=0.0):
    newLSB = layer.RSB
    width = layer.width
    layer.transform_checkForSelection_doComponents_( 
      rotationTransform(angle=degrees, xOrigin=xOrigin, yOrigin=yOrigin),
      False,
      True
    )
    layer.LSB = newLSB
    layer.width = width

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
    # for sourceGlyphName in sourceGlyphNamesIncludingGroups:
      # self.duplicatesourceGlyph(sourceGlyphName)
      # self.reverseMasters(sourceGlyphName)
      # self.reverseSpecialLayers(sourceGlyphName)
    self.updateFeatureCode()
    # self.specialGlyphs()

    Glyphs.redraw()



def rotationTransform( angle=180.0, xOrigin=0.0, yOrigin=0.0 ):
    """Returns a TransformStruct for rotating."""
    RotationTransform = NSAffineTransform.transform()
    RotationTransform.translateXBy_yBy_( xOrigin, yOrigin )
    RotationTransform.rotateByDegrees_( angle )
    RotationTransform.translateXBy_yBy_( -xOrigin, -yOrigin )
    return RotationTransform



## OT structure

# // external lookups 

# lookup lookup_0 {
#   sub A by A.rev;
#   sub Aacute by Aacute.rev;
#   ...
# } lookup_0;

# lookup lookup_1 {
#   sub A.rev by A;
#   sub Aacute.rev by Aacute;
# ...
# } lookup_1;


# // in calt
# // one section for each skip round?

# lookup calt0 {
# 	sub @A_1 @A_2' lookup lookup_0 ;
# 	sub B B' lookup lookup_0 ;
#   ...
# } calt0;
# lookup calt1 {
# 	sub @A_1 @skip_A @A_1' lookup lookup_0 ;
# 	sub B @skip_B B' lookup lookup_0 ;
#   ...
# } calt1;

# ///....
# // rev time

# lookup calt7 {
# 	sub @A_2 @A_2' lookup lookup_1 ;
# 	sub B.rev B.rev' lookup lookup_1 ;
#   ...
# } calt7;
# lookup calt8 {
#   sub @A_2 @skip_A @A_2' lookup lookup_1 ;
# 	sub B.rev @skip_B B.rev' lookup lookup_1;
# } calt8;
