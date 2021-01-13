from .connect import get_connection


def new_hospital_user(id, nom, dir, servi):
    '''
    Funcion que guarda el registro de un usuario hospital
    @return -> Regresa False en caso de cualquier fallo
                Regresa el id de la tabla hospital
    '''
    conn = get_connection()
    try:
        cur = conn.cursor()

        cur.execute(
            "SELECT pk_tipo_usuario_id FROM tipo_usuario WHERE descripcion_tipo_usuario = 'HOSPITAL'"
        )
        tipo_usuario = cur.fetchone()[0]

        cur.execute(
            "UPDATE usuario SET nombres_usuario= '{}', direccion ='{}', fk_tipo_usuario_id = {} WHERE pk_usuario_identificacion = '{}'"
            .format(nom, dir, tipo_usuario, id))

        cur.execute(
            "SELECT pk_tipo_servicio_id FROM tipo_servicio WHERE descripcion_tipo_servicio = '{}'"
            .format(servi))
        tipo_servicio = cur.fetchone()[0]

        cur.execute(
            "INSERT INTO hospital (fk_tipo_usuario_id,fk_tipo_servicio_id) VALUES({},{}) RETURNING pk_hospital_id"
            .format(tipo_usuario, tipo_servicio))

        conn.commit()
        id_hospital = cur.fetchone()[0]
        conn.close()
        return id_hospital

    except Exception as e:
        conn.rollback()
        return False