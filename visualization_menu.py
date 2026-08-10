# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 21:05:26 2026

PROYECTO FINAL 
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype

df=pd.read_csv("C:\\Users\\Tati\\Documents\\Curso Python Tecmilenio\\Procesamiento de datos\\proyecto final\\gaming.csv", encoding="utf-8")

#Eliminación de nulos y agrupamiento para análisis
df_estudiantes = df[
    df["grades_gpa"].notna() &
    df["work_productivity_score"].isna()]

df_empleados = df[
    df["work_productivity_score"].notna() &
    df["grades_gpa"].isna()]

df_ambos = df[
    df["grades_gpa"].notna() &
    df["work_productivity_score"].notna()]

#Definición de columnas str
columnas_validas = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

#funciones
def filtro_por_juego(df, ):
    
    print("\nJuegos disponibles:")   
    juegos_disponibles = df["primary_game"].unique()
    for i, juego in enumerate(juegos_disponibles.tolist(), 1):
        print(f"{i}. {juego}")
    
    titulo = input("\nIntroduce el nombre de un juego: ")

    if titulo not in juegos_disponibles:
        print("Opción invalida. ")
        return
    
    df_filtro_por_juego = df[df['primary_game']==titulo] 
    
    return print(df_filtro_por_juego)

def promedio_edad(df):
    return print(df["age"].mean())


# Poblacion de participante en cada df

def poblacion():
    print("Número de participantes por grupo: ")
    print("\nEstudiantes:", len(df_estudiantes))
    print("Empleados:", len(df_empleados))
    print("Trabajan y estudian:", len(df_ambos))
    print("Todos:", len(df))
    return

poblacion()

#Creación de gráfica utilizando  user input
def distribucion_columna_str():
    
    print("Tablas disponibles:")
    print("\n1. Empleados")
    print("2. Estudiantes")
    print("3. Trabajan y estudian")
    print("4. Todos")
    
    opcion_tabla = input("\nElige una opción (1-4): ")
    
    #creación de lista de posibles respuestas
    tablas = {
        "1": ("df_empleados", df_empleados),
        "2": ("df_estudiantes", df_estudiantes),
        "3": ("df_ambos", df_ambos),
        "4": ("df", df)
    }
    #tupla en caso de error
    if opcion_tabla not in tablas:
        print("Opción inválida, introduzca un número del 1 al 4: ")
        return
    
    #Aquí se define el df que se va a utilizar, y el nombre que se presentará en el título de la tabla
    
    nombre_df, df_usuario = tablas[opcion_tabla]
    
    #convertir una lista del diccionario a una lista hecha texto, esto es más "future proof" que la lista de arriba
    print("\nColumnas disponibles:")
    for i, col in enumerate(columnas_validas[1:], 1):
        print(f"{i}. {col}")
    
    columna_usuario = input("\nEscribe el nombre de la columna de la lista arriba: ")
    
    if columna_usuario not in columnas_validas:
           print("Columna inválida.")
           return
    
    #Se terminan de definir los parametros para la gráfica de barras utilizando las respuestas del usuario
    #se instruye contar valores y se organizan de menor a mayor
    
    frecuencia = df_usuario[columna_usuario].value_counts().sort_values()
    
    plt.figure()
    frecuencia.plot(kind="bar")
    
    plt.title(f"Frecuencia de {columna_usuario} en {nombre_df}")
    plt.xlabel(columna_usuario)
    plt.ylabel("Frecuencia")

    plt.tight_layout()
    plt.show()
    
    return frecuencia

#distribucion_columna_str()

#-------------------------------------------------------------------------------------------
#Barras juntas

