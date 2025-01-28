schema = [
    {
        "type": "function",
        "function": {
            "name": "get_trello_board_info",
            "description": "Obtiene toda la información de un tablero de Trello incluyendo listas, tarjetas y miembros. Muestra los IDs de las listas y tarjetas.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_card_to_list",
            "description": "Crea una nueva tarjeta en una lista específica de Trello. Puedes usar el ID de la lista o su nombre.",
            "parameters": {
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "ID o nombre de la lista donde se creará la tarjeta. Ejemplo: '12345' o 'Lista de Tareas'",
                    },
                    "name": {"type": "string", "description": "Nombre de la tarjeta."},
                    "description": {"type": "string", "description": "Descripción de la tarjeta."},
                },
                "required": ["list_id", "name", "description"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_card",
            "description": "Elimina una tarjeta de Trello usando su ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "card_id": {
                        "type": "string",
                        "description": "ID de la tarjeta a eliminar. Usa get_trello_board_info() para obtener los IDs.",
                    },
                },
                "required": ["card_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_list_cards",
            "description": "Obtiene todas las tarjetas de una lista específica. Puedes usar el ID de la lista o su nombre.",
            "parameters": {
                "type": "object",
                "properties": {
                    "list_id": {
                        "type": "string",
                        "description": "ID o nombre de la lista. Ejemplo: '12345' o 'Lista de Tareas'",
                    },
                },
                "required": ["list_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_card_descriptions",
            "description": "Busca un término específico en las descripciones de todas las tarjetas del tablero de Trello.",
            "parameters": {
                "type": "object",
                "properties": {
                    "search_term": {
                        "type": "string",
                        "description": "Término a buscar en las descripciones de las tarjetas"
                    }
                },
                "required": ["search_term"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_user_repos",
            "description": "Lista todos los repositorios del usuario autenticado en GitHub, mostrando detalles como nombre, privacidad, descripción, estrellas y última actualización.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "print_repo_contents",
            "description": "Muestra el contenido de un repositorio de GitHub de forma recursiva, incluyendo archivos y directorios.",
            "parameters": {
                "type": "object",
                "properties": {
                    "repo_name": {
                        "type": "string",
                        "description": "Nombre del repositorio a explorar"
                    },
                    "path": {
                        "type": "string",
                        "description": "Ruta dentro del repositorio (opcional)",
                        "default": "",
                    },
                    "level": {
                        "type": "integer",
                        "description": "Nivel de indentación (opcional)",
                        "default": 0,
                    },
                },
                "required": ["repo_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_branches",
            "description": "Lista todas las ramas (branches) de un repositorio específico de GitHub.",
            "parameters": {
                "type": "object",
                "properties": {
                    "repo_name": {
                        "type": "string",
                        "description": "Nombre del repositorio del cual listar las ramas"
                    },
                },
                "required": ["repo_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "show_commit_history",
            "description": "Muestra el historial de commits de un repositorio de GitHub, incluyendo detalles como autor, fecha y mensaje.",
            "parameters": {
                "type": "object",
                "properties": {
                    "repo_name": {
                        "type": "string",
                        "description": "Nombre del repositorio del cual mostrar el historial"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Número máximo de commits a mostrar (opcional)",
                        "default": 30,
                    },
                },
                "required": ["repo_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_rag",
            "description": "Realiza una consulta al sistema RAG (Retrieval-Augmented Generation) que busca información relevante en la base de conocimientos y genera una respuesta contextual en español.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query_text": {
                        "type": "string",
                        "description": "Texto de la pregunta o consulta a realizar al sistema RAG"
                    }
                },
                "required": ["query_text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_latest_card",
            "description": "Obtiene la información de la última tarjeta agregada al tablero de Trello, incluyendo su nombre, descripción, fecha de creación y lista donde se encuentra.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
]
