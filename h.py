Algoritmo Analizar_Riesgo

    Escribir "Nombre: "
    Leer nombre
    Escribir "Edad: "
    Leer edad
    Escribir "Peso: "
    Leer peso
    Escribir "Cantidad de vacunas recibidas: "
    Leer cantidad_vacunas

    Si (edad >= 18) Entonces
        Si (peso > 100 Y cantidad_vacunas < 2) Entonces
            Escribir "La persona ", nombre, " se encuentra en alto riesgo"
        Sino
            Si (peso < 100 Y cantidad_vacunas == 1) Entonces
                Escribir "La persona ", nombre, " se encuentra en riesgo normal"
            Sino Si (peso < 100 Y cantidad_vacunas == 0) Entonces
                Escribir "La persona ", nombre, " se encuentra en riesgo medio"
            Sino
                Escribir "La persona ", nombre, " no cuenta con la edad admitida para el análisis de datos"
            Fin Si
        Fin Si
    Sino
        Escribir "La persona ", nombre, " es menor de edad. El análisis de riesgo solo es para personas mayores de 18 años."
    Fin Si

FinAlgoritmo
