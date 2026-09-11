# -- made by jamie @_jmi. OR @jmialt_ (JOIN OMNI DBF (https://dsc.gg/odbf))
import os, re, sys, subprocess, shutil, tempfile, datetime
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(H)
L = os.environ.get("GOOFYSCATOR_LUNE") or os.path.join(R, "tools", "lune")
if not os.path.isfile(L):
    L = shutil.which("lune") or "lune"
J = r"""
require = function() error("require is disabled", 0) end
"""
M = J + r"""
local _r = getfenv
local _e = _r()
getfenv = function(x) return _e end
local function _x(a,b)
    local r,q=0,1
    a=math.floor(a or 0)%4294967296
    b=math.floor(b or 0)%4294967296
    for i=1,32 do
        if a%2~=b%2 then r=r+q end
        a=math.floor(a/2)
        b=math.floor(b/2)
        q=q*2
    end
    return r
end
local function _a(a,b)
    local r,q=0,1
    a=math.floor(a or 0)%4294967296
    b=math.floor(b or 0)%4294967296
    for i=1,32 do
        if a%2==1 and b%2==1 then r=r+q end
        a=math.floor(a/2)
        b=math.floor(b/2)
        q=q*2
    end
    return r
end
local function _o(a,b)
    local r,q=0,1
    a=math.floor(a or 0)%4294967296
    b=math.floor(b or 0)%4294967296
    for i=1,32 do
        if a%2==1 or b%2==1 then r=r+q end
        a=math.floor(a/2)
        b=math.floor(b/2)
        q=q*2
    end
    return r
end
bit32={band=_a,bor=_o,bxor=_x,bnot=function(a) return 4294967295-(math.floor(a)%4294967296) end,lshift=function(a,n) if n<=0 then return math.floor(a)%4294967296 end if n>=32 then return 0 end return (math.floor(a)*math.pow(2,n))%4294967296 end,rshift=function(a,n) if n<=0 then return math.floor(a)%4294967296 end if n>=32 then return 0 end return math.floor((math.floor(a)%4294967296)/math.pow(2,n)) end,arshift=function(a,n) if n<=0 then return math.floor(a)%4294967296 end if n>=32 then return 0 end return math.floor((math.floor(a)%4294967296)/math.pow(2,n)) end,btest=function(a,b) return _a(a,b)~=0 end}
bit=bit32
local _s=select
select=function(i,...) if i==nil then return 0 end if i=="#" then return _s("#",...) end if type(i)~="number" then i=1 end return _s(i,...) end
task=setmetatable({wait=function() return 0,0 end,spawn=function(f,...) if type(f)=="function" then pcall(f,...) end end,delay=function(t,f,...) if type(f)=="function" then pcall(f,...) end end,defer=function(f,...) if type(f)=="function" then pcall(f,...) end end,cancel=function(t) end,create=function(f) return {cancel=function() end} end,clock=function() return os.clock() end},{__index=function(t,k) return function() return 0 end end})
Random=setmetatable({}, {__call=function(s,x) return setmetatable({NextNumber=function() return 0 end,NextInteger=function(a,b) return a or 0 end,NextUnit=function() return 0 end},{}) end})
wait=function(t) return 0,0 end
spawn=function(f,...) if type(f)=="function" then pcall(f,...) end end
delay=function(t,f,...) if type(f)=="function" then pcall(f,...) end end
tick=function() return os.clock() end
warn=function(...) end
setclipboard=function(...) end
request=function(...) return {} end
http_request=function(...) return {} end
hookfunction=function(...) return function() end end
newcclosure=function(f) return f end
getgenv=function() return _e end
getrenv=function() return _e end
identifyexecutor=function() return "goofyscator-trace","v1" end
getexecutorname=function() return "goofyscator-trace" end
collectgarbage=function() return 0 end
syn=setmetatable({}, {__index=function() return function() end end})
getrawmetatable=function(t) return getmetatable(t) end
setrawmetatable=setmetatable
"""
def ds(s):
    p=re.sub(r'if type\((\w+)\) ~= "table" or \1\[1\] ~= 1 or \1\[2\] ~= (\w+) then error\("runtime error",0\);end;', '', s)
    return M + "\n" + p, None
def rl(p,t=30):
    with open(p,"r",encoding="utf-8",errors="replace") as f:
        s=f.read()
    c,_=ds(s)
    if not c:
        return "","",-1
    with tempfile.NamedTemporaryFile(mode="w",suffix=".luau",delete=False,encoding="utf-8") as tf:
        tf.write(c)
        h=tf.name
    try:
        r=subprocess.run([L,"run",h],capture_output=True,text=True,timeout=t)
        return r.stdout, r.stderr, r.returncode
    except subprocess.TimeoutExpired:
        return "","Timeout",-1
    except Exception as e:
        return "",str(e),-1
    finally:
        try: os.unlink(h)
        except: pass
def po(s):
    b=[]
    for x in (s or "").split("\n"):
        if x.strip() and not x.startswith("Warning") and not x.startswith("error"):
            b.append(x.strip())
    return b
def es(s):
    q=set()
    for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', s):
        x=m.group(1)
        try: x=x.encode().decode('unicode_escape')
        except: pass
        if 1 < len(x) < 500:
            q.add(x)
    return sorted(q, key=lambda x: (-len(x), x))
def go(b,q,p,s,e):
    o=[]
    o.append("-- made by jamie @_jmi. OR @jmialt_ (JOIN OMNI DBF (https://dsc.gg/odbf))")
    o.append("-- v10")
    o.append("-- src: " + os.path.basename(p))
    o.append("-- ts: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    o.append("")
    o.append("--!nocheck")
    o.append("")
    o.append("-- lines: " + str(len(b)))
    o.append("-- strs: " + str(len(q)))
    if e:
        o.append("-- note: " + e[:200].replace("\n"," "))
    o.append("")
    if b:
        o.append("-- out:")
        for x in b:
            o.append("-- " + x)
        o.append("")
    o.append("-- src:")
    o.append("")
    if b:
        for x in b:
            o.append('print("' + x.replace('"','\\"') + '")')
    else:
        o.append("-- empty")
    o.append("")
    return "\n".join(o)
def dc(p,o=None,t=30):
    if o is None:
        r,e=os.path.splitext(p)
        o=r+"_decompiled.lua"
    with open(p,"r",encoding="utf-8",errors="replace") as f:
        s=f.read()
    d,e,c=rl(p,t)
    b=po(d)
    q=es(s)
    x=go(b,q,p,d,e)
    with open(o,"w",encoding="utf-8") as f:
        f.write(x)
    u=o+".trace.txt"
    with open(u,"w",encoding="utf-8") as f:
        f.write("=== STDOUT ===\n" + (d or ""))
        f.write("\n=== STDERR ===\n" + (e or ""))
    return {"output":o,"trace":u,"behaviors":len(b),"strings":len(q),"stdout":d[:500] if d else "","stderr":e[:500] if e else ""}
if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python3 decompiler.py <input.lua> [output.lua] [timeout]")
        sys.exit(1)
    r=dc(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None, int(sys.argv[3]) if len(sys.argv)>3 else 30)
    print("[*] output -> " + r["output"])
    print("[*] behaviors: " + str(r["behaviors"]))
    print("[*] strings: " + str(r["strings"]))
    if r["stdout"]: print("[*] stdout: " + r["stdout"][:200])
    if r["stderr"]: print("[*] stderr: " + r["stderr"][:200])
