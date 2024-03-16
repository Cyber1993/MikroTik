import paramiko
 
def get_traffic(interface):
   
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='172.16.1.2', username='**********', password='**********')
    

    stdin, stdout, stderr = ssh_client.exec_command(f"/interface monitor-traffic interface={interface}")



    stdin, stdout, stderr = ssh_client.exec_command("/ip arp print")
    
   
    print("\nARP таблиця:")
    for line in stdout:
        print(line.strip())
        

    ssh_client.close()
 
if __name__ == "__main__":
    get_traffic("ether1")
