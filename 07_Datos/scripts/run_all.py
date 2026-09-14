# -*- coding: utf-8 -*-
"""Alias de la orden unica del paquete de datos SIGA.

    python 07_Datos/scripts/run_all.py

Hace exactamente lo mismo que `python 07_Datos/scripts/ejecutar.py`, con las
mismas opciones (--listar, --etapas). Existe porque la lista de verificacion de
la guia de cierre del docente, del 2026-09-14, invoca la orden con este nombre.
No duplica ninguna etapa: importa el orquestador y lo ejecuta.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ejecutar import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
