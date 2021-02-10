
import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224


def Comandi(socket): #controllo dei dati
    
    while True:
        try:
            dati = input(
                "dati dell'operazione (ko per terminare la connessione): ")
        except EOFError:
            print("\nOkay. Exit")
            break
        if not dati:
            print("Errore")
            continue
        if dati == 'ko':
            print("Chiudo la connessione con il server!")
            break

        dati = dati.encode() #codifica dei dati
        socket.send(dati) #invio dei dati
        dati = socket.recv(2048)


        if not dati: #se il server non risponde, mando il break per uscire
            print("Server non risponde. Exit")
            break

        dati = dati.decode()

        print("Ricevuto dal server:")
        print(dati + '\n')


#verifichiamo la connessione
def connessioneServer(address, port):
    sock_service = socket.socket()
    sock_service.connect((address, port))
    print("Connesso a " + str((address, port)))
    Comandi(sock_service)
    sock_service.close()

if __name__ == "__main__":
    connessioneServer(SERVER_ADDRESS, SERVER_PORT)