# -*- coding: utf-8 -*-
__doc__="""
Rebuild reverse variable alternates from base glyphs
"""

from GlyphsApp import *
from Foundation import *

contextRange = 10
contextRangeRev = 10
# normalGlyphs = ["Aacute"]
normalGlyphs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Oslash", "OE", "Thorn", "Schwa", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "A-cy", "Be-cy", "Ve-cy", "Ge-cy", "De-cy", "Ie-cy", "Zhe-cy", "Ze-cy", "Ii-cy", "Ka-cy", "El-cy", "Em-cy", "En-cy", "O-cy", "Fita-cy", "Obarred-cy", "Pe-cy", "Er-cy", "Es-cy", "Te-cy", "U-cy", "Ef-cy", "Ha-cy", "Che-cy", "Tse-cy", "Sha-cy", "Shcha-cy", "Dzhe-cy", "Softsign-cy", "Hardsign-cy", "Yeru-cy", "Dze-cy", "Ereversed-cy", "E-cy", "I-cy", "Je-cy", "Tshe-cy", "Dje-cy", "Ghemiddlehook-cy", "Iu-cy", "Ia-cy", "Yusbig-cy", "Haabkhasian-cy", "Ustraight-cy", "Shha-cy", "Cheabkhasian-cy", "Schwa-cy", "Qa-cy", "We-cy", "Dzeabkhasian-cy", "period", "comma", "exclam", "exclamdown", "question", "questiondown", "periodcentered", "asterisk", "slash", "backslash", "parenleft", "parenright", "braceleft", "braceright", "bracketleft", "bracketright", "hyphen", "endash", "emdash", "underscore", "quotesinglbase", "quotedblbase", "quotedblleft", "quotedblright", "quoteleft", "quoteright", "guillemetleft", "guillemetright", "guilsinglleft", "guilsinglright", "dollar", "euro", "plus", "equal", "greater", "less", "percent", "at", "ampersand", "cedi", "colonsign", "dong", "franc", "guarani", "hryvnia", "kip", "lira", "liraTurkish", "manat", "naira", "peseta", "peso", "ruble", "rupeeIndian", "sterling", "tenge", "tugrik", "won", "yen"]

