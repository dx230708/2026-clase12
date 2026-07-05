import pytest
from datetime import datetime
from faker import Faker
from utils.api_utils import create_post_api, update_post_api, delete_post_api

fake = Faker()

@pytest.mark.e2e  # Requerimiento 6: Marcado como End-to-End
def test_ciclo_de_vida_post_crud():
    """
    Cubre el ciclo de vida completo de un Post:
    1. Creación (POST) con datos Faker
    2. Modificación parcial (PATCH) del título
    3. Eliminación (DELETE)
    Valida esquemas, tipos de datos y tiempos.
    """
    
    # -------------------------------------------------------------------------
    # PASO 1: POST /posts (Creación con Faker)
    # -------------------------------------------------------------------------
    titulo_faker = fake.sentence()
    cuerpo_faker = fake.text()
    
    respuesta_post = create_post_api(title=titulo_faker, body=cuerpo_faker)
    
    assert respuesta_post.status_code == 201, f"Se esperaba 201, se obtuvo {respuesta_post.status_code}"
    datos_post = respuesta_post.json()
    
    # Validación de Esquema y Tipos (Requerimiento 5)
    assert "id" in datos_post and isinstance(datos_post["id"], int), "El ID debe existir y ser entero"
    assert datos_post["title"] == titulo_faker, "El título no coincide con el enviado por Faker"
    assert "createdAt" in datos_post, "Falta el campo 'createdAt'"
    
    # Guardamos el ID del recurso creado para usarlo en los siguientes pasos (Requerimiento 2)
    post_id = datos_post["id"]
    
    # -------------------------------------------------------------------------
    # PASO 2: PATCH /posts/{id} (Actualización de título)
    # -------------------------------------------------------------------------
    nuevo_titulo = "Título actualizado por QA" # Requerimiento 3
    
    respuesta_patch = update_post_api(post_id=post_id, title=nuevo_titulo)
    
    assert respuesta_patch.status_code == 200, f"Se esperaba 200, se obtuvo {respuesta_patch.status_code}"
    datos_patch = respuesta_patch.json()
    
    # Aserciones de control del PATCH
    assert datos_patch["id"] == post_id, "El ID del post cambió de manera inesperada"
    assert datos_patch["title"] == nuevo_titulo, "El título no se actualizó correctamente"
    assert "updatedAt" in datos_patch, "Falta el campo de tiempo 'updatedAt'"
    
    # Validación de Tiempo (Requerimiento 5): Comprobamos que incluya el año en curso
    anio_actual = str(datetime.now().year)
    assert anio_actual in datos_patch["updatedAt"], f"La fecha no corresponde al año actual {anio_actual}"
    
    # -------------------------------------------------------------------------
    # PASO 3: DELETE /posts/{id} (Eliminación)
    # -------------------------------------------------------------------------
    respuesta_delete = delete_post_api(post_id=post_id)
    
    # Valida código 200 OK (Requerimiento 4)
    assert respuesta_delete.status_code == 200, f"Se esperaba 200 al borrar, se obtuvo {respuesta_delete.status_code}"
    datos_delete = respuesta_delete.json()
    assert "message" in datos_delete, "La respuesta de borrado no contiene mensaje de confirmación"