#!/usr/bin/env python3
"""news-image-01 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: an editorial summary of
world news on 13 November 2026. A globe centred on Europe, the Middle East
and Asia is ringed by five vignettes of the day's biggest stories: a swarm
of drones over a map (Ukraine's ~1,200-drone strike on Russia), an airplane
parked beneath a control tower (the FAA's nationwide ground stop after a
communications failure), a computer chip beside a falling chart (Nvidia
CEO Jensen Huang's exit; shares briefly down 14%), an oil tanker in a
strait with smoke on the horizon (tankers hit in the Strait of Hormuz),
and warships at sea (China's large unannounced Pacific drills near
Taiwan). The program copies it to /output/entry.png, byte for byte, so
the judge sees exactly these bytes.

The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024
pixels; this file is a 1024x1024 JPEG of 155,884 bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUTPUT_DIR, "entry.png"))
