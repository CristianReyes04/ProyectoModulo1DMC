import streamlit as st
import numpy as np
import libreria_funciones as lf

st.title("Proyecto módulo 1 Fundamentals")
st.image("Logo_python.png")
st.sidebar.image("Logo_inst.png")
st.sidebar.title("Módulos")

modulo = st.sidebar.selectbox("Elija un módulo", ["Módulo Listas","Módulo Array","Módulo funciones"])
if modulo == "Módulo Listas":
  valor_inicial = st.number_input("Ingrese el valor inicial: ", value=0)
  valor_final = st.number_input("Ingrese el valor Final: ", value=1)
  lista_numerica = list(range(valor_inicial,valor_final))
  #similar a print es write
  st.write(lista_numerica)
elif modulo == "Módulo Array":
  st.write("Estas en el módulo de arreglos")
  limite_inferior = st.number_input("Ingrese el límite inferior", value=1200)
  limite_superior = st.number_input("Ingrese el límite superior", value = 1250)
  cantidad_datos =  st.number_input("Ingrese totalidad de datos a crear", value = 3)
  datos_produccion = np.random.randint(limite_inferior, limite_superior, cantidad_datos)
  st.write(datos_produccion)
  st.write("La producción total es:" ,  np.sum(datos_produccion))
  st.write("La producción promedio es:" , np.mean(datos_produccion) )
else:
  st.write("Estas en el módulo de funciones")
  principal = st.number_input("Ingrese Montos del Prestamo", value=0)
  tasa_anual = st.number_input("Ingrese Tasa Anual en decimal", value= 0.10)
  anios = st.number_input("Ingrese el Numero años del prestamo", value=1)
  pagos_por_anios = st.number_input("Ingrese cantidad pagos por año", value=12)
  cuota = lf.cuota_prestamo(principal,tasa_anual,anios,pagos_por_anios)
  st.write("La cuota del prestamo es:", cuota)

