import mysql.connector


database = 'glpi'
username = 'glpi'
password = 'MySQLPass'

#Homologação
server = 'srvglpi-hom.cetesb.local'
cnx = mysql.connector.connect(user=username, password=password, host=server, database=database)

'''
#Produção
server = 'srvglpi01.cetesb.local'
cnx = mysql.connector.connect(user=username, password=password, host=server, database=database, auth_plugin='mysql_native_password')
'''



def check(nome):
    cursor = cnx.cursor()
    selecao = ("select glpi_groups_users.users_id "
                "from glpi_groups_users "
                "right join glpi_users "
                "on glpi_groups_users.users_id = glpi_users.id "
                "where glpi_users.name = %s; ")
    try:
        cursor.execute(selecao, nome)
        result = cursor.fetchall()
        cursor.close()
        return result
    except:
        return None


def remove(users_id):
    cursor = cnx.cursor()
    remocao = ("delete from glpi_groups_users "
                "where glpi_groups_users.users_id = %s; ")
    try:
        cursor.execute(remocao, users_id)
        cnx.commit()
        print('removido - ', users_id)
        cursor.close()
    except:
        print('falha na remocao - ', users_id)
    

def inserir(campos):
    cursor = cnx.cursor()
    insercao = ("insert into glpi_groups_users (users_id, groups_id, is_dynamic, is_manager, is_userdelegate)"
                "values("
	            "(select id from glpi_users where name = %s),"
                "(select id from glpi_groups where name = %s),"
                "(0),"
                "(%s),"
                "(%s)"
                ");")
    try:
        cursor.execute(insercao, campos)
        cnx.commit()
        cursor.close()
        print('incluído - ', campos)
    except:
        print('falha na inclusão - ', campos)
