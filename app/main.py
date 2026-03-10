import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from db.monitor import monitorar

monitorar(intervalo_segundos=60)