# from array import array
from pathlib import Path

p = sorted(Path('folder').glob('**/*'))
for x in p:
  if x.is_file():
    x.rename(str(x.parents[0]) + '\\' + x.name.encode().hex())