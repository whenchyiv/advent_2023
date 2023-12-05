from input import input
from loguru import logger
import re


inputs: list[str] = input.split("\n")

numbers: list[str] = [
    re.findall(r"\d", i) for i in inputs
]
calibration_values: list[int] = [
    int(f"{c[0]}{c[-1]}") if len(c) > 1 else int(f"{c[0]}{c[0]}") for c in numbers
]

logger.info(f"\n❄️ Calibration value: {sum(calibration_values)} ❄️")
