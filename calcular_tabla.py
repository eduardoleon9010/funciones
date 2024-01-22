# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:21:08 2024

@author: USUARIO
"""

def calcular_tabla(equipo1, equipo2, equipo3, marcador1, marcador2, marcador3, marcador4, marcador5, marcador6):
    """
    Calcula y devuelve la tabla de posiciones de un torneo de fútbol.

    Parámetros:
    - equipo1, equipo2, equipo3: Nombres de los tres equipos.
    - marcador1, marcador2, marcador3, marcador4, marcador5, marcador6:
      Marcadores de los tres partidos, en el orden en que se jugaron.

    Retorna:
    Una cadena de caracteres que representa la tabla de posiciones con la información organizada en columnas bien alineadas.

    La tabla incluye las siguientes columnas:
    - Posición,
    - Nombre del equipo,
    - Puntos obtenidos,
    - Partidos jugados,
    - Partidos ganados,
    - Partidos empatados,
    - Partidos perdidos,
    - Goles a favor,
    - Goles en contra,
    - Diferencia de goles

    Ejemplo de uso:
    equipo1 = "Equipo A"
    equipo2 = "Equipo B"
    equipo3 = "Equipo C"
    marcador1 = 2
    marcador2 = 1
    marcador3 = 0
    marcador4 = 2
    marcador5 = 1
    marcador6 = 1

    tabla_resultado = calcular_tabla(equipo1, equipo2, equipo3, marcador1, marcador2, marcador3, marcador4, marcador5, marcador6)
    print(tabla_resultado)
    """
    equipos = [equipo1, equipo2, equipo3]
    partidos = [(marcador1, marcador2), (marcador3, marcador4), (marcador5, marcador6)]

    tabla = []

    for i, equipo in enumerate(equipos):
        puntos = 0
        partidos_jugados = 0
        partidos_ganados = 0
        partidos_empatados = 0
        partidos_perdidos = 0
        goles_a_favor = 0
        goles_en_contra = 0

        for j, (gol_equipo, gol_rival) in enumerate(partidos):
            partidos_jugados += 1
            goles_a_favor += gol_equipo
            goles_en_contra += gol_rival

            if i == j:
                continue  # No se compara el equipo consigo mismo

            if gol_equipo > gol_rival:
                puntos += 3
                partidos_ganados += 1
            elif gol_equipo == gol_rival:
                puntos += 1
                partidos_empatados += 1
            else:
                partidos_perdidos += 1

        diferencia_goles = goles_a_favor - goles_en_contra

        # Agregar los datos a la tabla
        tabla.append({
            'equipo': equipo,
            'puntos': puntos,
            'partidos_jugados': partidos_jugados,
            'partidos_ganados': partidos_ganados,
            'partidos_empatados': partidos_empatados,
            'partidos_perdidos': partidos_perdidos,
            'goles_a_favor': goles_a_favor,
            'goles_en_contra': goles_en_contra,
            'diferencia_goles': diferencia_goles
        })

    # Ordenar la tabla por puntos, diferencia de goles y goles a favor
    tabla = sorted(tabla, key=lambda x: (x['puntos'], x['diferencia_goles'], x['goles_a_favor']), reverse=True)

    # Formatear la tabla como cadena de caracteres
    resultado = "Posición | Equipo         | Puntos | PJ | PG | PE | PP | GF | GC | Dif.\n"
    resultado += "--------------------------------------------------------\n"

    for i, equipo in enumerate(tabla):
        resultado += f"{i + 1:^9} | {equipo['equipo']:<14} | {equipo['puntos']:^6} | {equipo['partidos_jugados']:^2} | {equipo['partidos_ganados']:^2} | {equipo['partidos_empatados']:^2} | {equipo['partidos_perdidos']:^2} | {equipo['goles_a_favor']:^2} | {equipo['goles_en_contra']:^2} | {equipo['diferencia_goles']:^3}\n"

    return resultado

# Ejemplo de uso:
equipo1 = "Equipo A"
equipo2 = "Equipo B"
equipo3 = "Equipo C"
marcador1 = 2
marcador2 = 1
marcador3 = 0
marcador4 = 2
marcador5 = 1
marcador6 = 1

tabla_resultado = calcular_tabla(equipo1, equipo2, equipo3, marcador1, marcador2, marcador3, marcador4, marcador5, marcador6)
print(tabla_resultado)
