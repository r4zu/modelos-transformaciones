#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 33 "model.ump"
# line 63 "model.ump"
import os

class AnalisisLaboratorio():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #AnalisisLaboratorio Attributes
    #AnalisisLaboratorio Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aSangre, aOrina, aHeces, aHistorialClinico):
        self._historialClinico = None
        self._heces = None
        self._orina = None
        self._sangre = None
        self._sangre = aSangre
        self._orina = aOrina
        self._heces = aHeces
        didAddHistorialClinico = self.setHistorialClinico(aHistorialClinico)
        if not didAddHistorialClinico :
            raise RuntimeError ("Unable to create analisisLaboratorio due to historialClinico. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setSangre(self, aSangre):
        wasSet = False
        self._sangre = aSangre
        wasSet = True
        return wasSet

    def setOrina(self, aOrina):
        wasSet = False
        self._orina = aOrina
        wasSet = True
        return wasSet

    def setHeces(self, aHeces):
        wasSet = False
        self._heces = aHeces
        wasSet = True
        return wasSet

    def getSangre(self):
        return self._sangre

    def getOrina(self):
        return self._orina

    def getHeces(self):
        return self._heces

    # Code from template association_GetOne 
    def getHistorialClinico(self):
        return self._historialClinico

    # Code from template association_SetOneToMany 
    def setHistorialClinico(self, aHistorialClinico):
        wasSet = False
        if aHistorialClinico is None :
            return wasSet
        existingHistorialClinico = self._historialClinico
        self._historialClinico = aHistorialClinico
        if not (existingHistorialClinico is None) and not existingHistorialClinico == aHistorialClinico :
            existingHistorialClinico.removeAnalisisLaboratorio(self)
        self._historialClinico.addAnalisisLaboratorio(self)
        wasSet = True
        return wasSet

    def delete(self):
        placeholderHistorialClinico = self._historialClinico
        self._historialClinico = None
        if not (placeholderHistorialClinico is None) :
            placeholderHistorialClinico.removeAnalisisLaboratorio(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "sangre" + ":" + str(self.getSangre()) + "," + "orina" + ":" + str(self.getOrina()) + "," + "heces" + ":" + str(self.getHeces()) + "]" + str(os.linesep) + "  " + "historialClinico = " + ((format(id(self.getHistorialClinico()), "x")) if not (self.getHistorialClinico() is None) else "null")

