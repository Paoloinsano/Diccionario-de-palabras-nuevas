meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "BUG": "error de un juego",
            "BRO": "Mejor amigo/persona a la que le tienes confianza",
            "CREEPY": "aterrador, siniestro",
            "AESTHETIC": "Algo muy bonito o hermoso",
            }
print("Bienvenido al diccionario de las palabras actuales")
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Lo lamento pero no tenemos esa palabra pero lo actualizaremos")
