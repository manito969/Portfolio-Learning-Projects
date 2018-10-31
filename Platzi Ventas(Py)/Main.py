import sys
Clients = 'pablo,ricardo,'

def create_client (Client_name):
    global Clients

    if client_name not in Clients:
        Clients += Client_name 
        _add_comma
    else:print('Client already in in the client\'s list')

def _add_comma():
    global Clients
    Clients +=','

def list_clients():
    global Clients
    print(Clients)

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*100)
    print('What woul you like to do today')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]hearch client')
    print('[L]ist of clients')

def _getclient_name():
    client_name=None

    while not client_name:
        client_name = input ('What is the client name? ')

        if client_name == 'exit':
            client_name= None
            break
    if not client_name:
        sys.exit()

    return client_name

def update_client(client_name, updated_client_name):
    global Clients
    if client_name in Clients:
        Clients= Clients.replace(client_name +',',updated_client_name +',')
    else:
        print('Client No exist')

def delete_client(client_name):
    global Clients
    if client_name in Clients:
        Clients= Clients.replace(client_name+',','')
    else: 
        print('Client No exist')

def search_client(client_name):
    global Clients
    clients_list= Clients.split(',')
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True
         
if __name__=='__main__':
    _print_welcome()

    command = input()
    command= command.upper()

    if command == 'C':
        client_name= _getclient_name()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_name= _getclient_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name= _getclient_name()
        updated_client_name= input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'S':
        client_name=_getclient_name()
        found=search_client(client_name)
        if found:
            print('The client is in the client\' list')
        else:
            print('The client: {} is not our client\'s list'.format(client_name))
    else:
        print('Invalid command')




    

