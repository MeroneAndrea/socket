#!/usr/bin/env python3
input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode() #con questo trasformiamo la scritta in bite
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode() #con questo la ricoddifichiamo
print(type(output_string))
print(output_string)

import socket #importiamo le socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_service = socket.socket()
sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT))) #controlliamo òla connessione
while True:
    try:
        dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ") #richiesta di un input 
    except EOFError:
        print("\nOkay. Exit")
        break
    if not dati:
        print("Non puoi inviare una stringa vuota!") #controllo
        continue
    if dati == '0':
        print("Chiudo la connessione con il server!") #chiusura del server
        break
    
    dati = dati.encode()

    sock_service.send(dati)

    dati = sock_service.recv(2048)

#encode dei dati

    if not dati: #controllo per vedere se il server funzina perfettamente
        print("Server non risponde. Exit")
        break
    
    dati = dati.decode()

    print("Ricevuto dal server:") #avviso che i dati sono stati inoltrati correttamente
    print(dati + '\n')

sock_service.close()