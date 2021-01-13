from .connect import get_connection


def signin_insert(id, email, telefono, contraseña):
    '''
    Guarda el registro inicial a la base de datos
    '''
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO public.usuario(pk_usuario_identificacion, email, telefono, contrasenya) VALUES (%s,%s,%s,%s)"
        cur.execute(sql, (id, email, telefono, contraseña))
        # conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False
