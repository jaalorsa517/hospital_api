from .connect import get_connection


def new_doctor_user(especialidad):
    '''
    Funcion que guarda el registro de un usuario hospital-medico
    @return -> Regresa False en caso de cualquier fallo
                Regresa el id de la tabla medico
    '''
    conn = get_connection()
    try:
        cur = conn.cursor()

        cur.execute(
            "SELECT pk_especialidad_id FROM especialidad WHERE nombre_especialidad = '{}'"
            .format(especialidad))
        tipo_especialidad = cur.fetchone()[0]

        cur.execute(
            "SELECT pk_tipo_servicio_id FROM tipo_servicio WHERE descripcion_tipo_servicio = 'MEDICO'"
        )
        tipo_servicio = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO medico (fk_especialidad_id,fk_tipo_servicio_id) VALUES({},'{}') RETURNING pk_medico_id"
            .format(tipo_especialidad, tipo_servicio))

        conn.commit()
        id_medico = cur.fetchone()[0]
        conn.close()
        return id_medico

    except Exception as e:
        conn.rollback()
        return False