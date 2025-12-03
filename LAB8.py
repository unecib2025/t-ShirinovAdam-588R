N1
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
unique_ips = set(ips)
print(unique_ips)
N2
bannedlogins={"root", "admin", "test"}
bannedlogins.add("hacker")
bannedlogins.remove("test")
print(bannedlogins)
N3
bannedports={21, 22, 23, 25}
if 22 in bannedports:
    print("Порт запрещён")
else:
    print("Порт разрешаен")
N4
a={"mal.com", "bad.net"}
b={"bad.net", "xevil.org"}
print(b.difference(a))
N5
whitelist={"alice", "bob", "root"}
blacklist={"root", "admin"}
print(whitelist.intersection(blacklist))
N6
a={"CVE-1", "CVE-2"}
b={"CVE-2", "CVE-3"}
print(b.union(a))
N7
admin={"read", "write", "delete"}
user={"read", "download"}
print(admin.symmetric_difference(user))
N8
a=set(["123", "qwerty", "test", "123", "qwerty", "admin"])
a.remove("test")
print(a)
N9
global_ips = {"10.0.0.1", "10.0.0.2", "192.168.1.1"}
local_ips = {"10.0.0.2", "10.0.0.3"}
local_ips.intersection_update(global_ips)
print(local_ips)
N10
logs = ["scan", "debug_mode", "scan", "connect", "debug_info"]
s = set()
for elem in logs:
    if "debug" not in elem:
        s.add(elem)
print(s)