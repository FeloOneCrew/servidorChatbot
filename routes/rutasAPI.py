from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from models.chatbot import chat
from database.basedatos import conexion

rutas = APIRouter()

@rutas.get("/asegurachat")
def consultarChat():
    try:
        consulta =  select(chat)
        print("hola")
        #Entregueme todo lo de la consulta
        resultado = conexion.execute(consulta).fetchall()
        resultadoJSON = [{'id': row.id, 'pregunta': row.pregunta, 'respuesta':row.respuesta} for row in resultado]
        return resultadoJSON

    except Exception as error:
        print(error)
        raise HTTPException(status_code = 500, detail=str(error))