#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 24 "model.ump"
# line 58 "model.ump"
import os

class HistorialClinico():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #HistorialClinico Attributes
    #HistorialClinico Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aFecha_cita, aDatos_generales_paciente, aDatos_exploracion, aDiagnostico, aPronostico, aTratamiento, aUsuario):
        self._analisisLaboratorios = None
        self._usuario = None
        self._tratamiento = None
        self._pronostico = None
        self._diagnostico = None
        self._datos_exploracion = None
        self._datos_generales_paciente = None
        self._fecha_cita = None
        self._fecha_cita = aFecha_cita
        self._datos_generales_paciente = aDatos_generales_paciente
        self._datos_exploracion = aDatos_exploracion
        self._diagnostico = aDiagnostico
        self._pronostico = aPronostico
        self._tratamiento = aTratamiento
        didAddUsuario = self.setUsuario(aUsuario)
        if not didAddUsuario :
            raise RuntimeError ("Unable to create historialClinico due to usuario. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self._analisisLaboratorios = []

    #------------------------
    # INTERFACE
    #------------------------
    def setFecha_cita(self, aFecha_cita):
        wasSet = False
        self._fecha_cita = aFecha_cita
        wasSet = True
        return wasSet

    def setDatos_generales_paciente(self, aDatos_generales_paciente):
        wasSet = False
        self._datos_generales_paciente = aDatos_generales_paciente
        wasSet = True
        return wasSet

    def setDatos_exploracion(self, aDatos_exploracion):
        wasSet = False
        self._datos_exploracion = aDatos_exploracion
        wasSet = True
        return wasSet

    def setDiagnostico(self, aDiagnostico):
        wasSet = False
        self._diagnostico = aDiagnostico
        wasSet = True
        return wasSet

    def setPronostico(self, aPronostico):
        wasSet = False
        self._pronostico = aPronostico
        wasSet = True
        return wasSet

    def setTratamiento(self, aTratamiento):
        wasSet = False
        self._tratamiento = aTratamiento
        wasSet = True
        return wasSet

    def getFecha_cita(self):
        return self._fecha_cita

    def getDatos_generales_paciente(self):
        return self._datos_generales_paciente

    def getDatos_exploracion(self):
        return self._datos_exploracion

    def getDiagnostico(self):
        return self._diagnostico

    def getPronostico(self):
        return self._pronostico

    def getTratamiento(self):
        return self._tratamiento

    # Code from template association_GetOne 
    def getUsuario(self):
        return self._usuario

    # Code from template association_GetMany 
    def getAnalisisLaboratorio(self, index):
        aAnalisisLaboratorio = self._analisisLaboratorios[index]
        return aAnalisisLaboratorio

    def getAnalisisLaboratorios(self):
        newAnalisisLaboratorios = tuple(self._analisisLaboratorios)
        return newAnalisisLaboratorios

    def numberOfAnalisisLaboratorios(self):
        number = len(self._analisisLaboratorios)
        return number

    def hasAnalisisLaboratorios(self):
        has = len(self._analisisLaboratorios) > 0
        return has

    def indexOfAnalisisLaboratorio(self, aAnalisisLaboratorio):
        index = (-1 if not aAnalisisLaboratorio in self._analisisLaboratorios else self._analisisLaboratorios.index(aAnalisisLaboratorio))
        return index

    # Code from template association_SetOneToMany 
    def setUsuario(self, aUsuario):
        wasSet = False
        if aUsuario is None :
            return wasSet
        existingUsuario = self._usuario
        self._usuario = aUsuario
        if not (existingUsuario is None) and not existingUsuario == aUsuario :
            existingUsuario.removeHistorialClinico(self)
        self._usuario.addHistorialClinico(self)
        wasSet = True
        return wasSet

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfAnalisisLaboratorios():
        return 0

    # Code from template association_AddManyToOne 
    def addAnalisisLaboratorio1(self, aSangre, aOrina, aHeces):
        from AnalisisLaboratorio import AnalisisLaboratorio
        return AnalisisLaboratorio(aSangre, aOrina, aHeces, self)

    def addAnalisisLaboratorio2(self, aAnalisisLaboratorio):
        wasAdded = False
        if (aAnalisisLaboratorio) in self._analisisLaboratorios :
            return False
        existingHistorialClinico = aAnalisisLaboratorio.getHistorialClinico()
        isNewHistorialClinico = not (existingHistorialClinico is None) and not self == existingHistorialClinico
        if isNewHistorialClinico :
            aAnalisisLaboratorio.setHistorialClinico(self)
        else :
            self._analisisLaboratorios.append(aAnalisisLaboratorio)
        wasAdded = True
        return wasAdded

    def removeAnalisisLaboratorio(self, aAnalisisLaboratorio):
        wasRemoved = False
        #Unable to remove aAnalisisLaboratorio, as it must always have a historialClinico
        if not self == aAnalisisLaboratorio.getHistorialClinico() :
            self._analisisLaboratorios.remove(aAnalisisLaboratorio)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addAnalisisLaboratorioAt(self, aAnalisisLaboratorio, index):
        wasAdded = False
        if self.addAnalisisLaboratorio(aAnalisisLaboratorio) :
            if index < 0 :
                index = 0
            if index > self.numberOfAnalisisLaboratorios() :
                index = self.numberOfAnalisisLaboratorios() - 1
            self._analisisLaboratorios.remove(aAnalisisLaboratorio)
            self._analisisLaboratorios.insert(index, aAnalisisLaboratorio)
            wasAdded = True
        return wasAdded

    def addOrMoveAnalisisLaboratorioAt(self, aAnalisisLaboratorio, index):
        wasAdded = False
        if (aAnalisisLaboratorio) in self._analisisLaboratorios :
            if index < 0 :
                index = 0
            if index > self.numberOfAnalisisLaboratorios() :
                index = self.numberOfAnalisisLaboratorios() - 1
            self._analisisLaboratorios.remove(aAnalisisLaboratorio)
            self._analisisLaboratorios.insert(index, aAnalisisLaboratorio)
            wasAdded = True
        else :
            wasAdded = self.addAnalisisLaboratorioAt(aAnalisisLaboratorio, index)
        return wasAdded

    def delete(self):
        placeholderUsuario = self._usuario
        self._usuario = None
        if not (placeholderUsuario is None) :
            placeholderUsuario.removeHistorialClinico(self)

        while len(self._analisisLaboratorios) > 0 :
            aAnalisisLaboratorio = self._analisisLaboratorios[len(self._analisisLaboratorios) - 1]
            aAnalisisLaboratorio.delete()
            self._analisisLaboratorios.remove(aAnalisisLaboratorio)

    def __str__(self):
        return str(super().__str__()) + "[" + "datos_generales_paciente" + ":" + str(self.getDatos_generales_paciente()) + "," + "datos_exploracion" + ":" + str(self.getDatos_exploracion()) + "," + "diagnostico" + ":" + str(self.getDiagnostico()) + "," + "pronostico" + ":" + str(self.getPronostico()) + "," + "tratamiento" + ":" + str(self.getTratamiento()) + "]" + str(os.linesep) + "  " + "fecha_cita" + "=" + str((((self.getFecha_cita().__str__().replaceAll("  ", "    ")) if not self.getFecha_cita() == self else "this") if not (self.getFecha_cita() is None) else "null")) + str(os.linesep) + "  " + "usuario = " + ((format(id(self.getUsuario()), "x")) if not (self.getUsuario() is None) else "null")

    def addAnalisisLaboratorio(self, *argv):
        from AnalisisLaboratorio import AnalisisLaboratorio
        if len(argv) == 3 and isinstance(argv[0], str) and isinstance(argv[1], str) and isinstance(argv[2], str) :
            return self.addAnalisisLaboratorio1(argv[0], argv[1], argv[2])
        if len(argv) == 1 and isinstance(argv[0], AnalisisLaboratorio) :
            return self.addAnalisisLaboratorio2(argv[0])
        raise TypeError("No method matches provided parameters")

