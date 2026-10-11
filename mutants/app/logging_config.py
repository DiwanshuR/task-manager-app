import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


log_file = Path(__file__).resolve().parent.parent / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[
        RotatingFileHandler(
            log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding="utf-8",
        )
    ],
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict