
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

def _getclient_name():
    return input ('What is the client name? ')

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

if __name__=='__main__':
    _print_welcome()

    command = input()
    command= command.upper()

    if command == 'C':
        client_name= _getclient_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name= _getclient_name()
        delete_client(client_name)
        list_clients()
    elif command =='U':
        client_name= _getclient_name()
        updated_client_name= input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print('Invalid command')



    

