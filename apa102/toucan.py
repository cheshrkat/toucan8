#!/usr/bin/env python3
import toucan_helpers as toucan
import subprocess

external_scripts = [
  "./toucan-helloworld.py",
  "./toucan-red.py",
  "./toucan-orange.py",
  "./toucan-green.py",
  "./toucan-fade.py",
  "./toucan-bluepulse.py",
  "./toucan-brightfade.py"
]

try:

    for x in external_scripts:
      print(f"----------------------------------------------")
      print(f"Running {x}")
      p = subprocess.Popen(f"python3 {x}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      if (p.stdout):
        subprocess_output=p.stdout
      if (p.stderr):
        subprocess_output=p.stderr
      for line in subprocess_output.readlines():
        print(line.decode("utf-8"))
      retval = p.wait()
      print(f"Done running {x}")

    lights = toucan.setup()
    toucan.lightsOut(lights)

except Exception as e:
    print(e)

finally:
    toucan.gpioClean()


