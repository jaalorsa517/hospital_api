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