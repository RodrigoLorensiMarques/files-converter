from pathlib import Path
import logging
import pypdfium2 as pdfium
from PIL import Image
from prefixo_conta import PrefixoConta

log = logging.getLogger(__name__)


class ConvertPDFtoGIF:

    def __init__(self, escala=2.0):
        self.escala = escala

    def converter(self, pdf: Path, destino: Path) -> Path:
        doc = pdfium.PdfDocument(pdf)
        try:
            if len(doc) == 0:
                raise ValueError("PDF sem páginas")
            if len(doc) > 1:
                log.warning("%s contém %d páginas - convertendo primeira página",
                            pdf.name, len(doc))

            img = doc[0].render(scale=self.escala, grayscale=True).to_pil()
        finally:
            doc.close()

        img.convert("1", dither=Image.Dither.NONE).save(destino, optimize=True)
        return destino

    def converter_lote(self, pdfs: list[Path], pasta_saida: Path) -> list[tuple[Path, Path]]:
        gerados = []
        prefixo = PrefixoConta().prefixo(pasta_saida)

        for pdf in pdfs:
            destino = pasta_saida / f"{prefixo}_{pdf.stem}.gif"
            try:
                self.converter(pdf, destino)
                kb = destino.stat().st_size // 1024
                log.info("convertido: %s -> %s (%d KB)", pdf.name, destino.name, kb)
                gerados.append((pdf, destino))
            except Exception:
                log.exception("falha ao converter: %s", pdf.name)
        return gerados