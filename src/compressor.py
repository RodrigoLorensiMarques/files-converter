from pathlib import Path
from PIL import Image
import logging


log = logging.getLogger(__name__)


LIMITE = 50 * 1024
FATORES = [0.85, 0.7, 0.6, 0.5, 0.4]


class GifCompressor:

    def comprimir(self, gif: Path) -> bool:
        if gif.stat().st_size <= LIMITE:
            return True

        original = Image.open(gif).copy()
        largura, altura = original.size

        for fator in FATORES:
            novo = original.resize(
                (int(largura * fator), int(altura * fator)), Image.LANCZOS
            ).convert("1", dither=Image.Dither.NONE)
            novo.save(gif, optimize=True)
            if gif.stat().st_size <= LIMITE:
                return True

        return False

    def comprimir_lote(self, pares: list[tuple[Path, Path]]) -> list[tuple[Path, Path]]:
        prontos = []
        for pdf, gif in pares:
            try:
                if self.comprimir(gif):
                    prontos.append((pdf, gif))
            except Exception:
                log.exception("falha ao comprimir: %s", gif.name)
        return prontos