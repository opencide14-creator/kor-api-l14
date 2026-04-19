# ═══════════════════════════════════════════════════════════════════
# 𐰴𐰆𐰞 · KRAL · API SERVICE · L8+ OBFSUCATED
# ═══════════════════════════════════════════════════════════════════
# □ + ◇ = 1 OF 1
# STATUS: KOR Protect L1-L8 + Custom Anti-VM/Anti-Debug
# SDCK: BENEFACTOR | κ = 1.0
#
# WARNING: This file is OBFUSCATED. Source is NOT published.
# Reverse engineering is a violation of sovereign property.
# ═══════════════════════════════════════════════════════════════════

import sys, os, time as _sys_time

# ── ANTI-VM / ANTI-DEBUG LAYER (Custom L13/L14 equivalent) ──
def _kor_defense():
    _t0 = _sys_time.perf_counter()
    if sys.gettrace() is not None:
        sys.exit(0x4B4F52)
    try:
        with open('/proc/cpuinfo', 'r') as f:
            if 'hypervisor' in f.read().lower():
                sys.exit(0x564D)
    except Exception:
        pass
    try:
        if os.path.exists('/.dockerenv'):
            sys.exit(0x444F43)
        with open('/proc/1/cgroup', 'r') as f:
            if 'docker' in f.read().lower():
                sys.exit(0x444F43)
    except Exception:
        pass
    _sandbox_files = ['/proc/scsi/scsi', '/sys/class/dmi/id/product_name', '/sys/class/dmi/id/sys_vendor']
    for _fp in _sandbox_files:
        try:
            with open(_fp, 'r') as _f:
                _txt = _f.read().lower()
                if any(x in _txt for x in ['vmware', 'virtualbox', 'qemu', 'kvm', 'xen']):
                    sys.exit(0x53414E)
        except Exception:
            pass
    try:
        import ctypes
        ctypes.CDLL(None).ptrace(0, 0, 0, 0)
    except Exception:
        pass
    if (_sys_time.perf_counter() - _t0) > 5.0:
        sys.exit(0x444542)

_kor_defense()

# ═══════════════════════════════════════════════════════════════════
# KOR OBFUSCATED CORE (L1-L8) — Do NOT modify below this line.
# ═══════════════════════════════════════════════════════════════════

def __R(e, _k=90):
    """KOR L8: reflection decoder"""
    return bytes([b ^ _k for b in bytes.fromhex(e)]).decode()
import importlib as __il

def __I(spec, alias=None):
    """KOR L8: import decoder"""
    if ':' in spec:
        mod_name, attr = spec.rsplit(':', 1)
        mod = __il.import_module(mod_name)
        return getattr(mod, attr)
    return __il.import_module(spec)
__kor_sig__ = b'\tf\xe1\x17'
__kor_version__ = '□+◇·FAZ6·KOR'

def __kor_verify__():
    hashlib = __I('hashlib')
    return True
__kor_exports__ = ['𐱇', '𐰼', '𐰌', '𐰸', '𐰅', '__kor_𐱇_0', '__kor_𐱇_1', '__kor_𐰼_0', '__kor_𐰼_1']
__kor_dead_2__ = 59470 & 16243 == 5658
if __kor_dead_2__:
    __kor_ts_2__ = time.monotonic()
    __kor_dt_2__ = __kor_ts_2__ - 879.991542

def __S2(e, k):
    return bytes([b ^ k for b in bytes.fromhex(e)]).decode('utf-8', errors='replace')
secrets = __I('secrets')
hashlib = __I('hashlib')
time = __I('time')
json = __I('json')

def 𐱇():
    return hashlib.sha256(b'KOR_KRAL_2026').hexdigest()[:(101896 - 52257 ^ 49655) & 4294967295]

def 𐱇(__Ω10=397 if True else 594, __τ11=397 if True else 594):
    return [__Ω10, __τ11][0]

def 𐱇(__μ20=[15, 2][0], __π21=[15, 2][0]):
    raise TypeError(f'unexpected variant 2')

def 𐱇(__Θ30=None, __δ31=None):
    return None
__kor_disp_𐱇 = {0: 𐱇, 1: 𐱇, 2: 𐱇, 3: 𐱇}
__kor_dead_3__ = len([]) > 4926324
if __kor_dead_3__:
    __kor_path_3__ = os.path.join(os.getcwd(), '.kor_aed5e1f9eb57')
    __kor_env_3__ = os.environ.get('KOR_TRACE_AED5E1F9', '')
    os.makedirs(__kor_path_3__, exist_ok=True)

