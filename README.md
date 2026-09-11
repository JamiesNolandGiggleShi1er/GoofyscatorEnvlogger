<!-- made by jamie @_jmi. OR @jmialt_ (JOIN OMNI DBF (https://dsc.gg/odbf)) -->
# goofyscator v10 deobf

yo this rips goofyscator v10 (spectra) stuff yk just runs the obf file under lune with a fake roblox env and dumps what it prints. no key or whatever.

## what u need
- python 3.8+
- lune - https://github.com/lune-org/lune - just have `lune` in PATH or set `GOOFYSCATOR_LUNE` to where ur binary is

## how to run
```bash
python src/decompiler.py <input.lua> [output.lua] [timeout]
# ex
python src/decompiler.py input.lua
# gives u input_decompiled.lua + .trace.txt next to it
```

## what it does rn
- kills `require`
- locks `getfenv` so that dumb `viT` check (`c[1]==1 and c[2]==De_`) dont trip and throw `runtime error`
- fakes `bit32`/`bit` (pure math no bitwise needed), `task`, `Random`, `wait`/`spawn`/`delay`, `hookfunction`, `newcclosure`, `identifyexecutor` etc
- patches out the `viT` guard `if type(c) ~= "table" or c[1] ~= 1 or c[2] ~= De_ then error("runtime error",0) end` before running
- grabs `print` output and rebuilds a clean `--!nocheck` file

## code api if u want to import it
```python
from src.decompiler import dc
r = dc("input.lua", "out.lua", 30)
print(r["output"], r["behaviors"], r["strings"])
```
`dc` is main, `ds` makes the patched src, `rl` runs it under lune, `po` parses prints, `es` grabs strings, `go` makes the final file.

## license
MIT - see LICENSE - made by jamie @_jmi. OR @jmialt_ (JOIN OMNI DBF (https://dsc.gg/odbf))

GIVE FRICKING CREDITS
