asignaturas = ["matemáticas", "lengua", "física", "química", "ef"]
notas_asig = []
for asignatura in asignaturas: 
    notas = float(input("introduce las notas de cada asignatura: "))
    if notas < 5:
            notas_asig.append(asignatura)
print(notas_asig)