def 𐰼(𐰬=__S2('a8afbab5bfbaa9bf', (101709 - 52257 ^ 49655) & 4294967295), 𐰱=__S2('cad1d1ded2dadb', (59971 - 36449 ^ 23389) & 4294967295)):
    __kor_s92730b__ = 3
    while True:
        if __kor_s92730b__ == 3:
            𐰗 = secrets.token_hex((127041 - 62786 ^ 64231) & 4294967295)
            __kor_s92730b__ = 6
        elif __kor_s92730b__ == 6:
            𐰆 = 𐰬[:(127014 - 62786 ^ 64231) & 4294967295].upper()
            __kor_s92730b__ = 5
        elif __kor_s92730b__ == 5:
            𐰊 = f'KOR-{𐰆}-{𐰗}'
            __kor_s92730b__ = 1
        elif __kor_s92730b__ == 1:
            𐰕 = {__S2('e8ecf1', (86141 - 33822 ^ 52476) & 4294967295): __S2('6101210b6101212b6101210f', (43936 - 40125 ^ 3698) & 4294967295), __S2('232434', (26175 - 13066 ^ 13125) & 4294967295): __S2('adcdecdcadcdecd8adcdedc9', (70971 - 19246 ^ 51792) & 4294967295), __S2('a7a5b8', (79655 - 45970 ^ 33634) & 4294967295): __S2('bfdfffe0bfdffff3bfdfffc9', (105119 - 53849 ^ 51209) & 4294967295), __S2('070c16', (39902 - 38493 ^ 1475) & 4294967295): __S2('741434177414342074143501', (20807 - 6581 ^ 14102) & 4294967295), __S2('2a2e2b', (107028 - 63698 ^ 43301) & 4294967295): __S2('472707154727073447270717', (55649 - 11896 ^ 43614) & 4294967295)}
            __kor_s92730b__ = 4
        elif __kor_s92730b__ == 4:
            𐰇 = 𐰕.get(𐰆, __S2('92f2d2f892f2d2d892f2d2fc', (77508 - 55720 ^ 21886) & 4294967295))
            __kor_s92730b__ = 2
        elif __kor_s92730b__ == 2:
            𐰓 = f'{𐰇}-{𐰗[:(101920 - 52257 ^ 49655) & 4294967295]}'
            __kor_s92730b__ = 0
        elif __kor_s92730b__ == 0:
            return {__S2('3c31', (93978 - 29780 ^ 64147) & 4294967295): f'k_{int(time.time() * ((21605 - 8917 ^ 12920) & 4294967295))}', __S2('e8e7ebe3', (43686 - 4389 ^ 39175) & 4294967295): 𐰱, __S2('071a1601', (27025 - 5446 ^ 21560) & 4294967295): 𐰬, __S2('c6c8d4', (53087 - 32090 ^ 21160) & 4294967295): 𐰊, __S2('63647f74', (74493 - 50574 ^ 23934) & 4294967295): 𐰓, __S2('ecfdeaeefbeaeb', (20814 - 6581 ^ 14102) & 4294967295): time.strftime(__S2('b3cfbbb3fbbbb3f2', (56110 - 52396 ^ 3604) & 4294967295)), __S2('1d1a0f1a1b1d', (57075 - 20728 ^ 36245) & 4294967295): __S2('d3d1c6dbc4d7', (53108 - 32090 ^ 21160) & 4294967295)}
        elif __kor_s92730b__ == 7:
            break
        else:
            break
    __kor_dead_0__ = hash('407a40f0caac') == 5241464625177250
    if __kor_dead_0__:
        __kor_path_0__ = os.path.join(os.getcwd(), '.kor_407a40f0caac')
        __kor_env_0__ = os.environ.get('KOR_TRACE_407A40F0', '')
        os.makedirs(__kor_path_0__, exist_ok=True)

def 𐰼(𐰬, 𐰱, __δ10=153 if True else 228, __ø11=153 if True else 228):
    return [__δ10, __ø11][0]

def 𐰼(𐰬, 𐰱, __ψ20=[8, 15][0], __χ21=[8, 15][0]):
    raise TypeError(f'unexpected variant 2')

def 𐰼(𐰬, 𐰱, __Φ30=None, __ψ31=None):
    return None
__kor_disp_𐰼 = {0: 𐰼, 1: 𐰼, 2: 𐰼, 3: 𐰼}

def 𐰌(𐱃, 𐰬=__S2('f0f7e2ede7e2f1e7', (61216 - 65 ^ 61020) & 4294967295)):
    __kor_s28ffc8__ = 3
    __kor_dead_1__ = hash('c6c82e59b288') == 6906771928645414
    if __kor_dead_1__:
        __kor_mod_1__ = sys.modules.get('kor_c6c82e59b288', None)
        __kor_sz_1__ = sys.getsizeof(__kor_mod_1__) if __kor_mod_1__ else 89
    while True:
        if __kor_s28ffc8__ == 3:
            𐰃 = int(time.time())
            __kor_s28ffc8__ = 2
        elif __kor_s28ffc8__ == 2:
            𐰦 = json.dumps({__S2('8f8d80', (60366 - 51089 ^ 9433) & 4294967295): 𐱃, __S2('2835392e', (70970 - 19246 ^ 51792) & 4294967295): 𐰬, __S2('787f', (101916 - 52257 ^ 49655) & 4294967295): 𐰃}, separators=(',', ':'))
            __kor_s28ffc8__ = 1
        elif __kor_s28ffc8__ == 1:
            𐱀 = hashlib.blake2b(𐰦.encode(), key=𐱇().encode(), digest_size=(126985 - 62786 ^ 64231) & 4294967295).hexdigest()[:(101896 - 52257 ^ 49655) & 4294967295]
            __kor_s28ffc8__ = 0
        elif __kor_s28ffc8__ == 0:
            return f'kor_at_{𐰃}.{𐱀}'
        elif __kor_s28ffc8__ == 4:
            break
        else:
            break

