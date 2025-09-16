import socket

def reverse_dns_lookup(ip_address):
    try:
        host,_,_=socket.gethostbyaddr(ip_address)
    except socket.herror:
        return None
    return host

if __name__=="__main__":
    ip_address='8.8.8.8'
    domain_name=reverse_dns_lookup(ip_address)
    if domain_name:
        print(f"The domain name for IP address {ip_address} is {domain_name}")
    else:
        print(f"No domain name found for IP address {ip_address}")