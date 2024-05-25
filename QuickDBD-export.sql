-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Usuario" (
    "id" int   NOT NULL,
    "email" text   NOT NULL,
    "contrasena" text   NOT NULL,
    "rol_id" int   NOT NULL,
    CONSTRAINT "pk_Usuario" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Roles" (
    "id" int   NOT NULL,
    "nombre_rol" text   NOT NULL,
    CONSTRAINT "pk_Roles" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "DatosPersonales" (
    "id" int   NOT NULL,
    "nombres" text   NOT NULL,
    "apellidos" text   NOT NULL,
    "dni" text   NOT NULL,
    "direccion" text   NOT NULL,
    "telefono" text   NOT NULL,
    "usuario_id" int   NOT NULL,
    CONSTRAINT "pk_DatosPersonales" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "HistorialClinico" (
    "id" int   NOT NULL,
    "fecha_cita" text   NOT NULL,
    "datos_generales_paciente" text   NOT NULL,
    "datos_exploracion" text   NOT NULL,
    "diagnostico" text   NOT NULL,
    "pronostico" text   NOT NULL,
    "tratamiento" text   NOT NULL,
    "usuario_id" int   NOT NULL,
    CONSTRAINT "pk_HistorialClinico" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "AnalisisLaboratorio" (
    "id" int   NOT NULL,
    "sangre" text   NOT NULL,
    "orina" text   NOT NULL,
    "heces" text   NOT NULL,
    "historial_clinico_id" int   NOT NULL,
    CONSTRAINT "pk_AnalisisLaboratorio" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "Usuario" ADD CONSTRAINT "fk_Usuario_rol_id" FOREIGN KEY("rol_id")
REFERENCES "Roles" ("id");

ALTER TABLE "DatosPersonales" ADD CONSTRAINT "fk_DatosPersonales_usuario_id" FOREIGN KEY("usuario_id")
REFERENCES "Usuario" ("id");

ALTER TABLE "HistorialClinico" ADD CONSTRAINT "fk_HistorialClinico_usuario_id" FOREIGN KEY("usuario_id")
REFERENCES "Usuario" ("id");

ALTER TABLE "AnalisisLaboratorio" ADD CONSTRAINT "fk_AnalisisLaboratorio_historial_clinico_id" FOREIGN KEY("historial_clinico_id")
REFERENCES "HistorialClinico" ("id");

