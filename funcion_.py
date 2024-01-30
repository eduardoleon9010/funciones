# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:43:00 2024

@author: USUARIO
"""
def escoger_carta(carta_mano, opcion_1, opcion_2):
    """
    Indica la opción de carta que el apostador debería escoger para hacer trampa.

    Parámetros:
    - carta_mano (dict): Diccionario representando la carta en la mano.
    - opcion_1 (dict): Diccionario representando la primera carta escondida.
    - opcion_2 (dict): Diccionario representando la segunda carta escondida.

    Resultado:
    - int: 1 para la primera carta escondida, 2 para la segunda carta escondida, 0 si ninguna ayuda al apostador.
    """
    def coincide_numero_o_palo(carta_1, carta_2):
        return (carta_1["numero"] == carta_2["numero"]) or (carta_1["palo"] == carta_2["palo"])

    if coincide_numero_o_palo(carta_mano, opcion_1) and coincide_numero_o_palo(carta_mano, opcion_2):
        return 1
    elif coincide_numero_o_palo(carta_mano, opcion_1):
        return 1
    elif coincide_numero_o_palo(carta_mano, opcion_2):
        return 2
    else:
        return 0

# Ejemplo de uso:
carta_en_mano = {"numero": "A", "palo": "Corazones"}
opcion_1 = {"numero": "K", "palo": "Corazones"}
opcion_2 = {"numero": 7, "palo": "Diamantes"}

opcion_elegida = escoger_carta(carta_en_mano, opcion_1, opcion_2)
print("El apostador debería escoger la opción:", opcion_elegida)