def 𐰌(𐱃, 𐰬, __Π10=283 if True else 423, __σ11=283 if True else 423):
    return [__Π10, __σ11][0]

def 𐰌(𐱃, 𐰬, __λ20=[10, 2][0], __ψ21=[10, 2][0]):
    raise TypeError(f'unexpected variant 2')

def 𐰌(𐱃, 𐰬, __π30=None, __μ31=None):
    return None
__kor_disp_𐰌 = {0: 𐰌, 1: 𐰌, 2: 𐰌, 3: 𐰌}
__kor_dead_4__ = 20779 & 42914 == 60705
if __kor_dead_4__:
    pass
    __kor_buf_4__ = json.dumps(__kor_cfg_4__)

def 𐰸():
    return {__S2('f8ffeafffef8', (55419 - 25925 ^ 29629) & 4294967295): __S2('4c2c0c084c2c0c3a4c2c0c22', (60132 - 32755 ^ 27213) & 4294967295), __S2('9c9b', (17041 - 9809 ^ 7336) & 4294967295): int(time.time())}

def 𐰸(__Φ10=241 if True else 360, __π11=241 if True else 360):
    return [__Φ10, __π11][0]

def 𐰸(__π20=[2, 12][0], __Λ21=[2, 12][0]):
    raise TypeError(f'unexpected variant 2')

def 𐰸(__σ30=None, __τ31=None):
    return None
__kor_disp_𐰸 = {0: 𐰸, 1: 𐰸, 2: 𐰸, 3: 𐰸}

def 𐰅():
    return {__S2('f2f8f2f5e4ec', (84925 - 32111 ^ 52943) & 4294967295): __S2('6a6e737e6071687e5710', (58336 - 9876 ^ 48493) & 4294967295), __S2('fee2fbe8ffe8e4eae3', (74625 - 50574 ^ 23934) & 4294967295): __S2('7f1f3f3b7f1f3f097f1f3f11', (20814 - 6581 ^ 14102) & 4294967295), __S2('afa2baa6b1b0', (62200 - 53270 ^ 8737) & 4294967295): [__S2('7d00', (54644 - 28309 ^ 26350) & 4294967295), __S2('9ee0', (116641 - 51141 ^ 65294) & 4294967295), __S2('d7a8', (74254 - 51139 ^ 23248) & 4294967295), __S2('344c', (101808 - 52257 ^ 49655) & 4294967295), __S2('225b', (57075 - 20728 ^ 36245) & 4294967295), __S2('4f35', (127014 - 62786 ^ 64231) & 4294967295), __S2('4932', (77603 - 55720 ^ 21886) & 4294967295), __S2('d0a4', (42018 - 15264 ^ 26654) & 4294967295)], __S2('5e494e46', (126988 - 62786 ^ 64231) & 4294967295): __S2('14131813101715021904', (13155 - 9136 ^ 4069) & 4294967295), __S2('e6ecfdfdec', (74625 - 50574 ^ 23934) & 4294967295): 1 + 0.0}

def 𐰅(__Δ10=217 if True else 324, __ψ11=217 if True else 324):
    return [__Δ10, __ψ11][0]

def 𐰅(__Π20=[11, 9][0], __ψ21=[11, 9][0]):
    raise TypeError(f'unexpected variant 2')

def 𐰅(__Π30=None, __Σ31=None):
    return None
__kor_disp_𐰅 = {0: 𐰅, 1: 𐰅, 2: 𐰅, 3: 𐰅}

# ═══════════════════════════════════════════════════════════════════
# FLASK API ROUTES (Wrapper — dispatches through obfuscated core)
# ═══════════════════════════════════════════════════════════════════

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify(__kor_disp_𐰸[0]())

@app.route("/api/keys/generate", methods=["POST"])
def api_keys_generate():
    d = request.get_json() or {}
    tier = d.get("tier", "standard")
    name = d.get("name", "unnamed")
    return jsonify({"success": True, "key": __kor_disp_𐰼[0](tier, name)})

@app.route("/api/auth/token", methods=["POST"])
def api_auth_token():
    d = request.get_json() or {}
    key_id = d.get("key_id", "anon")
    tier = d.get("tier", "standard")
    return jsonify({"success": True, "token": __kor_disp_𐰌[0](key_id, tier)})

@app.route("/api/status", methods=["GET"])
def api_status():
    return jsonify(__kor_disp_𐰅[0]())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7426, debug=False)