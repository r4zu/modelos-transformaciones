#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 8 "model.ump"
# line 48 "model.ump"
import os
from enum import Enum, auto

class Usuario():
    #------------------------
    # ENUMERATIONS
    #------------------------
    class Roles(Enum):
        def _generate_next_value_(name, start, count, last_values):
            return name
        def __str__(self):
            return str(self.value)
        Cliente = auto()
        Doctor = auto()
        Admin = auto()

    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Usuario Attributes
    #Usuario Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    @classmethod
    def alternateConstructor(cls, aId, aEmail, aContrasena, aRol, aDatosPersonales):
        self = cls.__new__(cls)
        self._historialClinicos = None
        self._datosPersonales = None
        self._rol = None
        self._contrasena = None
        self._email = None
        self._id = None
        self._id = aId
        self._email = aEmail
        self._contrasena = aContrasena
        self._rol = aRol
        if aDatosPersonales is None or not (aDatosPersonales.getUsuario() is None) :
            raise RuntimeError ("Unable to create Usuario due to aDatosPersonales. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self._datosPersonales = aDatosPersonales
        self._historialClinicos = []
        return self

    def __init__(self, aId, aEmail, aContrasena, aRol, aNombresForDatosPersonales, aApellidoForDatosPersonales, aDniForDatosPersonales, aDireccionForDatosPersonales, aTelefonoForDatosPersonales):
        from DatosPersonales import DatosPersonales
        self._historialClinicos = None
        self._datosPersonales = None
        self._rol = None
        self._contrasena = None
        self._email = None
        self._id = None
        self._id = aId
        self._email = aEmail
        self._contrasena = aContrasena
        self._rol = aRol
        self._datosPersonales = DatosPersonales.alternateConstructor(aNombresForDatosPersonales, aApellidoForDatosPersonales, aDniForDatosPersonales, aDireccionForDatosPersonales, aTelefonoForDatosPersonales, self)
        self._historialClinicos = []

    #------------------------
    # INTERFACE
    #------------------------
    def setId(self, aId):
        wasSet = False
        self._id = aId
        wasSet = True
        return wasSet

    def setEmail(self, aEmail):
        wasSet = False
        self._email = aEmail
        wasSet = True
        return wasSet

    def setContrasena(self, aContrasena):
        wasSet = False
        self._contrasena = aContrasena
        wasSet = True
        return wasSet

    def setRol(self, aRol):
        wasSet = False
        self._rol = aRol
        wasSet = True
        return wasSet

    def getId(self):
        return self._id

    def getEmail(self):
        return self._email

    def getContrasena(self):
        return self._contrasena

    def getRol(self):
        return self._rol

    # Code from template association_GetOne 
    def getDatosPersonales(self):
        return self._datosPersonales

    # Code from template association_GetMany 
    def getHistorialClinico(self, index):
        aHistorialClinico = self._historialClinicos[index]
        return aHistorialClinico

    def getHistorialClinicos(self):
        newHistorialClinicos = tuple(self._historialClinicos)
        return newHistorialClinicos

    def numberOfHistorialClinicos(self):
        number = len(self._historialClinicos)
        return number

    def hasHistorialClinicos(self):
        has = len(self._historialClinicos) > 0
        return has

    def indexOfHistorialClinico(self, aHistorialClinico):
        index = (-1 if not aHistorialClinico in self._historialClinicos else self._historialClinicos.index(aHistorialClinico))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfHistorialClinicos():
        return 0

    # Code from template association_AddManyToOne 
    def addHistorialClinico1(self, aFecha_cita, aDatos_generales_paciente, aDatos_exploracion, aDiagnostico, aPronostico, aTratamiento):
        from HistorialClinico import HistorialClinico
        return HistorialClinico(aFecha_cita, aDatos_generales_paciente, aDatos_exploracion, aDiagnostico, aPronostico, aTratamiento, self)

    def addHistorialClinico2(self, aHistorialClinico):
        wasAdded = False
        if (aHistorialClinico) in self._historialClinicos :
            return False
        existingUsuario = aHistorialClinico.getUsuario()
        isNewUsuario = not (existingUsuario is None) and not self == existingUsuario
        if isNewUsuario :
            aHistorialClinico.setUsuario(self)
        else :
            self._historialClinicos.append(aHistorialClinico)
        wasAdded = True
        return wasAdded

    def removeHistorialClinico(self, aHistorialClinico):
        wasRemoved = False
        #Unable to remove aHistorialClinico, as it must always have a usuario
        if not self == aHistorialClinico.getUsuario() :
            self._historialClinicos.remove(aHistorialClinico)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addHistorialClinicoAt(self, aHistorialClinico, index):
        wasAdded = False
        if self.addHistorialClinico(aHistorialClinico) :
            if index < 0 :
                index = 0
            if index > self.numberOfHistorialClinicos() :
                index = self.numberOfHistorialClinicos() - 1
            self._historialClinicos.remove(aHistorialClinico)
            self._historialClinicos.insert(index, aHistorialClinico)
            wasAdded = True
        return wasAdded

    def addOrMoveHistorialClinicoAt(self, aHistorialClinico, index):
        wasAdded = False
        if (aHistorialClinico) in self._historialClinicos :
            if index < 0 :
                index = 0
            if index > self.numberOfHistorialClinicos() :
                index = self.numberOfHistorialClinicos() - 1
            self._historialClinicos.remove(aHistorialClinico)
            self._historialClinicos.insert(index, aHistorialClinico)
            wasAdded = True
        else :
            wasAdded = self.addHistorialClinicoAt(aHistorialClinico, index)
        return wasAdded

    def delete(self):
        existingDatosPersonales = self._datosPersonales
        self._datosPersonales = None
        if not (existingDatosPersonales is None) :
            existingDatosPersonales.delete()

        while len(self._historialClinicos) > 0 :
            aHistorialClinico = self._historialClinicos[len(self._historialClinicos) - 1]
            aHistorialClinico.delete()
            self._historialClinicos.remove(aHistorialClinico)

    def __str__(self):
        return str(super().__str__()) + "[" + "id" + ":" + str(self.getId()) + "," + "email" + ":" + str(self.getEmail()) + "," + "contrasena" + ":" + str(self.getContrasena()) + "]" + str(os.linesep) + "  " + "rol" + "=" + str((((self.getRol().__str__().replaceAll("  ", "    ")) if not self.getRol() == self else "this") if not (self.getRol() is None) else "null")) + str(os.linesep) + "  " + "datosPersonales = " + ((format(id(self.getDatosPersonales()), "x")) if not (self.getDatosPersonales() is None) else "null")

    def addHistorialClinico(self, *argv):
        from HistorialClinico import HistorialClinico
        if len(argv) == 6 and isinstance(argv[0], Date) and isinstance(argv[1], str) and isinstance(argv[2], str) and isinstance(argv[3], str) and isinstance(argv[4], str) and isinstance(argv[5], str) :
            return self.addHistorialClinico1(argv[0], argv[1], argv[2], argv[3], argv[4], argv[5])
        if len(argv) == 1 and isinstance(argv[0], HistorialClinico) :
            return self.addHistorialClinico2(argv[0])
        raise TypeError("No method matches provided parameters")

