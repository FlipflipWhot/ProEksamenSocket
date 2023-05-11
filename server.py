import socket
from _thread import *
from player import Player
import pickle

server = '192.168.67.1'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print('Waiting for a connection, server Started')

players = [Player([0, 0], [10, 10], 'red', 'player one'),
           Player([100, 100], [10, 10], 'blue', 'player two')]

def threaded_client(conn, player):
    reply = ''
    conn.send(pickle.dumps(players[player]))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print(f'Received: {data}')
                print(f'Sending: {reply}')

            conn.sendall(pickle.dumps(reply))

        except socket.error:
            break
    print('Lost connection')
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print(f'Connected to: {addr}')

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
