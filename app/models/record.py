from .connect import get_connection


def new_record_user(doctor, patient, observer, states):
    '''
    Funcion que guarda el registro de los registros
    @return -> Regresa False en caso de cualquier fallo
                Regresa el id de la tabla registro
    '''
    conn = get_connection()
    try:
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO registro (fk_medico_id,fk_paciente_id,observaciones,estado_paciente) VALUES({},{},'{}','{}') RETURNING pk_registro_id"
            .format(doctor, patient, observer, states))

        conn.commit()
        id_medico = cur.fetchone()[0]
        conn.close()
        return id_medico

    except Exception as e:
        conn.rollback()
        return False


def get_record_patient(id):
    sql = """
    SELECT pk_hospital_id as cod_hospital, pk_medico_id as cod_medico, 
    nombre_especialidad, fecha_registro, estado_paciente, observaciones
    FROM registro
    INNER JOIN medico ON fk_medico_id = pk_medico_id
    INNER JOIN especialidad ON fk_especialidad_id = pk_especialidad_id
    INNER JOIN hospital ON medico.fk_tipo_servicio_id = hospital.fk_tipo_servicio_id
    WHERE fk_paciente_id = {}
    """.format(id)
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        resul = cur.fetchall()
        conn.close()
        return resul
    except Exception as e:
        return False


def get_record_doctor(id):
    sql = """
    SELECT pk_hospital_id as cod_hospital, pk_medico_id as cod_medico, 
    nombre_especialidad, fecha_registro, estado_paciente, observaciones
    FROM registro
    INNER JOIN medico ON fk_medico_id = pk_medico_id
    INNER JOIN especialidad ON fk_especialidad_id = pk_especialidad_id
    INNER JOIN hospital ON medico.fk_tipo_servicio_id = hospital.fk_tipo_servicio_id
    WHERE fk_medico_id = {}
    """.format(id)
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        resul = cur.fetchall()
        conn.close()
        return resul
    except Exception as e:
        return False


def get_record_hospital(id):
    sql = """
    SELECT pk_hospital_id as cod_hospital, pk_medico_id as cod_medico, 
    nombre_especialidad, fecha_registro, estado_paciente, observaciones
    FROM registro
    INNER JOIN medico ON fk_medico_id = pk_medico_id
    INNER JOIN especialidad ON fk_especialidad_id = pk_especialidad_id
    INNER JOIN hospital ON medico.fk_tipo_servicio_id = hospital.fk_tipo_servicio_id
    """.format(id)
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        resul = cur.fetchall()
        conn.close()
        return resul
    except Exception as e:
        return False