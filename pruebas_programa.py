import montecarlo as mc


juego = mc.Juego()

equipo1 = juego.Crear_equipo("EQUIPO Dinamita")
equipo2 = juego.Crear_equipo("EQUIPO Loco")


detalles_E1 = mc.Mostrar_detalle_equipo(equipo1)

print(detalles_E1)

tiro1,tiro2 = juego.obtenerCantidadDisparos(equipo1,equipo2)

print(tiro1)
print(tiro2)