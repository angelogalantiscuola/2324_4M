#Es 8 
class  Conto:
    def __init__(self,id_conto,intestato,iban,saldo_disponibile,patrimonio_investito):
        self.id_conto=id_conto
        self.intestato=intestato
        self.iban=iban
        self.saldo_disponibile=saldo_disponibile
        self.patrimonio_investito=patrimonio_investito
    def dep(self,deposito):
        self.saldo_disponibile=(deposito+self.saldo_disponibile)
    def pre(self,prelievo):
        self.saldo_disponibile=(prelievo-self.saldo_disponibile)
    def inv(self,investimento):
        self.patrimonio_investito=(investimento+self.patrimonio_investito)
        self.saldo_disponibile=(self.saldo_disponibile-investimento)
    def disinv(self,disinvesti):
        self.patrimonio_investito=(self.patrimonio_investito-disinvesti)
        self.saldo_disponibile=(self.saldo_disponibile+disinvesti)
constructor=Conto("345436", "Pino", "IT 12 A 12345 12345 123456789012", 1700000, 13000000)
