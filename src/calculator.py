import logging

logger = logging.getLogger(__name__)

def add(a, b):
    """Return the sum of a and b."""
    logger.info(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    logger.info(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    logger.info(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    """Return the result of dividing a by b. Raises ValueError if b == 0."""
    logger.info(f"Dividing {a} / {b}")
    if b == 0:
        logger.error("Attempted division by zero")
        raise ValueError("Cannot divide by zero")
    return a / b