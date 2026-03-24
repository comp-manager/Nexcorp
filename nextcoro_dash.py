#!/usr/bin/env python3
“””
NexCorp C2 Dashboard — Flask visual companion
Run: python3 nexcorp_dashboard.py
Open: http://localhost:8888 in your phone browser
“””

from flask import Flask, render_template_string
app = Flask(**name**)

HTML = “””<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<title>fsociety · C2</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=VT323&display=swap" rel="stylesheet">
<style>
:root{--g:#00ff41;--dg:#00c832;--r:#ff2e2e;--y:#ffd700;--bg:#010a01;--bg2:#050f05;--bd:#0a2a0a;--mt:#2a4a2a;--tx:#a0c8a0}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--g);font-family:'Share Tech Mono',monospace;font-size:12px;min-height:100vh;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.07) 2px,rgba(0,0,0,.07) 4px);pointer-events:none;z-index:9999}
@keyframes flicker{0%,100%{opacity:1}93%{opacity:.88}99%{opacity:.93}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes pulse-r{0%,100%{box-shadow:0 0 5px var(--r)}50%{box-shadow:0 0 16px var(--r)}}
@keyframes pulse-g{0%,100%{box-shadow:0 0 4px var(--g)}50%{box-shadow:0 0 14px var(--g)}}
@keyframes scrolllog{0%{transform:translateY(0)}100%{transform:translateY(-50%)}}
body{animation:flicker 9s infinite}

.hdr{display:flex;align-items:center;justify-content:space-between;padding:12px 14px 8px;border-bottom:1px solid var(–bd);background:var(–bg2);position:sticky;top:0;z-index:100}
.logo{font-family:‘VT323’,monospace;font-size:26px;letter-spacing:3px;text-shadow:0 0 10px var(–g)}
.logo span{color:var(–r);text-shadow:0 0 10px var(–r)}
.hdr-r{text-align:right;font-size:10px;color:var(–mt);line-height:1.8}
.live{color:var(–r);text-shadow:0 0 8px var(–r);font-size:11px}
.blink{animation:blink 1s step-end infinite}

.stats{display:flex;border-bottom:1px solid var(–bd)}
.st{flex:1;padding:8px 10px;border-right:1px solid var(–bd);background:var(–bg2)}
.st:last-child{border-right:none}
.st-l{font-size:9px;color:var(–mt);text-transform:uppercase;letter-spacing:1px;margin-bottom:3px}
.st-v{font-family:‘VT323’,monospace;font-size:24px;line-height:1}
.sr{color:var(–r);text-shadow:0 0 8px var(–r)}
.sg{color:var(–g);text-shadow:0 0 8px var(–g)}
.sy{color:var(–y);text-shadow:0 0 8px var(–y)}

.sec-t{font-size:9px;letter-spacing:2px;color:var(–mt);text-transform:uppercase;padding:8px 14px 6px;border-bottom:1px solid var(–bd);background:var(–bg2)}

.node{padding:10px 14px;border-bottom:1px solid var(–bd);cursor:pointer;transition:background .15s;border-left:2px solid transparent}
.node:hover{background:rgba(0,255,65,.03)}
.node.sel{background:rgba(0,255,65,.05);border-left-color:var(–g)}
.node.sel-r{background:rgba(255,46,46,.04);border-left-color:var(–r)}
.nt{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}
.nm{font-family:‘VT323’,monospace;font-size:17px}
.badge{font-size:9px;padding:2px 6px;border-radius:2px;letter-spacing:1px;text-transform:uppercase}
.b-g{background:rgba(0,255,65,.1);color:var(–g);border:1px solid rgba(0,255,65,.3);animation:pulse-g 2s infinite}
.b-r{background:rgba(255,45,45,.1);color:var(–r);border:1px solid rgba(255,45,45,.3);animation:pulse-r 1.4s infinite}
.b-i{background:transparent;color:var(–mt);border:1px solid var(–mt)}
.nm-meta{display:flex;gap:12px;font-size:10px;color:var(–mt);flex-wrap:wrap}
.nm-meta span{color:var(–tx)}

.det{padding:12px 14px}
.det-host{font-family:‘VT323’,monospace;font-size:20px;color:var(–g);text-shadow:0 0 8px var(–g)}
.det-sub{font-size:10px;color:var(–mt);margin-top:2px;margin-bottom:10px}
.ir{display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid rgba(10,42,10,.8);font-size:11px}
.il{color:var(–mt)}.iv{color:var(–tx)}
.iv.dan{color:var(–r);text-shadow:0 0 5px var(–r)}
.iv.wrn{color:var(–y)}
.iv.ok{color:var(–g)}
.sub2{font-size:9px;letter-spacing:2px;color:var(–mt);text-transform:uppercase;margin:12px 0 6px}
.fe{display:flex;justify-content:space-between;padding:4px 7px;background:rgba(0,255,65,.03);border:1px solid var(–bd);margin-bottom:3px;font-size:10px}
.fp{color:var(–g);word-break:break-all}.fs{color:var(–mt);white-space:nowrap;margin-left:6px}

.log-panel{border-top:1px solid var(–bd);background:var(–bg2);height:100px}
.log-t{font-size:9px;letter-spacing:2px;color:var(–mt);text-transform:uppercase;padding:5px 14px 3px;border-bottom:1px solid var(–bd)}
.log-scr{overflow:hidden;height:75px}
.log-in{padding:3px 14px;animation:scrolllog 20s linear infinite}
.ll{font-size:10px;color:var(–mt);line-height:1.7}
.ll .ts{color:var(–bd);margin-right:6px}
.ll.w .m{color:var(–y)}.ll.e .m{color:var(–r)}.ll.o .m{color:var(–dg)}
::-webkit-scrollbar{width:3px}::-webkit-scrollbar-track{background:var(–bg)}::-webkit-scrollbar-thumb{background:var(–mt)}
</style>

</head>
<body>

<div class="hdr">
  <div class="logo">fs<span>0</span>ciety <span style="font-size:12px;color:var(--mt);letter-spacing:1px">// C2</span></div>
  <div class="hdr-r">
    <div class="live">● LIVE <span class="blink">_</span></div>
    <div id="clk">--:--:--</div>
    <div>TUN0 · 10.0.0.44</div>
  </div>
</div>

<div class="stats">
  <div class="st"><div class="st-l">Compromised</div><div class="st-v sr">5</div></div>
  <div class="st"><div class="st-l">Sessions</div><div class="st-v sg">4</div></div>
  <div class="st"><div class="st-l">Exfil</div><div class="st-v sr">1</div></div>
  <div class="st"><div class="st-l">Data</div><div class="st-v sy">4.2 GB</div></div>
</div>

<div class="sec-t">// compromised nodes</div>

<div class="node sel" onclick="show(0)">
  <div class="nt"><div class="nm" style="color:var(--g)">srv-nexcorp-prod01</div><div class="badge b-g">Active</div></div>
  <div class="nm-meta">IP:<span>172.16.4.23</span> OS:<span>Ubuntu 18.04</span> User:<span style="color:var(--r)">ROOT</span></div>
</div>
<div class="node" onclick="show(1)">
  <div class="nt"><div class="nm" style="color:var(--r)">db-nexcorp-mysql01</div><div class="badge b-r">Exfiltrating</div></div>
  <div class="nm-meta">IP:<span>172.16.4.31</span> OS:<span>Debian 10</span> User:<span style="color:var(--r)">ROOT</span></div>
</div>
<div class="node" onclick="show(2)">
  <div class="nt"><div class="nm" style="color:var(--y)">wkstn-nxc-adm02</div><div class="badge b-g">Active</div></div>
  <div class="nm-meta">IP:<span>172.16.2.11</span> OS:<span>Windows 10</span> User:<span style="color:var(--y)">SYSTEM</span></div>
</div>
<div class="node" onclick="show(3)">
  <div class="nt"><div class="nm" style="color:var(--y)">mail-nexcorp-ex01</div><div class="badge b-g">Active</div></div>
  <div class="nm-meta">IP:<span>172.16.4.18</span> OS:<span>Win Server 2016</span> User:<span style="color:var(--y)">SYSTEM</span></div>
</div>
<div class="node" onclick="show(4)">
  <div class="nt"><div class="nm" style="color:var(--g)">cctv-hub-nxc-gf</div><div class="badge b-i">Idle</div></div>
  <div class="nm-meta">IP:<span>192.168.10.5</span> OS:<span>Embedded Linux</span> User:<span>root</span></div>
</div>

<div id="det" class="det"></div>

<div class="log-panel">
  <div class="log-t">// live activity</div>
  <div class="log-scr"><div class="log-in" id="log"></div></div>
</div>

<script>
const N=[
  {host:"srv-nexcorp-prod01",sub:"172.16.4.23 · Ubuntu 18.04.5 · Apache/Tomcat",
   rows:[["Access Level","ROOT (uid=0)","dan"],["Entry Vector","CVE-2019-0708 — Tomcat AJP RCE","wrn"],
         ["Session","Reverse Shell → port 4444","ok"],["Persistence","SSH backdoor port 2222","wrn"],
         ["AV","None detected","ok"],["Firewall","UFW disabled","ok"],["First Seen","2026-03-19 02:14:33",""]],
   files:[["/opt/nexcorp/data/employees.sql","812 KB"],["/opt/nexcorp/finance/q3_payroll.csv","241 KB"],
          ["/var/www/html/config/db.php","2.1 KB"],["/home/admin/.ssh/id_rsa","1.7 KB"],["/etc/shadow","4.3 KB"]]},
  {host:"db-nexcorp-mysql01",sub:"172.16.4.31 · Debian 10 · MySQL 5.7.32",
   rows:[["Access Level","ROOT (uid=0)","dan"],["Entry Vector","Lateral move — stolen SSH key","wrn"],
         ["Status","EXFILTRATING — 1.3 GB remain","dan"],["DB","nexcorp_prod — 34 tables","wrn"],
         ["Session","Reverse Shell → port 5555","ok"],["First Seen","2026-03-19 03:02:11",""]],
   files:[["/var/lib/mysql/nexcorp_prod/customers.ibd","2.1 GB"],["/var/lib/mysql/nexcorp_prod/invoices.ibd","890 MB"],
          ["/root/dump/nexcorp_full.sql","2.1 GB"],["/root/dump/users_plain.txt","44 KB"]]},
  {host:"wkstn-nxc-adm02",sub:"172.16.2.11 · Windows 10 Pro · Domain: NEXCORP",
   rows:[["Access Level","NT AUTHORITY\\SYSTEM","dan"],["Entry Vector","Phishing — macro payload","wrn"],
         ["Session","Meterpreter HTTPS → port 443","ok"],["Domain User","NEXCORP\\kadmin (Domain Admin)","dan"],
         ["NTLM Hash","Captured — cracking 23%...","wrn"],["AV","Windows Defender — bypassed","ok"],
         ["First Seen","2026-03-20 11:44:07",""]],
   files:[["C:\\Users\\kadmin\\Documents\\VPN_Credentials.docx","44 KB"],
          ["C:\\Users\\kadmin\\Desktop\\server_map.xlsx","128 KB"],
          ["C:\\Windows\\NTDS\\ntds.dit","11 MB"],["C:\\Temp\\mimikatz_output.txt","28 KB"]]},
  {host:"mail-nexcorp-ex01",sub:"172.16.4.18 · Windows Server 2016 · Exchange 2019",
   rows:[["Access Level","Exchange Admin / SYSTEM","dan"],["Entry Vector","ProxyLogon CVE-2021-26855","wrn"],
         ["Web Shell","\\owa\\auth\\svcdiag.aspx","ok"],["Mailboxes","214 indexed","dan"],
         ["Emails","8,400 — CEO + Finance","dan"],["Persistence","Web shell + sched task","wrn"],
         ["First Seen","2026-03-20 23:58:41",""]],
   files:[["C:\\Exports\\ceo_mailbox_full.pst","1.8 GB"],["C:\\Exports\\finance_Q1_Q2.pst","740 MB"],
          ["C:\\Exports\\hr_all_staff.pst","2.1 GB"]]},
  {host:"cctv-hub-nxc-gf",sub:"192.168.10.5 · Embedded Linux · Hikvision DS-7608NI",
   rows:[["Access Level","root","ok"],["Entry Vector","Default creds admin:12345","wrn"],
         ["Cameras","8 live — lobby, car park, server room","dan"],
         ["RTSP","rtsp://192.168.10.5:554/ch01","wrn"],
         ["NVR Storage","30-day recording accessible","dan"],["First Seen","2026-03-21 07:19:02",""]],
   files:[["/mnt/nvr/2026-03-21/ch01_lobby.mp4","4.1 GB"],["/mnt/nvr/2026-03-21/ch05_serverroom.mp4","4.1 GB"],
          ["/etc/hikvision/users.conf","1.4 KB"]]}
];

function show(i){
  const n=N[i];
  let h=`<div class="det-host">${n.host}</div><div class="det-sub">${n.sub}</div>`;
  n.rows.forEach(([l,v,c])=>{h+=`<div class="ir"><span class="il">${l}</span><span class="iv ${c}">${v}</span></div>`});
  h+=`<div class="sub2">// exfiltrated files</div>`;
  n.files.forEach(([p,s])=>{h+=`<div class="fe"><span class="fp">${p}</span><span class="fs">${s}</span></div>`});
  document.getElementById('det').innerHTML=h;
  document.querySelectorAll('.node').forEach((el,j)=>{
    el.classList.remove('sel','sel-r');
    if(j===i)el.classList.add(i===1?'sel-r':'sel');
  });
}
show(0);

// clock
setInterval(()=>{document.getElementById('clk').textContent=new Date().toTimeString().slice(0,8)},1000);

// log
const logs=[
  ["o","SESSION ALIVE · srv-nexcorp-prod01 · ping 2s"],
  ["e","EXFIL IN PROGRESS · db-nexcorp-mysql01 · 847 MB / 2.1 GB"],
  ["w","FILE INDEXED · /var/lib/mysql/nexcorp_prod/customers.ibd"],
  ["o","SHELL OK · wkstn-nxc-adm02 · 44ms"],
  ["o","SESSION ALIVE · mail-nexcorp-ex01 · web shell responding"],
  ["w","CRED CRACKING · NEXCORP\\\\kadmin NTLM — 23%"],
  ["o","TUNNEL STABLE · tun0 → 10.0.0.44 · encrypted"],
  ["w","MAILBOX INDEXED · ceo@nexcorp.com · 2140 emails"],
  ["e","CAMERA STREAM · rtsp://192.168.10.5:554/ch05 · server room"],
  ["o","DOMAIN ADMIN HASH CAPTURED · NEXCORP\\\\kadmin"],
  ["e","EXFIL DONE · q3_payroll.csv · 241 KB"],
  ["o","HEARTBEAT · all 5 nodes alive"],
];
const now=Date.now();
let h='';
[...logs,...logs].forEach(([c,m],i)=>{
  const d=new Date(now-(logs.length-(i%logs.length))*14000);
  const ts=d.toTimeString().slice(0,8);
  h+=`<div class="ll ${c}"><span class="ts">[${ts}]</span><span class="m">${m}</span></div>`;
});
document.getElementById('log').innerHTML=h;
</script>

</body>
</html>"""

@app.route(”/”)
def index():
return render_template_string(HTML)

if **name** == “**main**”:
print(”\n  NexCorp C2 Dashboard”)
print(”  Open http://localhost:8888 in your browser\n”)
app.run(host=“0.0.0.0”, port=8888, debug=False)
