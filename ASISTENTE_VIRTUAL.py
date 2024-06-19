import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generar datos ficticios
np.random.seed(42)  # Para reproducibilidad

n = 1000
ids = range(1, n+1)
ingresos = np.random.randint(1000, 5000, n)
egresos = np.random.randint(500, 4000, n)

data = {
    'ID': ids,
    'Ingresos': ingresos,
    'Egresos': egresos
}

df = pd.DataFrame(data)

# Título y subtítulo
st.title("Asistente Virtual para la Optimización Financiera Personalizada")
st.subheader("Gestión Integral de Egresos e Ingresos")

# Mostrar datos generados
st.header("Datos Generados")
st.write("A continuación se presentan los ingresos y egresos generados para 1000 personas:")

st.dataframe(df)

# Mostrar estadísticas descriptivas
st.header("Estadísticas Descriptivas")
st.write("Estadísticas descriptivas de los ingresos y egresos generados:")

st.write(df.describe())

# Gráfico de barras
st.header("Gráfico de Barras")
fig, ax = plt.subplots()
sns.barplot(data=df.melt(id_vars=['ID'], value_vars=['Ingresos', 'Egresos']), x='variable', y='value', ax=ax)
ax.set_title('Distribución de Ingresos y Egresos')
ax.set_xlabel('Tipo')
ax.set_ylabel('Monto')
st.pyplot(fig)

# Resumen de los resultados del gráfico de barras
st.subheader("Resumen del Gráfico de Barras")
max_ingresos = df['Ingresos'].max()
max_egresos = df['Egresos'].max()
st.write(f"El ingreso máximo registrado es {max_ingresos} y el egreso máximo registrado es {max_egresos}. Esto muestra la distribución de los montos máximos observados en la muestra de 1000 personas.")

# Gráfico de pastel
st.header("Gráfico de Pastel")
fig, ax = plt.subplots()
total_ingresos = df['Ingresos'].sum()
total_egresos = df['Egresos'].sum()
ax.pie([total_ingresos, total_egresos], labels=['Ingresos', 'Egresos'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
ax.set_title('Proporción de Ingresos y Egresos')
st.pyplot(fig)

# Resumen de los resultados del gráfico de pastel
st.subheader("Resumen del Gráfico de Pastel")
proporcion_ingresos = total_ingresos / (total_ingresos + total_egresos) * 100
proporcion_egresos = total_egresos / (total_ingresos + total_egresos) * 100
st.write(f"Los ingresos representan aproximadamente el {proporcion_ingresos:.1f}% y los egresos representan aproximadamente el {proporcion_egresos:.1f}% del total de la muestra. Esto muestra la proporción de ingresos y egresos en relación con el total.")

