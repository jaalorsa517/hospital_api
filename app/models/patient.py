from .connect import get_connection


def new_patient_user(id, nom, dir, birth):
    '''
    Funcion que guarda el registro de un usuario paciente
    @return -> Regresa False en caso de cualquier fallo
                Regresa el id de la tabla paciente
    '''
    conn = get_connection()
    try:
        cur = conn.cursor()

        cur.execute(
            "SELECT pk_tipo_usuario_id FROM tipo_usuario WHERE descripcion_tipo_usuario = 'PACIENTE'"
        )
        tipo_usuario = cur.fetchone()[0]

        cur.execute(
            "UPDATE usuario SET nombres_usuario= '{}', direccion ='{}', fk_tipo_usuario_id = {} WHERE pk_usuario_identificacion = '{}'"
            .format(nom, dir, tipo_usuario, id))

        cur.execute(
            "INSERT INTO paciente (fk_tipo_usuario_id,nacimiento) VALUES({},'{}') RETURNING pk_paciente_id"
            .format(tipo_usuario, birth))

        conn.commit()
        id_paciente = cur.fetchone()[0]
        conn.close()
        return id_paciente

    except Exception as e:
        conn.rollback()
        return False