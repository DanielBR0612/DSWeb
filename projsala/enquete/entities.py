class Alternativa:
    def __init__(self, ):

class Enquete:
    def __init__(self, id: int, texto: str, votos: int = 0):
        self.id = id
        self.texto = texto
        self.votos = votos
    
    def __str__(self):
        return f"Enquete(id={self.id}, texto='{self.texto}', votos={self.votos})"
        