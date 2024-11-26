
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO)

def log_info(message):
    """Registra un mensaje informativo."""
    logging.info(message)

def log_error(message):
    """Registra un mensaje de error."""
    logging.error(message)