class usuario:
    def __init__(self,id_emp,password):
        self._id_emp = id_emp
        self._password = password

    def login(self,db,widget):
        db.dbcursor.execute("""SELECT usr.name, usr.surname, rol.rol 
                            FROM Users.usr AS usr
                            INNER JOIN Users.rol AS rol 
                            ON usr.id_emp = rol.id_emp
                            WHERE rol.id_emp = %s AND rol.password = %s""", (self._id_emp, self._password))

        result = db.dbcursor.fetchall()
        name = result[0][0]
        surname = result[0][1]
        c_name = name + " " + surname
        rol = result[0][2]
        try:
            if rol == "Recepcion":
                from Ui.Recepcion.a_recep import a2
                a2(db, widget, c_name)
            elif rol == "Bodega":
                from Ui.Almacen.a_almacen import a3
                a3(db, widget)
            elif rol == "Cocina":
                from Ui.Cocina.a_cocina import a4
                a4(db, widget)
        except Exception as e:
            print(e)
            return True
        
