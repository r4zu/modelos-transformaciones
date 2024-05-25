#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 15 "model.ump"
# line 53 "model.ump"
import os

class DatosPersonales():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #DatosPersonales Attributes
    #DatosPersonales Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    @classmethod
    def alternateConstructor(cls, aNombres, aApellido, aDni, aDireccion, aTelefono, aUsuario):
        self = cls.__new__(cls)
        self._usuario = None
        self._telefono = None
        self._direccion = None
        self._dni = None
        self._apellido = None
        self._nombres = None
        self._nombres = aNombres
        self._apellido = aApellido
        self._dni = aDni
        self._direccion = aDireccion
        self._telefono = aTelefono
        if aUsuario is None or not (aUsuario.getDatosPersonales() is None) :
            raise RuntimeError ("Unable to create DatosPersonales due to aUsuario. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self._usuario = aUsuario
        return self

    def __init__(self, aNombres, aApellido, aDni, aDireccion, aTelefono, aIdForUsuario, aEmailForUsuario, aContrasenaForUsuario, aRolForUsuario):
        from Usuario import Usuario
        self._usuario = None
        self._telefono = None
        self._direccion = None
        self._dni = None
        self._apellido = None
        self._nombres = None
        self._nombres = aNombres
        self._apellido = aApellido
        self._dni = aDni
        self._direccion = aDireccion
        self._telefono = aTelefono
        self._usuario = Usuario.alternateConstructor(aIdForUsuario, aEmailForUsuario, aContrasenaForUsuario, aRolForUsuario, self)

    #------------------------
    # INTERFACE
    #------------------------
    def setNombres(self, aNombres):
        wasSet = False
        self._nombres = aNombres
        wasSet = True
        return wasSet

    def setApellido(self, aApellido):
        wasSet = False
        self._apellido = aApellido
        wasSet = True
        return wasSet

    def setDni(self, aDni):
        wasSet = False
        self._dni = aDni
        wasSet = True
        return wasSet

    def setDireccion(self, aDireccion):
        wasSet = False
        self._direccion = aDireccion
        wasSet = True
        return wasSet

    def setTelefono(self, aTelefono):
        wasSet = False
        self._telefono = aTelefono
        wasSet = True
        return wasSet

    def getNombres(self):
        return self._nombres

    def getApellido(self):
        return self._apellido

    def getDni(self):
        return self._dni

    def getDireccion(self):
        return self._direccion

    def getTelefono(self):
        return self._telefono

    # Code from template association_GetOne 
    def getUsuario(self):
        return self._usuario

    def delete(self):
        existingUsuario = self._usuario
        self._usuario = None
        if not (existingUsuario is None) :
            existingUsuario.delete()

    def __str__(self):
        return str(super().__str__()) + "[" + "nombres" + ":" + str(self.getNombres()) + "," + "apellido" + ":" + str(self.getApellido()) + "," + "dni" + ":" + str(self.getDni()) + "," + "direccion" + ":" + str(self.getDireccion()) + "," + "telefono" + ":" + str(self.getTelefono()) + "]" + str(os.linesep) + "  " + "usuario = " + ((format(id(self.getUsuario()), "x")) if not (self.getUsuario() is None) else "null")

