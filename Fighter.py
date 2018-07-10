class Fighter:

    def __init__(self, nome, eta, hp, attacco, difesa):

        self.nome = nome

        self.eta = eta

        self.hp = hp

        self.attacco = attacco

        self.difesa = difesa

    def __str__(self):

        return 'Combattente: ' + self.nome




