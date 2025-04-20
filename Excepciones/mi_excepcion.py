
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")

# Lanzando mi propia excepcion
# raise MiExcepcion("jajajjajaja, persona poco culta")

# Manejandola
try:
    raise MiExcepcion("jajajjajaja, persona poco culta")
except:  # noqa: E722
    print("como vas a cometer ese error?")
