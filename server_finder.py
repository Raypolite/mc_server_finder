from mcstatus import MinecraftServer
import random

def DbUpdate(finalIp, query, status):
    dataBase = open("ServerNameDataBase.txt", "a")
    dataBase.write("ip: {0}".format(finalIp))
    dataBase.write(
        "The server has {0} players and replied in {1} ms\n".format(status.players.online, status.latency))
    dataBase.write("The server has the following players online: {0}\n".format(", ".join(query.players.names)))
    dataBase.write("plugins:" + str(query.software.plugins) + ", ")
    dataBase.write("version:" + str(query.software.version) + ", ")
    dataBase.write(str(query.software.brand))
    dataBase.write("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    dataBase.close()

def find():
    try:
        finalIp = '.'.join('%s'%random.randint(0, 255) for i in range(4))
        print(finalIp)
        server = MinecraftServer.lookup(finalIp)

        status = server.status()

        query = server.query()

        DbUpdate(finalIp, query, status)

        print("server found!")
        pass
    except:
        print("no server found!")
        pass
    find()

find()
