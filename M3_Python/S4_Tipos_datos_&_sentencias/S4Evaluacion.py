#Requerimos crear un registro de datos personales de tres personas.
# diccionarios
# clave: valor

#Los datos que se necesitan son: su nombre, apellido y teléfono
persona_uno = {'nombre': 'Miguel', 'apellido': 'Luis', 'telefono': 1234567890}

persona_dos = {
    'nombre': 'Andres', 
    'apellido': 'Gonzalez', 
    'telefono': 3234567891
    }

persona_tres = {'nombre': 'Isabela', 'apellido': 'Andrade', 'telefono': 2434567892}

lista_personas = [persona_uno, persona_dos, persona_tres]
print(lista_personas)

lista_personas[0]['nombre'] = 'Miguelito' # Modificar un valor



# diccionario de diccionarios
personas = {
    'persona_uno' : {'nombre': 'Miguel', 'apellido': 'Luis', 'telefono': 1234567890},
    'persona_dos' : {
    'nombre': 'Andres', 
    'apellido': 'Gonzalez', 
    'telefono': 3234567891
    },
    'persona_tres' : {'nombre': 'Isabela', 'apellido': 'Andrade', 'telefono': 2434567892},
    'persona_cuatro' : {
        'nombre': 'Maria', 
        'apellido': 'Andrade', 
        'telefono': 1234567890,
        'direccion': {
            'calle': 'calle 1',
            'numero': 123,
            'region': 'Metropolitana'
        }
    }
}

#diccionario[clave][subclave]
print(personas['persona_uno']['nombre'])
print(personas['persona_cuatro']['direccion']['region'])
