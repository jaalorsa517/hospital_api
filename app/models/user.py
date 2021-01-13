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
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False


def authorized(id):
    '''
    Devuelve el usuario con el id
    '''
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = "SELECT pk_usuario_identificacion as id, email,contrasenya as password, created_on, update_on FROM public.usuario WHERE pk_usuario_identificacion= '{}' ".format(
            id)
        cur.execute(sql)
        resul = dict(
            zip(('id', 'email', 'password', 'created_on', 'update_on'),
                cur.fetchall()[0]))
        conn.close()
        return resul
    except Exception as e:
        return False


def update_pass(id, passw):
    try:
        conn = get_connection()
        cur = conn.cursor()
        sql = "UPDATE public.usuario SET contrasenya='{}' WHERE pk_usuario_identificacion = '{}';".format(
            passw, id)
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False