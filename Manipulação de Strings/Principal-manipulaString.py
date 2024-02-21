from manipulaString import Manipulador_de_Strings

manip = Manipulador_de_Strings('Instituto Federal')

print('\nTexto Invertido:')
print(manip.inverterTexto())

print('\nNovo texto:')
manip.setTexto('ifsp')
print(manip.texto)

print('\nTexto em maiusculo:')
print(manip.maiuscula())

print('\nAbreviar nome:')
manip.setTexto("PEDRO LUCAS CALVO BASCHONI")
print(manip.abreviar())
manip.setTexto("Abigail Baratela do Carmo")
manip.setTexto(manip.maiuscula())
print(manip.abreviar())

