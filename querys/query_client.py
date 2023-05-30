from dao.cliente import ClienteDAO 

def show_client(username, password):
    client = ClienteDAO()
    data = client.select_client(username, password)
    return data


def update_client_db(i_rent, identification):
    client = ClienteDAO()
    client.update_client(i_rent, identification)