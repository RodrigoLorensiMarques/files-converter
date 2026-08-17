from config import PREFIXO_ATUALIZACAO, PREFIXO_NOVO

class PrefixoConta:

    def prefixo (self, diretorio):
    
        if "atualizacao" in str(diretorio):
            return f"{PREFIXO_ATUALIZACAO}numeroconta"


        elif "novo" in str(diretorio):
            return F"{PREFIXO_NOVO}numeroconta"

        return
