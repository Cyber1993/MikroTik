import paramiko

def get_cap_registration_table():
   
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='172.16.1.2', username='**********', password='**********')
    

    stdin, stdout, stderr = ssh_client.exec_command("/caps-man registration-table print stats")

  
    print("Таблиця реєстрації CAP:")
    for line in stdout:
        print(line.strip())


    ssh_client.close()

if __name__ == "__main__":
    get_cap_registration_table()
