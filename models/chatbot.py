from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from database.basedatos import metaDatos, motorBD

#Modelo de la tabla CHAT
chat = Table("chat", metaDatos,
             Column("id", Integer, primary_key=True),
             Column("pregunta", String(200)),
             Column("respuesta", String(200)),
             )

metaDatos.create_all(motorBD)