def barras_comparativas(): 
    
    print("\nColumnas disponibles:")
    for i, col in enumerate(df[1:], 1):
        print(f"{i}. {col}")
         
    columna_comparar = input("\n¿Qué valor deseas comparar? ")
    
    if columna_comparar not in df.columns: 
        print("La columna no existe. ") 
        return 
    
    #Para valores númericos: Barra promedio
    if is_numeric_dtype(df_estudiantes[columna_comparar]):
        
        estudiantes = df_estudiantes[columna_comparar].mean() 
        empleados = df_empleados[columna_comparar].mean() 
        ambos = df_ambos[columna_comparar].mean() 
        
        df_comparativa = pd.DataFrame({
            "Grupo": ["Estudiantes", "Empleados", "Trabajan y estudian"], 
            "Promedio": [estudiantes, empleados, ambos] }) 
        
        ax = df_comparativa.plot(kind="bar", x="Grupo", y="Promedio", figsize=(8,5)) 
        plt.title(f"Comparación de {columna_comparar}") 
        plt.xlabel("Grupo") 
        plt.ylabel("Promedio") 
        plt.legend() 
        
        for barra in ax.patches:
            altura = barra.get_height()
            ax.text(
                barra.get_x() + barra.get_width()/2,
                altura,
                f"{altura:.2f}",
                ha="center",
                va="bottom"
    )
        
        plt.show() 
        
    #Para valores categóricos se crean barras comparativas    
    else:
        
        estudiantes = df_estudiantes[columna_comparar].value_counts()
        empleados = df_empleados[columna_comparar].value_counts()
        ambos = df_ambos[columna_comparar].value_counts()
     
        df_comparativa = pd.concat(
             [estudiantes, empleados, ambos],
             axis=1,
             keys=["Estudiantes", "Empleados", "Trabajan y estudian"]
         ).fillna(0)
    
        df_comparativa.plot(kind="bar", figsize=(8,5))
        plt.ylabel("Frecuencia")
    
        plt.title(f"Comparación de {columna_comparar}")
        plt.xlabel("Grupo / Categoría")
        plt.tight_layout()
        
        ax = df_comparativa.plot(kind="bar", figsize=(8,5))

        for barra in ax.patches:
            altura = barra.get_height()
            ax.text(
                barra.get_x() + barra.get_width()/2,
                altura,
                int(altura),
                ha="center",
                va="bottom"
            )
        
        plt.show()
    
#barras_comparativas()

#----------------------------------------------------------------------------------------------------------------------

#grafica dispercion
    
    plt.figure()
    plt.scatter(df["exercise_hours_weekly"], df["weight_change_kg"]) #tener la misma dimension de datos (x, y)
    plt.title("Relación horas de ejercicio vs peso en kilos adquirido")
    plt.xlabel("exercise_hours_weekly")
    plt.ylabel("weight_change_kg")
    plt.tight_layout()
    plt.show()
    
    
    plt.figure()
    plt.scatter(df["daily_gaming_hours"], df["sleep_hours"]) #tener la misma dimension de datos (x, y)
    plt.title("Relación horas de juego vs horas de sueño")
    plt.xlabel("daily_gaming_hours")
    plt.ylabel("sleep_hours")
    plt.tight_layout()
    plt.show()
    
    return

#-------------------------------------------------------------------
#Creación de Menú

while True: 
    print("\n=====Herramienta de Análisis de Datos en: 'Gaming and Mental Health'=====")
    print("\n1. Producir una gráfica de barras")
    print("2. Comparar columnas entre grupos")
    print("3. Filtro por juego")
    print("4. Edad promedio participantes")
    print("5. Cantidad de participantes por grupo")
    print("6. Gráficas de dispersión sueño y ejercicio")
    print("7. Salir")

    
    opcion=input("\nSelecciona una opción del Menú: ")
    
    if opcion =="1":
        distribucion_columna_str()
    
    elif opcion =="2":
        barras_comparativas()
        
    elif opcion =="3":
        filtro_por_juego(df, )
        
    elif opcion =="4":
        promedio_edad(df)
    
    elif opcion =="5":
        poblacion()
    
    elif opcion =="6":
                
        plt.figure()
        plt.scatter(df["exercise_hours_weekly"], df["weight_change_kg"]) #tener la misma dimension de datos (x, y)
        plt.title("Relación horas de ejercicio vs peso en kilos adquirido")
        plt.xlabel("exercise_hours_weekly")
        plt.ylabel("weight_change_kg")
        plt.tight_layout()
        plt.show()
        
        
        plt.figure()
        plt.scatter(df["daily_gaming_hours"], df["sleep_hours"]) #tener la misma dimension de datos (x, y)
        plt.title("Relación horas de juego vs horas de sueño")
        plt.xlabel("daily_gaming_hours")
        plt.ylabel("sleep_hours")
        plt.tight_layout()
        plt.show()
        
    elif opcion =="7":
         print("Procesamiento terminado")
         break
    else:
        print("Opción no válida")
        
