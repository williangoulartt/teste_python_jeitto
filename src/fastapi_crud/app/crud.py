from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


def get_cliente_by_email(db: Session, email: str):
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()


def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = get_cliente_by_email(db, email=cliente.email)
    if db_cliente:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_cliente = models.Cliente(nome=cliente.nome, email=cliente.email, telefone=cliente.telefone)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