normalGlyphs = ["A"]

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
  {
    'key': 'A-cy',
    'glyphs': ['Abreve-cy', 'Adieresis-cy']
  },
  {
    'key': 'Ge-cy',
    'glyphs': ['Gje-cy', 'Gheupturn-cy', 'Ghestroke-cy', 'Gedescender-cy', 'Gestrokehook-cy']
  },
  {
    'key': 'Ie-cy',
    'glyphs': ['Iegrave-cy', 'Io-cy', 'Iebreve-cy']
  },
  {
    'key': 'Zhe-cy',
    'glyphs': ['Zhedescender-cy', 'Zhebreve-cy', 'Zhedieresis-cy']
  },
  {
    'key': 'Ze-cy',
    'glyphs': ['Zedescender-cy', 'Zedieresis-cy', 'Reversedze-cy']
  },
  {
    'key': 'Ii-cy',
    'glyphs': ['Iishort-cy', 'Iigrave-cy', 'Iishorttail-cy', 'Imacron-cy', 'Idieresis-cy']
  }, 
  {
    'key': 'Ka-cy',
    'glyphs': ['Kje-cy', 'Kadescender-cy', 'Kaverticalstroke-cy', 'Kastroke-cy', 'Kabashkir-cy', 'Kahook-cy']
  },
  {
    'key': 'El-cy',
    'glyphs': ['Eltail-cy', 'Elhook-cy', 'Eldescender-cy']
  },
  {
    'key': 'Em-cy',
    'glyphs': ['Emtail-cy']
  },
  {
    'key': 'En-cy',
    'glyphs': ['Nje-cy', 'Enghe-cy', 'Enhook-cy', 'EnLeftHook-cy']
  },
  {
    'key': 'O-cy',
    'glyphs': ['Odieresis-cy']
  },
  {
    'key': 'Obarred-cy',
    'glyphs': ['Obarreddieresis-cy']
  },
  {
    'key': 'Pe-cy',
    'glyphs': ['Pedescender-cy']
  },
  {
    'key': 'Er-cy',
    'glyphs': ['Ertick-cy']
  },
  {
    'key': 'Es-cy',
    'glyphs': ['Esdescender-cy']
  },
  {
    'key': 'Te-cy',
    'glyphs': ['Tedescender-cy', 'Tetse-cy']
  },
  {
    'key': 'U-cy',
    'glyphs': ['Ushort-cy', 'Umacron-cy', 'Udieresis-cy', 'Uhungarumlaut-cy']
  },
  {
    'key': 'Ha-cy',
    'glyphs': ['Hadescender-cy', 'Hahook-cy', 'Hastroke-cy']
  },
  {
    'key': 'Che-cy',
    'glyphs': ['Chedescender-cy', 'Cheverticalstroke-cy', 'Chekhakassian-cy', 'Chedieresis-cy']
  },
  {
    'key': 'Softsign-cy',
    'glyphs': ['Lje-cy', 'Yat-cy', 'Semisoftsign-cy']
  },
  {
    'key': 'Yeru-cy',
    'glyphs': ['Yerudieresis-cy']
  },
  {
    'key': 'Ereversed-cy',
    'glyphs': ['Edieresis-cy']
  },
  {
    'key': 'I-cy',
    'glyphs': ['Yi-cy', 'Palochka-cy']
  },
  {
    'key': 'Ustraight-cy',
    'glyphs': ['Ustraightstroke-cy']
  },
  {
    'key': 'Shha-cy',
    'glyphs': ['Shhadescender-cy']
  },
  {
    'key': 'Cheabkhasian-cy',
    'glyphs': ['Chedescenderabkhasian-cy']
  },
  {
    'key': 'Schwa-cy',
    'glyphs': ['Schwadieresis-cy']
  },
]
glyphGroups = [
  {
    'key': 'A',
    'glyphs': []
  }
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
specialGlyphs = []

universalSkipGlyphs = ['space']

ignoreInCaltList = [g['name'] for g in specialGlyphs if g['ignoreInCalt']]
specialGlyphsNameList = [g['name'] for g in specialGlyphs]

sourceGlyphNames = normalGlyphs + list(map(lambda g: g['name'], specialGlyphs))
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
    self.masterIds = list(map(lambda x: x.id, Glyphs.font.masters))
    self.reversedMasterIds = self.masterIds[:]
    self.reversedMasterIds.reverse()

    self.axisVals = list(map(lambda x: x.axes[0], Glyphs.font.masters))
    self.axisRange = (max(self.axisVals) - min(self.axisVals))
    self.axisId = Glyphs.font.axes[0].axisId

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

  def copyLayer(self, sourceLayerMeta, sourceLayer, targetLayer):
    newLayer = sourceLayer.copyDecomposedLayer()
    newLayer.name = sourceLayerMeta.name
    newLayer.layerId = sourceLayerMeta.layerId
    newLayer.associatedMasterId = sourceLayerMeta.associatedMasterId

    targetGlyph = targetLayer.parent
    targetGlyph.layers[targetLayer.layerId] = newLayer

  def reverseMasters(self, sourceGlyphName):
    sourceGlyph = Glyphs.font.glyphs[sourceGlyphName]
    targetGlyph = Glyphs.font.glyphs[sourceGlyphName + altSuffix]

    self.addComponentSpecialLayers(targetGlyph)

    for i, masterId in enumerate(self.masterIds):
      sourceLayerMeta = sourceGlyph.layers[masterId]
      sourceLayer = sourceGlyph.layers[self.reversedMasterIds[i]]

      self.copyLayer(
        sourceLayerMeta, 
        sourceLayer, 
        targetGlyph.layers[masterId])

    self.decomposeGlyph(targetGlyph)

  def addComponentSpecialLayers(self, targetGlyph):
    for component in targetGlyph.layers[0].components:
      glyphLayerNames = list(map(lambda x: x.name, targetGlyph.layers))
      for layer in component.component.layers:
        if layer.isSpecialLayer:
          if layer.name not in glyphLayerNames:
            print('add: ' + layer.name, layer.associatedMasterId)
            newLayer = GSLayer()
            newLayer.name = layer.name
            newLayer.associatedMasterId = layer.associatedMasterId

            newLayer.attributes['coordinates'] = {self.axisId: layer.name.replace('{', '').replace('}', '') }
            targetGlyph.layers.append(newLayer)
            targetGlyph.layers[newLayer.layerId].reinterpolate()
            

  def decomposeGlyph(self, targetGlyph):
    for layer in targetGlyph.layers:
      layer.decomposeComponents()

  def reverseSpecialLayers(self, sourceGlyphName):
    sourceGlyph = Glyphs.font.glyphs[sourceGlyphName]
    targetGlyph = Glyphs.font.glyphs[sourceGlyphName + altSuffix]
    
    for layer in targetGlyph.layers:
      if layer.isSpecialLayer:
        oldName = str(layer.name)
        
        oldAxisVal = int(oldName[oldName.find("{")+1:oldName.find("}")])
        newAxisVal = int(self.axisRange - oldAxisVal + min(self.axisVals))
        # if newAxisVal == 167:
        #   newAxisVal = 166
        # elif newAxisVal == 834:
        #   newAxisVal = 833

        newName = oldName.replace(str(oldAxisVal), str(newAxisVal))

        oldAssociatedMasterIndex = self.masterIds.index(layer.associatedMasterId)

        newAssociatedMasterIndex = len(self.masterIds) - oldAssociatedMasterIndex - 2
        layer.attributes['coordinates'] = None
        layer.name = newName
        layer.attributes['coordinates'] = {self.axisId: newAxisVal }
        layer.associatedMasterId = self.masterIds[newAssociatedMasterIndex]

  def getAltName(self, name):
    if name in specialGlyphsNameList:
      specialGlyph = list(filter(lambda sg: sg['name'] == g, specialGlyphsNameList))[0]
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
    matchingGroups = list(filter(lambda glyphGroup: glyphGroup['key'] == glyphName, glyphGroups))
    excludeList = []
    if len(matchingGroups) > 0:
      excludeList = [matchingGroups[0]['key']] + matchingGroups[0]['glyphs']
    else:
      excludeList = [glyphName]
    
    return list(filter(lambda g: g not in excludeList, caltGlyphNamesIncludingGroups))

  def skipClasses(self):
    code = ""
    for glyph in caltGlyphNames:
      glyphs1 = self.glyphsNotInGroup(glyph)
      glyphs2 = [self.getAltName(g) for g in glyphs1]
      skipGlyphs = glyphs1 + glyphs2 + universalSkipGlyphs
      code += "@skip" + glyph + " = [" + " ".join(skipGlyphs) + "];\n"
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
    featurePrefix = next(fPfx for fPfx in Glyphs.font.featurePrefixes if fPfx.name == 'caltClasses')
    featurePrefix.code = code


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
    for glyphName in caltGlyphNamesIncludingGroups:
      code += "sub " + glyphName + " by " + self.getAltName(glyphName) + ";\n"
    code += "} calt1;\n"

    code += "lookup calt2 {\n"
    for glyphName in caltGlyphNamesIncludingGroups:
      code += "  sub " + self.getAltName(glyphName) + " by " + glyphName + ";\n"
    code += "} calt2;\n"

    featurePrefix = next(fPfx for fPfx in Glyphs.font.featurePrefixes if fPfx.name == 'caltLookups')
    featurePrefix.code = code
  def updateFeatureCode(self):
    code = ""
    self.generateClasses()
    self.generateGlobalLookups()

    code += "lookup swap useExtension {\n"
    for i in range(contextRange):
      code += self.featureDupLookup(i, False)
    code += "} swap;\n"

    code += "lookup swapR useExtension {\n"
    for i in range(contextRangeRev):
      code += self.featureDupLookup(i, True)
    code += "} swapR;\n"

    caltFeature = next(feat for feat in Glyphs.font.features if feat.name == 'calt')
    caltFeature.code = code
    Glyphs.font.updateFeatures()


  def classOrBaseSub(self, glyphName, position):
    matchingGroups = list(filter(lambda glyphGroup: glyphGroup['key'] == glyphName, glyphGroups))
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
      # code += "lookup " + tagName + " useExtension {\n"

      for sourceGlyphName in glyphNameChunk:
        
        skipCode = " ".join(list(map(lambda x: "@skip" + sourceGlyphName, range(skip))))
        targetGlyph = self.classOrBaseSub(sourceGlyphName, 1)
        replacementLookup = 'calt1'

        if rev:
          targetGlyph = self.classOrBaseSub(sourceGlyphName, 2)
          replacementLookup = 'calt2'

        code += "  sub " + targetGlyph + " " + skipCode + " " + targetGlyph + "\' lookup " + replacementLookup + ";\n"

      # code += "} " + tagName + ";\n"

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
    Glyphs.font.disableUpdateInterface()

    for sourceGlyphName in sourceGlyphNamesIncludingGroups:
      self.duplicatesourceGlyph(sourceGlyphName)
      self.reverseMasters(sourceGlyphName)
      self.reverseSpecialLayers(sourceGlyphName)
    self.updateFeatureCode()
    self.specialGlyphs()
    
    Glyphs.font.enableUpdateInterface()
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
