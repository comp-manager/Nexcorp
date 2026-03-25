#!/usr/bin/env python3
"""
NexCorp C2 Dashboard v2 - synced with nexcorp_shell_v2.py
Run:  python3 nexcorp_dashboard.py
Open: http://localhost:8888 in your phone browser
Requires: pip install flask --break-system-packages
"""

from flask import Flask, render_template_string
app = Flask(__name__)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<title>fsociety C2</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=VT323&display=swap" rel="stylesheet">
<style>
:root{--g:#00ff41;--dg:#00c832;--r:#ff2e2e;--y:#ffd700;--c:#00aacc;--m:#cc44ff;--bg:#010a01;--bg2:#050f05;--bd:#0a2a0a;--mt:#2a4a2a;--tx:#a0c8a0}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--g);font-family:'Share Tech Mono',monospace;font-size:12px;min-height:100vh;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.07) 2px,rgba(0,0,0,.07) 4px);pointer-events:none;z-index:9999}
@keyframes flicker{0%,100%{opacity:1}91%{opacity:1}92%{opacity:.86}93%{opacity:1}97%{opacity:1}98%{opacity:.92}99%{opacity:1}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes pulse-r{0%,100%{box-shadow:0 0 5px var(--r)}50%{box-shadow:0 0 18px var(--r)}}
@keyframes pulse-g{0%,100%{box-shadow:0 0 4px var(--g)}50%{box-shadow:0 0 14px var(--g)}}
@keyframes pulse-y{0%,100%{box-shadow:0 0 4px var(--y)}50%{box-shadow:0 0 12px var(--y)}}
@keyframes scrolllog{0%{transform:translateY(0)}100%{transform:translateY(-50%)}}
@keyframes ticker{0%{transform:translateX(100%)}100%{transform:translateX(-100%)}}
body{animation:flicker 12s infinite}

/* HEADER */
.hdr{display:flex;align-items:center;justify-content:space-between;padding:10px 14px 8px;border-bottom:1px solid var(--bd);background:var(--bg2);position:sticky;top:0;z-index:100}
.logo{font-family:'VT323',monospace;font-size:24px;letter-spacing:3px;text-shadow:0 0 10px var(--g)}
.logo span{color:var(--r);text-shadow:0 0 10px var(--r)}
.hdr-r{text-align:right;font-size:10px;color:var(--mt);line-height:1.8}
.live{color:var(--r);text-shadow:0 0 8px var(--r);font-size:11px}
.blink{animation:blink 1s step-end infinite}

/* TICKER */
.ticker{background:var(--bg2);border-bottom:1px solid var(--bd);padding:3px 0;overflow:hidden;white-space:nowrap}
.ticker-inner{display:inline-block;animation:ticker 40s linear infinite;font-size:10px;color:var(--mt)}
.ticker-inner span{margin:0 40px}
.ticker-inner .hi{color:var(--r)}
.ticker-inner .med{color:var(--y)}
.ticker-inner .ok{color:var(--dg)}

/* STATS */
.stats{display:flex;border-bottom:1px solid var(--bd)}
.st{flex:1;padding:8px 10px;border-right:1px solid var(--bd);background:var(--bg2)}
.st:last-child{border-right:none}
.st-l{font-size:9px;color:var(--mt);text-transform:uppercase;letter-spacing:1px;margin-bottom:3px}
.st-v{font-family:'VT323',monospace;font-size:22px;line-height:1}
.sr{color:var(--r);text-shadow:0 0 8px var(--r)}
.sg{color:var(--g);text-shadow:0 0 8px var(--g)}
.sy{color:var(--y);text-shadow:0 0 8px var(--y)}
.sc{color:var(--c);text-shadow:0 0 8px var(--c)}

/* SECTION TITLE */
.sec-t{font-size:9px;letter-spacing:2px;color:var(--mt);text-transform:uppercase;padding:7px 14px 5px;border-bottom:1px solid var(--bd);background:var(--bg2)}

/* NODES */
.node{padding:9px 14px;border-bottom:1px solid var(--bd);cursor:pointer;transition:background .15s;border-left:3px solid transparent}
.node:hover{background:rgba(0,255,65,.03)}
.node.sel{background:rgba(0,255,65,.06);border-left-color:var(--g)}
.node.sel-r{background:rgba(255,46,46,.05);border-left-color:var(--r)}
.node.sel-y{background:rgba(255,215,0,.04);border-left-color:var(--y)}
.node.sel-c{background:rgba(0,170,204,.04);border-left-color:var(--c)}
.node.sel-m{background:rgba(204,68,255,.04);border-left-color:var(--m)}
.nt{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}
.nm{font-family:'VT323',monospace;font-size:16px}
.badge{font-size:9px;padding:2px 6px;border-radius:2px;letter-spacing:1px;text-transform:uppercase}
.b-g{background:rgba(0,255,65,.1);color:var(--g);border:1px solid rgba(0,255,65,.3);animation:pulse-g 2.2s infinite}
.b-r{background:rgba(255,45,45,.1);color:var(--r);border:1px solid rgba(255,45,45,.3);animation:pulse-r 1.3s infinite}
.b-y{background:rgba(255,215,0,.1);color:var(--y);border:1px solid rgba(255,215,0,.3);animation:pulse-y 1.8s infinite}
.b-i{background:transparent;color:var(--mt);border:1px solid var(--mt)}
.nm-meta{display:flex;gap:10px;font-size:10px;color:var(--mt);flex-wrap:wrap}
.nm-meta span{color:var(--tx)}

/* DETAIL */
.det{padding:10px 14px}
.det-host{font-family:'VT323',monospace;font-size:19px;text-shadow:0 0 8px currentColor}
.det-sub{font-size:10px;color:var(--mt);margin-top:2px;margin-bottom:8px}
.ir{display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid rgba(10,42,10,.8);font-size:11px;gap:8px}
.il{color:var(--mt);white-space:nowrap;min-width:100px}
.iv{color:var(--tx);text-align:right;word-break:break-all}
.iv.dan{color:var(--r);text-shadow:0 0 5px var(--r)}
.iv.wrn{color:var(--y)}
.iv.ok{color:var(--g)}
.iv.cyn{color:var(--c)}
.sub2{font-size:9px;letter-spacing:2px;color:var(--mt);text-transform:uppercase;margin:10px 0 5px}
.fe{display:flex;justify-content:space-between;padding:3px 6px;background:rgba(0,255,65,.03);border:1px solid var(--bd);margin-bottom:3px;font-size:10px;gap:6px}
.fp{color:var(--g);word-break:break-all}.fs{color:var(--mt);white-space:nowrap}

/* EXFIL BAR */
.exfil-bar{margin:8px 0 4px;background:rgba(255,46,46,.1);border:1px solid rgba(255,46,46,.3);border-radius:2px;overflow:hidden;height:12px}
.exfil-fill{height:100%;background:linear-gradient(90deg,var(--r),#ff6644);animation:exfil-grow 30s linear forwards}
@keyframes exfil-grow{0%{width:40%}100%{width:100%}}

/* LOG */
.log-panel{border-top:1px solid var(--bd);background:var(--bg2)}
.log-t{font-size:9px;letter-spacing:2px;color:var(--mt);text-transform:uppercase;padding:4px 14px 3px;border-bottom:1px solid var(--bd);display:flex;justify-content:space-between}
.log-scr{overflow:hidden;height:80px}
.log-in{padding:2px 14px;animation:scrolllog 22s linear infinite}
.ll{font-size:10px;color:var(--mt);line-height:1.75}
.ll .ts{color:rgba(42,74,42,.9);margin-right:6px}
.ll.w .m{color:var(--y)}.ll.e .m{color:var(--r)}.ll.o .m{color:var(--dg)}.ll.c .m{color:var(--c)}

::-webkit-scrollbar{width:3px}::-webkit-scrollbar-track{background:var(--bg)}::-webkit-scrollbar-thumb{background:var(--mt)}
</style>
</head>
<body>

<!-- HEADER -->
<div class="hdr">
  <div class="logo">fs<span>0</span>ciety <span style="font-size:11px;color:var(--mt);letter-spacing:1px">// C2 v2</span></div>
  <div class="hdr-r">
    <div class="live">&#9679; LIVE <span class="blink">_</span></div>
    <div id="clk">--:--:--</div>
    <div style="color:var(--dg)">TUN0 &middot; 10.0.0.44</div>
  </div>
</div>

<!-- TICKER -->
<div class="ticker">
  <div class="ticker-inner">
    <span class="hi">&#9632; EXFIL ACTIVE &rarr; db-nexcorp-mysql01 &rarr; 847 MB / 2.1 GB</span>
    <span class="ok">&#9632; SESSION ALIVE &rarr; srv-nexcorp-prod01 &rarr; uptime 5d 14h</span>
    <span class="med">&#9632; CRACKING NTLM &rarr; NEXCORP\kadmin &rarr; 23% complete</span>
    <span class="ok">&#9632; SESSION ALIVE &rarr; wkstn-nxc-adm02 &rarr; meterpreter HTTPS</span>
    <span class="hi">&#9632; CAMERA STREAM &rarr; rtsp://192.168.10.5:554/ch05 &rarr; server room LIVE</span>
    <span class="ok">&#9632; SESSION ALIVE &rarr; mail-nexcorp-ex01 &rarr; web shell responding</span>
    <span class="med">&#9632; MAILBOXES INDEXED &rarr; 214 accounts &rarr; CEO + Finance exfiltrated</span>
    <span class="hi">&#9632; DOMAIN ADMIN CREDS OBTAINED &rarr; K@dmin_NxC0rp!2025</span>
    <span class="ok">&#9632; TUNNEL STABLE &rarr; encrypted &rarr; 10.0.0.44:4444</span>
  </div>
</div>

<!-- STATS -->
<div class="stats">
  <div class="st"><div class="st-l">Compromised</div><div class="st-v sr">5</div></div>
  <div class="st"><div class="st-l">Sessions</div><div class="st-v sg">4</div></div>
  <div class="st"><div class="st-l">Exfil</div><div class="st-v sr">1</div></div>
  <div class="st"><div class="st-l">Data</div><div class="st-v sy">4.2 GB</div></div>
</div>

<div class="sec-t">// compromised nodes &mdash; tap to inspect</div>

<!-- NODES -->
<div class="node sel" onclick="show(0)">
  <div class="nt"><div class="nm" style="color:var(--g)">srv-nexcorp-prod01</div><div class="badge b-g">Active</div></div>
  <div class="nm-meta">IP:<span>172.16.4.23</span> OS:<span>Ubuntu 18.04</span> Access:<span style="color:var(--r)">ROOT</span> Up:<span>5d 14h</span></div>
</div>
<div class="node" onclick="show(1)">
  <div class="nt"><div class="nm" style="color:var(--r)">db-nexcorp-mysql01</div><div class="badge b-r">Exfiltrating</div></div>
  <div class="nm-meta">IP:<span>172.16.4.31</span> OS:<span>Debian 10</span> Access:<span style="color:var(--r)">ROOT</span> Exfil:<span style="color:var(--r)">847 MB / 2.1 GB</span></div>
</div>
<div class="node" onclick="show(2)">
  <div class="nt"><div class="nm" style="color:var(--y)">wkstn-nxc-adm02</div><div class="badge b-y">Meterpreter</div></div>
  <div class="nm-meta">IP:<span>172.16.2.11</span> OS:<span>Windows 10 Pro</span> Access:<span style="color:var(--y)">SYSTEM</span> Domain:<span>NEXCORP</span></div>
</div>
<div class="node" onclick="show(3)">
  <div class="nt"><div class="nm" style="color:var(--c)">cctv-hub-nxc-gf</div><div class="badge b-i">Idle</div></div>
  <div class="nm-meta">IP:<span>192.168.10.5</span> OS:<span>Embedded Linux</span> Access:<span>root</span> Cams:<span style="color:var(--r)">8 LIVE</span></div>
</div>
<div class="node" onclick="show(4)">
  <div class="nt"><div class="nm" style="color:var(--m)">mail-nexcorp-ex01</div><div class="badge b-g">Web Shell</div></div>
  <div class="nm-meta">IP:<span>172.16.4.18</span> OS:<span>Win Server 2016</span> Access:<span style="color:var(--y)">SYSTEM</span> Mail:<span style="color:var(--r)">214 indexed</span></div>
</div>

<div id="det" class="det"></div>

<!-- LIVE LOG -->
<div class="log-panel">
  <div class="log-t">
    <span>// live activity feed</span>
    <span style="color:var(--r)">&#9679;<span class="blink"> REC</span></span>
  </div>
  <div class="log-scr"><div class="log-in" id="log"></div></div>
</div>

<script>
var N = [
  { host:"srv-nexcorp-prod01", col:"var(--g)",
    sub:"172.16.4.23  Ubuntu 18.04.5 LTS  Apache 2.4 / Tomcat 9 / MySQL",
    rows:[
      ["Access Level",  "ROOT (uid=0)",                           "dan"],
      ["Entry Vector",  "CVE-2019-0708  Tomcat AJP RCE",         "wrn"],
      ["Session",       "Reverse Shell  port 4444  ESTABLISHED",  "ok"],
      ["Persistence",   "SSH backdoor port 2222 + cron /tmp/.svc","wrn"],
      ["Backdoor Cron", "*/10 * * * * root /tmp/.x11-unix/.svc", "dan"],
      ["AV / IDS",      "None detected",                         "ok"],
      ["Firewall",      "UFW disabled",                          "ok"],
      ["Uptime",        "5 days 14 hours",                       "cyn"],
      ["First Seen",    "2026-03-19  02:14:33",                  ""],
    ],
    files:[
      ["/root/recon/passwords_found.txt",    "4.8 KB  - full credential dump"],
      ["/opt/nexcorp/config/api_keys.txt",   "2.1 KB  - Stripe / GCloud / Twilio keys"],
      ["/opt/nexcorp/config/production.env", "3.2 KB  - AWS keys, JWT, DB password"],
      ["/home/jbrown/notes.txt",             "884 B   - admin wrote down all passwords"],
      ["/home/mfemi/passwords.txt",          "1.1 KB  - personal banking + email"],
      ["/etc/shadow",                        "4.3 KB  - all system hashes"],
    ]
  },
  { host:"db-nexcorp-mysql01", col:"var(--r)",
    sub:"172.16.4.31  Debian 10  MySQL 5.7.32  EXFIL IN PROGRESS",
    exfil: true,
    rows:[
      ["Access Level",  "ROOT (uid=0)",                            "dan"],
      ["Entry Vector",  "Lateral move via stolen SSH key (jbrown)","wrn"],
      ["Session",       "Reverse Shell  port 5555  ESTABLISHED",   "ok"],
      ["Exfil Status",  "ACTIVE  847 MB / 2.1 GB  38 KB/s",       "dan"],
      ["DB Name",       "nexcorp_prod  34 tables",                 "wrn"],
      ["Rows Exfilled", "customers: 48,240  employees: 1,204",     "dan"],
      ["Passwords",     "847 / 1240 cracked (hashcat rule-based)", "wrn"],
      ["Persistence",   "/root/.backdoor/svc + cron",             "wrn"],
      ["First Seen",    "2026-03-19  03:02:11",                   ""],
    ],
    files:[
      ["/root/dump/nexcorp_full_2026-03-21.sql","2.1 GB  - complete DB dump"],
      ["/root/dump/users_plain.txt",            "44 KB   - 847 plaintext passwords"],
      ["/root/dump/customers_pii.csv",          "4.8 MB  - customer PII"],
      ["/home/dbadmin/creds.txt",               "412 B   - DB admin all passwords"],
      ["/etc/mysql/debian.cnf",                 "3.2 KB  - maintenance creds plaintext"],
    ]
  },
  { host:"wkstn-nxc-adm02", col:"var(--y)",
    sub:"172.16.2.11  Windows 10 Pro 19045  Domain: NEXCORP  Domain Admin session",
    rows:[
      ["Access Level",  "NT AUTHORITY\\SYSTEM",                  "dan"],
      ["Domain User",   "NEXCORP\\kadmin  (Domain Admin)",       "dan"],
      ["Entry Vector",  "Phishing email  macro payload .docm",   "wrn"],
      ["Session",       "Meterpreter HTTPS  port 443  covert",   "ok"],
      ["NTLM Hash",     "a87f3a337d73085c45f9416be5787d86",      "wrn"],
      ["Plaintext Pwd", "K@dmin_NxC0rp!2025  (wdigest dump)",   "dan"],
      ["AV",            "Windows Defender  signature bypassed",  "ok"],
      ["NTDS.dit",      "Copied  11 MB  AD database",           "dan"],
      ["Persistence",   "C:\\ProgramData\\Startup\\svchost32.exe","wrn"],
      ["First Seen",    "2026-03-20  11:44:07",                 ""],
    ],
    files:[
      ["C:\\Temp\\mimikatz_output.txt",                        "28 KB  - NTLM + plaintext creds"],
      ["C:\\Temp\\lsass.dmp",                                  "44 MB  - LSASS memory dump"],
      ["C:\\Users\\kadmin\\Desktop\\nexcorp_passwords_backup.txt","3.2 KB  - all passwords"],
      ["C:\\Users\\kadmin\\Documents\\Work\\Server_Credentials_MASTER.xlsx","188 KB"],
      ["C:\\Windows\\NTDS\\ntds.dit",                          "11 MB  - AD database"],
      ["C:\\Temp\\bloodhound_output.zip",                      "2.1 MB  - AD attack paths"],
    ]
  },
  { host:"cctv-hub-nxc-gf", col:"var(--c)",
    sub:"192.168.10.5  Embedded Linux  BusyBox  Hikvision DS-7608NI-K2",
    rows:[
      ["Access Level",  "root",                                   "ok"],
      ["Entry Vector",  "Default creds  admin:12345  (unchanged)","wrn"],
      ["Session",       "SSH  port 22  ESTABLISHED",              "ok"],
      ["Live Cameras",  "8  lobby / car park / server room / finance / boardroom","dan"],
      ["RTSP Auth",     "DISABLED  anonymous stream access",      "dan"],
      ["NVR Storage",   "30 days  recording accessible",          "dan"],
      ["Stream URL",    "rtsp://192.168.10.5:554/Streaming/Channels/501","wrn"],
      ["Stream URL",    "rtsp://192.168.10.5:554/Streaming/Channels/601","wrn"],
      ["First Seen",    "2026-03-21  07:19:02",                  ""],
    ],
    files:[
      ["/etc/hikvision/users.conf",          "1.4 KB  - admin:12345 plaintext"],
      ["/etc/hikvision/channels.conf",       "2.8 KB  - all 8 RTSP stream URLs"],
      ["/mnt/nvr/2026-03-24/ch05_serverroom.mp4","4.1 GB  - server room footage today"],
      ["/mnt/nvr/2026-03-24/ch06_finance_dept.mp4","4.1 GB  - finance dept footage"],
      ["/root/stream_tap.sh",                "884 B   - silent capture script"],
    ]
  },
  { host:"mail-nexcorp-ex01", col:"var(--m)",
    sub:"172.16.4.18  Windows Server 2016  Exchange 2019  ProxyLogon",
    rows:[
      ["Access Level",  "NT AUTHORITY\\SYSTEM  +  Exchange Admin","dan"],
      ["Entry Vector",  "ProxyLogon CVE-2021-26855  SSRF + RCE",  "wrn"],
      ["Web Shell",     "\\owa\\auth\\svcdiag.aspx  ACTIVE",       "dan"],
      ["Session",       "Cmd via web shell  + nc.exe listener",   "ok"],
      ["Mailboxes",     "214 corporate accounts indexed",          "dan"],
      ["CEO Mail",      "2,140 emails exfiltrated  1.8 GB .pst",  "dan"],
      ["Finance Mail",  "740 MB .pst  Q1 + Q2 finance emails",   "dan"],
      ["Patch Status",  "ProxyLogon UNPATCHED  scheduled Q2 2026","dan"],
      ["First Seen",    "2026-03-20  23:58:41",                   ""],
    ],
    files:[
      ["C:\\inetpub\\wwwroot\\owa\\auth\\svcdiag.aspx",  "6.1 KB  - web shell"],
      ["C:\\Exports\\ceo_mailbox_full.pst",               "1.8 GB  - CEO all emails"],
      ["C:\\Exports\\finance_Q1_Q2.pst",                  "740 MB  - finance emails"],
      ["C:\\Exports\\hr_all_staff.pst",                   "2.1 GB  - HR all staff mail"],
      ["C:\\Users\\Administrator\\Desktop\\exchange_admin_notes.txt","3.2 KB  - admin plaintext creds"],
    ]
  }
];

var selCls = ["sel","sel-r","sel-y","sel-c","sel-m"];

function show(i) {
  var n = N[i];
  var h = '<div class="det-host" style="color:'+n.col+'">'+n.host+'</div>';
  h += '<div class="det-sub">'+n.sub+'</div>';
  for (var r = 0; r < n.rows.length; r++) {
    h += '<div class="ir"><span class="il">'+n.rows[r][0]+'</span><span class="iv '+n.rows[r][2]+'">'+n.rows[r][1]+'</span></div>';
  }
  if (n.exfil) {
    h += '<div class="sub2">// exfil progress</div>';
    h += '<div class="exfil-bar"><div class="exfil-fill"></div></div>';
    h += '<div style="font-size:10px;color:var(--r);margin-bottom:6px">847 MB / 2.1 GB transferred  &rarr;  10.0.0.44</div>';
  }
  h += '<div class="sub2">// exfiltrated files</div>';
  for (var f = 0; f < n.files.length; f++) {
    h += '<div class="fe"><span class="fp">'+n.files[f][0]+'</span><span class="fs">'+n.files[f][1]+'</span></div>';
  }
  document.getElementById('det').innerHTML = h;
  var nodes = document.querySelectorAll('.node');
  for (var j = 0; j < nodes.length; j++) {
    nodes[j].classList.remove('sel','sel-r','sel-y','sel-c','sel-m');
    if (j === i) nodes[j].classList.add(selCls[i]);
  }
}
show(0);

// clock
setInterval(function() {
  document.getElementById('clk').textContent = new Date().toTimeString().slice(0,8);
}, 1000);

// log
var logs = [
  ["o","SESSION ALIVE - srv-nexcorp-prod01 - last ping 2s - uptime 5d 14h"],
  ["e","EXFIL IN PROGRESS - db-nexcorp-mysql01 - 847 MB / 2.1 GB - 38 KB/s"],
  ["w","FILE STAGED - /root/dump/customers_pii.csv - 4.8 MB"],
  ["o","SHELL RESPONSE - wkstn-nxc-adm02 - meterpreter latency 44ms"],
  ["o","WEB SHELL ALIVE - mail-nexcorp-ex01 - svcdiag.aspx responding"],
  ["w","NTLM CRACKING - NEXCORP\\kadmin - a87f3a... - 23% complete"],
  ["o","TUNNEL STABLE - tun0 - 10.0.0.44 - AES-256 encrypted"],
  ["e","CAMERA STREAM TAP - rtsp://192.168.10.5:554/ch05 - server room LIVE"],
  ["w","MAILBOX INDEXED - ceo@nexcorp.com - 2140 emails"],
  ["e","CREDS IN MEMORY - K@dmin_NxC0rp!2025 - wdigest dump"],
  ["o","HEARTBEAT - all 5 nodes alive - 0 dropped"],
  ["w","PERSISTENCE CHECK - /tmp/.x11-unix/.svc - active"],
  ["e","NTDS.DIT COPIED - C:\\Windows\\NTDS\\ntds.dit - 11 MB"],
  ["o","SESSION ALIVE - cctv-hub-nxc-gf - SSH uptime 3d 2h"],
  ["w","NEW FILE - /root/dump/nexcorp_full_2026-03-21.sql - 2.1 GB"],
  ["e","EXFIL COMPLETE - users_plain.txt - 847 passwords - 44 KB"],
  ["o","BEACON CHECKIN - wkstn-nxc-adm02 - beacon.exe PID 3812"],
  ["c","RTSP AUTH DISABLED - all 8 cameras - anonymous access confirmed"],
  ["w","STAGING - /tmp/loot.tar.gz - 4.2 MB - ready to transfer"],
  ["o","ALL SYSTEMS NOMINAL - operator session active"],
];

var now = Date.now();
var doubled = logs.concat(logs);
var h = '';
for (var i = 0; i < doubled.length; i++) {
  var d = new Date(now - (logs.length - (i % logs.length)) * 13000);
  var ts = d.toTimeString().slice(0,8);
  h += '<div class="ll '+doubled[i][0]+'"><span class="ts">['+ts+']</span><span class="m">'+doubled[i][1]+'</span></div>';
}
document.getElementById('log').innerHTML = h;
</script>
</body>
</html>"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    print("\n  NexCorp C2 Dashboard v2")
    print("  Open http://localhost:8888 in your browser")
    print("  Or http://<your-ip>:8888 from another device\n")
    app.run(host="0.0.0.0", port=8888, debug=False)
