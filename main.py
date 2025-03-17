import app
from fastapi import FastAPI, Request, Form, HTTPException, Depends, Cookie, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import mysql.connector
from fastapi.staticfiles import StaticFiles
from fastapi import Response
import json
from typing import Optional
from starlette.responses import JSONResponse

app= FastAPI()

app.mount("/static", StaticFiles(directory= "static"), name="static")

templates= Jinja2Templates(directory="templates")


def conectar_banco():
    return mysql.connector.connect(
        host= "",
        user= "",
        password= "",
        database= ""
    )

def criar_tabela_usuario():
    conexao= conectar_banco()
    cursor= conexao.cursor()
    cursor.execute("""
        CREAT TABLE IF NOT EXISTS usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL
                )

            """)
    conexao.commit()
    cursor.close()
    conexao.close()

criar_tabela_usuario()

def criar_tabela_produtos():
    conexao= conectar_banco()
    cursor= conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto(
                id INT AUTO_INCREMENT PRIMARY KEY,
                vonixx_extractus INT(10),
                vonixx_bactran INT(10),
                vonixx_sanitizante INT(10),                            
                vonixx_sintra INT(10),
        )
    """)

    conexao.commit()
    cursor.close()
    conexao.close()
    
criar_tabela_produtos()


def criar_tabela_agendamento():
    conexao= conectar_banco()
    cursor= conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agendamento(
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente VARCHAR(255) NOT NULL,
                endereco VARCHAR(255) NOT NULL,    
                telefone VARCHAR(20) NOT NULL,
                data_agendamento VARCHAR(255) NOT NULL,         
                vonixx_extractus INT(10),
                vonixx_bactran INT(10),
                vonixx_sanitizante INT(10),                            
                vonixx_sintra INT(10),
                status VARCHAR(20) DEFAUT 'pendente',   
        )
    """)
    conexao.commit()
    cursor.close()
    conexao.close()

criar_tabela_agendamento()

def obter_usuario(usuario_id: int):
    conexao= conectar_banco()
    cursor= conexao.cursor(dictionary=True)
    sql= "SELECT * FROM usuario WHERE id= %s"
    val= (usuario_id)
    cursor.execute(sql, val)
    usuario= cursor.fetchone()
    cursor.close()
    conexao.close()
    if not usuario:
        raise HTTPException(status_code=404, detail="usuário não encontrado")
    return usuario


def obter_agendamento(agendamento_id: int):
    conexao= conectar_banco()
    cursor= conexao.cursor(dictionary=True)
    sql= "SELECT * FROM agendamento WHERE id= %s"
    val= (agendamento_id)
    cursor.execute(sql, val)
    agendamento= cursor.fetchone()
    cursor.close()
    conexao.close()
    if not agendamento:
        raise HTTPException(status_code=404, detail="agenamento não encontrado")
    return agendamento
    

def obter_produto(produto_id: int):
    conexao= conectar_banco()
    cursor= conexao.cursor(dictionary=True)
    sql= "SELECT * FROM produto WHERE id= %s"
    val= (produto_id)
    cursor.execute(sql, val)
    produto= cursor.fetchone()
    cursor.close()
    conexao.close()
    if not produto:
        raise HTTPException(status_code=404, detail="produto não encontrado")
    return produto    


def verificar_autenticacao(usuario_id: int= Cookie(None)):
    return usuario_id is not None

@app.get("/", response_class= HTMLResponse)
async def pagina_principal(request: Request, response: Response):
    usuario_id= request.cookies.get("usuario_id")
    if not usuario_id:
        return RedirectResponse(url="/login", status_code=303)
    usuario= obter_usuario(int(usuario_id))

    if not usuario:
        response.delete_cookie("usuario_id")
    return RedirectResponse(url="/login", status_code=303)
    
    return templates.TemplateResponse("pagina_principal.html", {"request": request, "usuario": usuario})

