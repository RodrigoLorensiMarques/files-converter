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
        try:
            pdfs = watcher.varrer(diretorio)

            if pdfs:
                pares = conversor.converter_lote(pdfs, diretorio)
                prontos = compressor.comprimir_lote(pares)

                for pdf, gif in prontos:
                    pdf.unlink()
        except Exception:
            log.exception("falha ao processar diretório: %s", diretorio)

    time.sleep(INTERVALO)