## USO DE FLASK


from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formato.html')



@app.route('/guardar', methods=['POST'])
def guardar():
        record_id = request.form['record_id']
        age = request.form['age']
        gender = request.form['gender']
        daily_gaming_hours = request.form['daily_gaming_hours']
        game_genre = request.form['game_genre']
        primary_game = request.form['primary_game']
        gaming_platform = request.form['gaming_platform']
        sleep_hours = request.form['sleep_hours']
        sleep_quality = request.form['sleep_quality']
        sleep_disruption_frequency = request.form['sleep_disruption_frequency']
        academic_work_performance = request.form['academic_work_performance']
        grades_gpa = request.form['grades_gpa']
        work_productivity_score = request.form['work_productivity_score']
        mood_state = request.form['mood_state']
        mood_swing_frequency = request.form['mood_swing_frequency']
        withdrawal_symptoms = request.form['withdrawal_symptoms']
        loss_of_other_interests = request.form['loss_of_other_interests']
        continued_despite_problems = request.form['continued_despite_problems']
        eye_strain = request.form['eye_strain']
        back_neck_pain = request.form['back_neck_pain']
        weight_change_kg = request.form['weight_change_kg']
        exercise_hours_weekly = request.form['exercise_hours_weekly']
        social_isolation_score = request.form['social_isolation_score']
        face_to_face_social_hours_weekly = request.form['face_to_face_social_hours_weekly']
        monthly_game_spending_usd = request.form['monthly_game_spending_usd']
        years_gaming = request.form['years_gaming']
        gaming_addiction_risk_level = request.form['gaming_addiction_risk_level']


        archivo_csv = 'gaming.csv'

        campos = [
            'record_id','age','gender','daily_gaming_hours','game_genre',
            'primary_game','gaming_platform','sleep_hours','sleep_quality',
            'sleep_disruption_frequency','academic_work_performance','grades_gpa',
            'work_productivity_score','mood_state','mood_swing_frequency',
            'withdrawal_symptoms','loss_of_other_interests',
            'continued_despite_problems','eye_strain','back_neck_pain',
            'weight_change_kg','exercise_hours_weekly','social_isolation_score',
            'face_to_face_social_hours_weekly','monthly_game_spending_usd',
            'years_gaming','gaming_addiction_risk_level'
        ]

        escribir_cabecera = (not os.path.exists(archivo_csv)) or (os.path.getsize(archivo_csv) == 0)

        with open(archivo_csv, mode='a', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=campos)

            if escribir_cabecera:
                w.writeheader()

            w.writerow({
                'record_id': record_id,
                'age': age,
                'gender': gender,
                'daily_gaming_hours': daily_gaming_hours,
                'game_genre': game_genre,
                'primary_game': primary_game,
                'gaming_platform': gaming_platform,
                'sleep_hours': sleep_hours,
                'sleep_quality': sleep_quality,
                'sleep_disruption_frequency': sleep_disruption_frequency,
                'academic_work_performance': academic_work_performance,
                'grades_gpa': grades_gpa,
                'work_productivity_score': work_productivity_score,
                'mood_state': mood_state,
                'mood_swing_frequency': mood_swing_frequency,
                'withdrawal_symptoms': withdrawal_symptoms,
                'loss_of_other_interests': loss_of_other_interests,
                'continued_despite_problems': continued_despite_problems,
                'eye_strain': eye_strain,
                'back_neck_pain': back_neck_pain,
                'weight_change_kg': weight_change_kg,
                'exercise_hours_weekly': exercise_hours_weekly,
                'social_isolation_score': social_isolation_score,
                'face_to_face_social_hours_weekly': face_to_face_social_hours_weekly,
                'monthly_game_spending_usd': monthly_game_spending_usd,
                'years_gaming': years_gaming,
                'gaming_addiction_risk_level': gaming_addiction_risk_level
            })
         

        return redirect('/')


if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1", port=5000)
