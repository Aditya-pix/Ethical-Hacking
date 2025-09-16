import whois
from domain_validator import is_registered
domain_name="psit.ac.in"
if is_registered(domain_name):
    whois_info=whois.whois(domain_name)
    print("Domain registrar: ",whois_info.registrar)
    print("Domain server: ",whois_info.whois_server)
    print("Domain creation date: ",whois_info.creation_date)
    print("Domain Expiration date: ",whois_info.expiration_date)
    print(whois_info)
    print(type(whois_info))