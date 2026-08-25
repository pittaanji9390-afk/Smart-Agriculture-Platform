"""
Structured Logging Framework - AgriSphere OS
Configures standard library logging with structured JSON and colored console formatters.
"""

import logging
import sys
import json
from datetime import datetime, timezone

class StructuredJsonFormatter(logging.Formatter):
    """Formats log records as JSON objects for centralized log aggregators (Elasticsearch / Datadog / Loki)."""
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "line_no": record.lineno,
            "function": record.funcName
        }
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        if hasattr(record, "extra_fields"):
            log_entry.update(record.extra_fields)
        return json.dumps(log_entry)

def setup_logging(json_format: bool = False, log_level: str = "INFO") -> logging.Logger:
    """Initializes and returns the root application logger."""
    logger = logging.getLogger("agrisphere")
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(level)

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    if json_format:
        handler.setFormatter(StructuredJsonFormatter())
    else:
        handler.setFormatter(logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s:%(module)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        ))

    logger.addHandler(handler)
    logger.propagate = False
    return logger

logger = setup_logging()
