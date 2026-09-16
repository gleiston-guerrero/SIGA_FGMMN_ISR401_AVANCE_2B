# ============================================================
# SIGA — Pipeline de analisis reproducible del componente empirico
# Entrega 4 (2B) · Equipo FGMMN · UTEQ · ISR-401
#
# Uso:   cd 06_Experimento && make all
#
# REGLA: ninguna cifra, tabla o figura del manuscrito se escribe a
# mano. Todo se genera desde datos_crudos/ ejecutando este pipeline.
# Una cifra no reproducible activa el gatekeeper G4.
# ============================================================

PY      := python
SCRIPTS := ./scripts_analisis
CRUDOS  := ./datos_crudos
PROC    := ./datos_procesados
RES     := resultados
FIGS    := ../07_Publicacion/figuras
TABS    := ../07_Publicacion/tablas

.PHONY: all clean deps verificar entorno consolidar acuerdo supuestos \
        hipotesis efectos saturacion potencia figuras tablas

# ---- Objetivo principal -------------------------------------------------
all: entorno consolidar acuerdo supuestos hipotesis efectos saturacion \
     potencia figuras tablas
	@echo ""
	@echo "== Pipeline completo. Tablas en $(TABS)/ y figuras en $(FIGS)/ =="
	@echo "== Verifique que cada cifra del manuscrito provenga de aqui.  =="

# ---- Preparacion --------------------------------------------------------
deps:
	$(PY) -m pip install -r requirements.txt

entorno:
	@mkdir -p $(PROC) $(RES) $(FIGS) $(TABS)
	@$(PY) --version
	@$(PY) -m pip freeze > $(RES)/entorno_python.txt
	@echo "-> Entorno registrado en $(RES)/entorno_python.txt"

# ---- Etapa 1: consolidacion de datos crudos -----------------------------
# Lee las hojas de puntuacion de cada juez desde datos_crudos/ y produce
# un unico dataframe largo (juez, item, dimension, puntuacion, origen).
consolidar: entorno
	$(PY) $(SCRIPTS)/analizar_resultados.py --etapa consolidar \
		--entrada $(CRUDOS) --salida $(PROC)

# ---- Etapa 2: acuerdo inter-evaluador -----------------------------------
# Kappa de Cohen ponderado lineal por par de jueces y kappa de Fleiss
# para el conjunto completo, por dimension.
acuerdo: consolidar
	$(PY) $(SCRIPTS)/analizar_resultados.py --etapa acuerdo \
		--entrada $(PROC) --salida $(RES)

# ---- Etapa 3: pruebas de supuestos --------------------------------------
# Shapiro-Wilk (normalidad) y Levene (homogeneidad de varianzas).
supuestos: consolidar
	$(PY) $(SCRIPTS)/analizar_resultados.py --etapa supuestos \
		--entrada $(PROC) --salida $(RES)

# ---- Etapa 4: pruebas de hipotesis --------------------------------------
# t apareada si Shapiro-Wilk no rechaza normalidad; Wilcoxon de rangos
# con signo en caso contrario. Correccion de Holm-Bonferroni por
# comparaciones multiples (5 dimensiones).
hipotesis: supuestos
	$(PY) $(SCRIPTS)/analizar_resultados.py --etapa hipotesis \
		--entrada $(PROC) --salida $(RES) --correccion holm

# ---- Etapa 5: tamanos de efecto -----------------------------------------
# d de Cohen (parametrico) o delta de Cliff (no parametrico), con
# intervalos de confianza al 95 % por bootstrap de 10 000 replicas.
efectos: hipotesis
	$(PY) $(SCRIPTS)/analizar_resultados.py --etapa efectos \
		--entrada $(PROC) --salida $(RES) --bootstrap 10000 --semilla 20260802

# ---- Etapa 6: curva de saturacion temica --------------------------------
# Codigos nuevos acumulados por entrevista, en orden cronologico.
saturacion: entorno
	$(PY) $(SCRIPTS)/curva_saturacion.py \
		--entrada ../02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv \
		--salida $(FIGS)/curva_saturacion.png \
		--tabla $(TABS)/saturacion_por_entrevista.csv

# ---- Etapa 6b: calculo de potencia estadistica --------------------------
# Via alterna al criterio C6 cuando la curva de saturacion no muestra
# inflexion (Enfoque 1). Cohen d=0.5, alpha=0.05, potencia deseada=0.80.
potencia: entorno
	$(PY) $(SCRIPTS)/power_calculation.py \
		--n-actual $(words $(wildcard $(CRUDOS)/juez*.csv)) \
		--salida-csv $(RES)/power_calculation.csv \
		--salida-tex $(TABS)/tabla_power_calculation.tex

# ---- Etapa 7: figuras y tablas del manuscrito ---------------------------
figuras: efectos
	$(PY) $(SCRIPTS)/generar_figuras.py --entrada $(RES) --salida $(FIGS) --procesados $(PROC)

tablas: efectos
	$(PY) $(SCRIPTS)/generar_tablas.py --entrada $(RES) --salida $(TABS) --procesados $(PROC) \
		--acuerdo-ic ../07_Datos/resultados/acuerdo_interevaluador_ic.csv

# ---- Verificacion de integridad de la evidencia -------------------------
# Todo el material audiovisual vive dentro de este repositorio. Este
# objetivo comprueba que cada archivo de audio y de video declarado es real
# y del tipo declarado, y que el manifiesto de sumas cuadra sobre el arbol.
#
# Requiere ffprobe (FFmpeg) en el PATH.
#
# Uso:  make verificar

verificar:
	@echo "== Sondeo de codec y duracion sobre el material de entrevista =="
	@find ../02_Evidencias/Video ../02_Evidencias/Audio ../05_MVP/demostracion -type f \
		\( -name '*.mp4' -o -name '*.mp3' -o -name '*.wav' \) \
		-exec sh -c 'printf "%s  " "$$1"; ffprobe -v error \
		-show_entries format=duration,format_name -of csv=p=0 "$$1" \
		|| echo "ARCHIVO INVALIDO"' _ {} \;
	@echo ""
	@echo "== Verificacion del manifiesto de sumas sobre todo el arbol =="
	@cd .. && sha256sum -c checksums.sha256 --quiet && echo "Manifiesto correcto."
	@echo ""
	@echo "== Cada cifra afirmada en prosa, contra la salida que la sostiene =="
	@cd .. && $(PY) 07_Publicacion/verificar_afirmaciones.py

# ---- Limpieza -----------------------------------------------------------
# No borra datos_crudos/: son evidencia primaria irremplazable.
clean:
	rm -rf $(PROC)/* $(RES)/*.csv $(RES)/*.png
	@echo "-> Derivados eliminados. datos_crudos/ intacto."
