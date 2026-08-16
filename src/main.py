import logging
import time
from watcher import DirectoryWatcher
from converter import ConvertPDFtoGIF
from compressor import GifCompressor
from config import ESCALA,INTERVALO, DIRETORIOS
import log_setup


log_setup.configurar()

log = logging.getLogger("main")



watcher = DirectoryWatcher()
conversor = ConvertPDFtoGIF(ESCALA)
compressor = GifCompressor()

log.info("iniciado — monitorando %d diretório(s)", len(DIRETORIOS))


while True:
    for diretorio in DIRETORIOS:
        pdfs = watcher.varrer(diretorio)

        if pdfs:
            gifs = conversor.converter_lote(pdfs, diretorio)
            prontos = compressor.comprimir_lote(gifs)

            convertidos = {gif.stem for gif in gifs}
            for pdf in pdfs:
                if pdf.stem in convertidos:
                    pdf.unlink()

    time.sleep(INTERVALO)