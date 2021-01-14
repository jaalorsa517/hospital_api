-- CREATE USER hospital;

-- ALTER user hospital with password 'hospital';

-- CREATE DATABASE hospital WITH OWNER = hospital ENCODING = 'UTF8';

-- GRANT ALL PRIVILEGES ON DATABASE hospital TO hospital;


-----------------------------------
-- TABLAS


CREATE TABLE public.tipo_usuario (
    pk_tipo_usuario_id serial,
    descripcion_tipo_usuario character varying(10),
    PRIMARY KEY (pk_tipo_usuario_id)
);

ALTER TABLE
    public.tipo_usuario OWNER to hospital;

--------------------------

CREATE TABLE public.usuario (
    pk_usuario_identificacion character varying(20) NOT NULL,
    email character varying(50) NOT NULL,
    telefono character varying(30) NOT NULL,
    contrasenya character varying(150) NOT NULL,
    apellidos_usuario character varying(50),
    nombres_usuario character varying(50),
    update_on timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_on timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    direccion character varying(100),
    fk_tipo_usuario_id integer,
    role_on character varying(10) DEFAULT 'basic',
    PRIMARY KEY (pk_usuario_identificacion),
    CONSTRAINT email_uq UNIQUE (email),
    CONSTRAINT usuario_tipo_usuario_fkey FOREIGN KEY (fk_tipo_usuario_id) REFERENCES public.tipo_usuario (pk_tipo_usuario_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID
);

ALTER TABLE
    public.usuario OWNER to hospital;

--------------------------------------------
CREATE TABLE public.paciente (
    pk_paciente_id serial,
    nacimiento date NOT NULL,
    fk_tipo_usuario_id integer,
    CONSTRAINT paciente_pkey PRIMARY KEY (pk_paciente_id),
    CONSTRAINT paciente_tipo_usuario_fkey FOREIGN KEY (fk_tipo_usuario_id) REFERENCES public.tipo_usuario (pk_tipo_usuario_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID
);

ALTER TABLE
    public.paciente OWNER to hospital;

--------------------------------------------------
CREATE TABLE public.tipo_servicio (
    pk_tipo_servicio_id serial,
    descripcion_tipo_servicio character varying,
    PRIMARY KEY (pk_tipo_servicio_id)
);

ALTER TABLE
    public.tipo_servicio OWNER to hospital;

----------------------------------------------------
CREATE TABLE public.hospital (
    pk_hospital_id serial,
    fk_tipo_servicio_id integer,
    fk_tipo_usuario_id integer,
    CONSTRAINT hospital_pkey PRIMARY KEY (pk_hospital_id),
    CONSTRAINT hospital_tipo_usuario_fkey FOREIGN KEY (fk_tipo_usuario_id) REFERENCES public.tipo_usuario (pk_tipo_usuario_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID,
    CONSTRAINT hospital_tipo_servicio_fkey FOREIGN KEY (fk_tipo_servicio_id) REFERENCES public.tipo_servicio (pk_tipo_servicio_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID
);

ALTER TABLE
    public.hospital OWNER to hospital;

----------------------------------------------------------------------------
CREATE TABLE public.especialidad (
    pk_especialidad_id serial,
    nombre_especialidad character varying(50),
    PRIMARY KEY (pk_especialidad_id)
);

ALTER TABLE
    public.especialidad OWNER to hospital;

----------------------------------------------------------------------------
CREATE TABLE public.medico (
    pk_medico_id serial,
    fk_especialidad_id integer,
    fk_tipo_servicio_id integer,
    CONSTRAINT medico_pkey PRIMARY KEY (pk_medico_id),
    CONSTRAINT medico_tipo_servicio_fkey FOREIGN KEY (fk_tipo_servicio_id) REFERENCES public.tipo_servicio (pk_tipo_servicio_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID,
    CONSTRAINT medicoo_especialidad_fkey FOREIGN KEY (fk_especialidad_id) REFERENCES public.especialidad (pk_especialidad_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID
);

ALTER TABLE
    public.medico OWNER to hospital;

---------------------------------------------------------------------------------
CREATE TABLE public.registro (
    pk_registro_id serial,
    estado_paciente character varying(50) NOT NULL,
    observaciones text NOT NULL,
    fecha_registro timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    fk_medico_id integer,
    fk_paciente_id integer,
    CONSTRAINT registro_pkey PRIMARY KEY (pk_registro_id),
    CONSTRAINT registro_paciente_fkey FOREIGN KEY (fk_paciente_id) REFERENCES public.paciente (pk_paciente_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID,
    CONSTRAINT registro_medico_fkey FOREIGN KEY (fk_medico_id) REFERENCES public.medico (pk_medico_id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION NOT VALID
);

ALTER TABLE
    public.registro OWNER to hospital;

------------------------------------------------------------
-- FUNCION Y TRIGGER

CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.update_on = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER set_timestamp
BEFORE UPDATE ON usuario
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

----------------------------------------------------------------
--DATOS NECESARIOS
INSERT INTO
    public.tipo_servicio(descripcion_tipo_servicio)
VALUES
    ('MEDICO');

INSERT INTO
    public.tipo_usuario(descripcion_tipo_usuario)
VALUES
    ('HOSPITAL');

INSERT INTO
    public.tipo_usuario(descripcion_tipo_usuario)
VALUES
    ('PACIENTE');

INSERT INTO
    public.especialidad(nombre_especialidad)
VALUES
    ('GENERAL');

INSERT INTO
    public.especialidad(nombre_especialidad)
VALUES
    ('OFTAMOLOGIA');

INSERT INTO
    public.especialidad(nombre_especialidad)
VALUES
    ('PEDIATRIA');