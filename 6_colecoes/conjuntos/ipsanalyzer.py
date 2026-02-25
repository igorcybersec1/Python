ips1 = {"0.0.0.0", "1.1.1.1", "2.2.2.2", "3.3.3.3"}
ips2 = {"2.2.2.2", "3.3.3.3", "4.4.4.4", "5.5.5.5"}

suspects = ips1.intersection(ips2)
print("IPS SUSPEITOS:")

for value, ip in enumerate(suspects):

    position = value + 1
    print(f"{position}: {ip}")
