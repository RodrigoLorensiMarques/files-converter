from pathlib import Path

ARQUIVO_DIRETORIOS = Path("/Users/rodrigomarques/Documents/GitHub/files-converter/diretorios.txt")

DIRETORIOS = [
    Path(linha.strip())
    for linha in ARQUIVO_DIRETORIOS.read_text(encoding="utf-8").splitlines()
    if linha.strip() and not linha.startswith("#")
]
# Conversão
ESCALA = 1.0

# Ritmo de varredura
INTERVALO = 2


# Logs
LOG_ARQUIVO = Path("/Users/rodrigomarques/Documents/GitHub/files-converter/logs/pdf2gif.log")
LOG_NIVEL = "INFO"