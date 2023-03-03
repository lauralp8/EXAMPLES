# TRAZAS
# modificaciones que aparecen printeados
import logging

logger = logging.getLogger()
# todo lo que sea de nivel igual o más importante que debug, sale por pantalla
logging.basicConfig(level = logging.DEBUG)

# todo lo que sea de nivel igual o más importante que warning, sale por pantalla
logging.basicConfig(level = logging.WARNING)

logging.basicConfig(format='%(asctime)s-%(module)s [%(levelname)] %(funcName)s:%(message)s', level= logging.DEBUG)

def cuadrado(x:int) -> int:
    """
    Function that squares a number given
    :param x: number
    :return: number^2
    """
    logger.info(f'Calling the function with value {x}')
    return x**2

numero = cuadrado(2)
print(numero)



