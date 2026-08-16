
class DirectoryWatcher:

    def __init__(self):
        self._tamanhos = {}


    def varrer(self, diretorio):
        novos_arquivos = []


        for pdf in diretorio.glob("*.pdf"):

            tamanho_atual = pdf.stat().st_size

            if tamanho_atual > 0 and self._tamanhos.get(pdf) == tamanho_atual:
                del self._tamanhos[pdf]

                novos_arquivos.append(pdf)

            else:
                self._tamanhos[pdf] = tamanho_atual

        return novos_arquivos