import funciones_lectura_archivos as tools

lineas= tools.leer_archivo("noticia.txt")
tools.mostrar_lineas(lineas)
Texto = ["La educación es el medio para reconstruir la sociedad colombiana, que a través de los años ha sido azotada por\n",
"el látigo del terrorismo y la violencia. Esta misma, apoyada en el arte, puede construir nuevos caminos para cada uno\n",
"de los jóvenes que están afectados por estos conflictos, puede llevarlos a que hagan sus sueños realidad y a que\n",
"amplíen su horizonte. Ellos, los jóvenes, guiados por maestros comprometidos con su educación y que hacen que trascienda\n",
"y sea para la paz, pueden lograr grandes cosas."]
tools.escritura_archivo("Opinion.txt",Texto)

tools.agregar_lineas_archivo("noticia.txt","\nAbril 20 del 2020, El nuevo siglo")

