import os
import platform
import time
import docker
from pyfiglet import Figlet


op = platform.system()
op = op.replace('#','')


path = os.getcwd()

if op == "Windows":
    path = str(path) + "\\docker-compose.yml"
else:
    path = str(path) + "/docker-compose.yml"

f = open(path, 'w')
f.write('')
f.close()



f = Figlet(font='big')
msg = f.renderText('Auto-compose')
print(msg)



print("1. This tool is not for beginners.")
print("2. Use it to make things easier for the experts.")
print("3. This tool is OSS\n\n")

print("\n\n立ち上げたいコンテナの数")
global connum
connum = input()
connum = int(connum)
time.sleep(0.3)


def network():
    print("\nnetworkの設定をしますか？ (yes or no)")
    global netyesorno
    netyesorno = input()    
    time.sleep(0.3)
    if netyesorno == "yes":
        print("\n作成するネットワーク数")
        global netnum
        netnum = input()
        netnum = int(netnum)
        
    
def netall():            
    for c in range(netnum): 
        d = c + 1
        print("\n\n" + str(d) + "個目のネットワーク")
        print("\n指定するネットワークタイプ\n1. none\n2. default\n3. macvlan")
        net = input()
        global nethan
        
        if net == "1":
                        
            f = open(path, 'a')
            image = "     image: " + str(image) + "\n" 
            f.write(image)
            f.close()

        elif net == "2":
            print("\nネットワークの名前を入力してください")
            netname = input()
            time.sleep(0.3)
            print("\nネットワークのネットワークアドレスを入力してください")
            netadd = input()
            time.sleep(0.3)
            print("\nネットワークのサブネットをCIDRで入力してください(例：/24)")
            netsub = input ()
            time.sleep(0.3)
                
            f = open(path, 'a')
            if c == 0:
                net = "networks:\n  " + str(netname) + ":\n" + "    ipam:\n" + "      driver: default\n      config:\n        - subnet: " + str(netadd) + str(netsub) + "\n"
                f.write(net)
                f.close()
                time.sleep(0.3)
            else:
                net = "  " + str(netname) + ":\n" + "    ipam:\n" + "      driver: default\n      config:\n        - subnet: " + str(netadd) + str(netsub) + "\n"
                f.write(net)
                f.close()
                time.sleep(0.3)
                
                
        elif net == "3":            
            print("\nネットワークの名前を入力してください")
            netname = input()
            time.sleep(0.3)
            print("\nネットワークのネットワークアドレスを入力してください")
            netadd = input()
            time.sleep(0.3)
            print("\nネットワークのサブネットをCIDRで入力してください(例：/24)")
            netsub = input()
            time.sleep(0.3)
            print("ホストのネットワーク・インターフェース名を入力")
            netint = input()
            
            if vernum < 3:
                print("ネットワークのゲートウェイ")
                netgate = input()
            else:
                path
                
            f = open(path, 'a')


            if c == 0:
                if vernum < 3:
                    net = "networks:\n  " + str(netname) + ":\n    driver: macvlan\n    driver_opts:\n      parent: " + str(netint) + "\n" +"    ipam:\n" + "      config:\n        - subnet: " + str(netadd) + str(netsub) + "\n          gateway: " + str(netgate) + "\n"
                else:
                    net = "networks:\n  " + str(netname) + ":\n    driver: macvlan\n    driver_opts:\n      parent: " + str(netint) + "\n" +"    ipam:\n" + "      config:\n        - subnet: " + str(netadd) + str(netsub) + "\n"
                f.write(net)
                f.close()
                time.sleep(0.3)
            else:
                if vernum < 3:
                    net = "  " + str(netname) + ":\n    driver: macvlan\n    driver_opts:\n      parent: " + str(netint) + "\n" +"    ipam:\n" + "      config:\n        - subnet: " + str(netadd) + str(netsub) + "\n          gateway: " + str(netgate) + "\n"
                else:
                    net = "  " + str(netname) + ":\n    driver: macvlan\n    driver_opts:\n      parent: " + str(netint) + "\n" +"    ipam:\n" + "      config:\n        - subnet: " + str(netadd) + str(netsub) + "\n"
                f.write(net)
                f.close()
                time.sleep(0.3)


def connet():
    for c in range(netnum):
        d = c + 1
        print("\n適用させるネットワーク名(無い場合はnoneと入力)")
        print("\n" + str(d) + "個目")
        conn = input()
        if conn == "none":
            break
        else:
            f = open(path, 'a')
            
            if c == 0:
                net1 = "    networks:\n      " + str(conn) + ":\n"
            else:
                net1 = "      " + str(conn) + ":\n"
            f.write(net1)
            f.close()
            time.sleep(0.3)

            print("\nipアドレスの指定(指定しない場合はnone)")
            ip = input()

            if ip == "none":
                break

            else:
                f = open(path, 'a')
                net2 = "        ipv4_address: " + str(ip) + "\n"  
                f.write(net2)
                f.close()
                time.sleep(0.3)

def ver():
    print("\ndocker-compose.ymlファイルのバージョン")
    global vernum
    ver = input()
    vernum = int(ver)
    f = open(path, 'w')
    ver = "version: " + "'" + str(ver) + "'" + "\n"
    f.write(ver)
    f.close()
    time.sleep(0.3)


def conname():
    print("\n立ち上げたいコンテナの名前")
    conname = input()
    f = open(path, 'a')
    conname = "  " + conname + ":\n    container_name: " + str(conname) + "\n"
    f.write(conname)
    f.close()
    time.sleep(0.5)



def build():
    print("\nDockerfileはインターネットの物を参照しますか？ (yes or no)")
    yesorno = input()
    time.sleep(0.3)
    if yesorno == "yes":
        print("\nイメージ名を入力してください。")
        image = input()
        f = open(path, 'a')
        image = "    image: " + str(image) + "\n" 
        f.write(image)
        f.close()
        
    elif yesorno == "no":
        print("\nDockerfileのpathを入力してください。")
        imagepath = input()
        f = open(path, 'a')
        image = "    build: \n" + "      dockerfile: " + str(imagepath) + "\n"
        f.write(image)
        f.close()
        time.sleep(0.3)

def port():
    print("\nポートフォワーディングの設定をします。ホスト側のポート番号を入力してください（ポートフォワーディングをしない場合はnone）")
    port = input()
    time.sleep(0.3)
    if port == "none":
        path
    else:
        print("コンテナ側のポート番号を入力")
        conport = input()
        time.sleep(0.3)

        f = open(path, 'a')
        ports = "    ports: \n" + "      - " + str(port) + ":" + str(conport) + "\n"
        f.write(ports)
        f.close()
        time.sleep(0.3)


def volu():
    print("\nボリュームの紐付けを行います。紐付けたいボリューム数を入力してください。(紐付けをしない場合はnone)")    
    volnum = input()
    time.sleep(0.3)
    if volnum == "none":
        path
    else:
        volnum = int(volnum)
        for i in range(volnum):
            b = i + 1
            print("\n" + str(b) + "個目のボリューム")
            print("ホスト側のボリュームパスを入力")
            convol1 = input()
            os.makedirs(convol1, exist_ok=True)
            time.sleep(0.3)
            print("コンテナ側のボリュームパスを入力")
            convol2 = input()
            time.sleep(0.3)

            f = open(path, 'a')
            if i == 0:
                convolvol = "    volumes: \n" + "      - " + str(convol1) + ":" + str(convol2) + "\n"   
            else:
                convolvol = "\n" + "      - " + str(convol1) + ":" + str(convol2) + "\n" 
            f.write(convolvol)
            f.close()
            time.sleep(0.3)

def env():
    print("\n環境変数の設定を行います。設定したい変数の数を入力してください。(設定をしない場合はnone)")    
    envnum = input()
    time.sleep(0.3)
    if envnum == "none":
        path
    else:
        envnum = int(envnum)
        for i in range(envnum):
            b = i + 1
            print("\n" + str(b) + "個目の環境変数")
            print("設定したい環境変数を入力")
            conenv1 = input()
            time.sleep(0.3)
            print("環境変数のパラメータ")
            conenv2 = input()
            time.sleep(0.3)

            f = open(path, 'a')
            if i == 0:
                convolvol = "    environment: \n" + "      - " + str(conenv1) + ":" + str(conenv2) + "\n"   
            else:
                convolvol = "\n" + "      - " + str(conenv1) + "=" + str(conenv2) + "\n" 
            f.write(convolvol)
            f.close()
            time.sleep(0.3)


def res():
    print("\nコンテナの自動起動についての設定を行います。\n1. エラーで停止した場合に再起動(on-failure)\n2. 常に再起動(always)\n3. 設定しない\n")
    res = input()
    res = int(res)
    time.sleep(0.3)
    if res == 1:
        f = open(path, 'a')
        resop = "    restart: on-failure\n"   
        f.write(resop)
        f.close()
        time.sleep(0.3)       

    elif res == 2:
        f = open(path, 'a')
        resop = "    restart: always\n"   
        f.write(resop)
        f.close()
        time.sleep(0.3)       

    elif res == 3:
        f = open(path, 'a')
        resop = "    restart: no\n"   
        f.write(resop)
        f.close()
        time.sleep(0.3)  


def tty():             
    print("\nコンテナのタスクが終了しても、起動したままにしますか？(yes or no)")
    tty = input()
    if tty == "yes":
        f = open(path, 'a')
        ttyop = "    tty: true\n"   
        f.write(ttyop)
        f.close()
        time.sleep(0.3)
    else:
        path

def com():
    print("\nコンテナで実行したいコマンドの数を入力してください。(無い場合は0)")
    com = input()
    com = int(com)
    time.sleep(0.3)
    
    if com == 1:
        print("\nコンテナで実行したいコマンドを入力してください")
        comcom = input()
        f = open(path, 'a')
        comop = "    command: >\n      bash -c'" + str(comcom) + "'"  
        f.write(comop)
        f.close()
        time.sleep(0.3) 

    elif com > 1:    
        for i in range(com):
            b = i + 1
            print("\nコンテナで実行したいコマンドを入力してください")
            print(str(b) + "個目")

            comcom = input()
            f = open(path, 'a')

            if i == 0:
                comop = "    command: >\n      bash -c'" + str(comcom) + " &&\n"  

            elif b == com:
                comop = "      " + str(comcom) + "'"
                
            else:
                comop = "      " + str(comcom) + "&&\n"

            f.write(comop)
            f.close()
            time.sleep(0.3)
                        
        f = open(path, 'a')
    else:
        path   
 
        
def dep():
    print("\nこのコンテナより先に起動させたいコンテナの数を入力してください（特に設定しない場合は0）")
    dep = input()
    dep = int(dep)

    if dep > 0:
        for i in range(dep):
            depnum = i + 1        
            print("\nこのコンテナより先に起動させたいコンテナの名前")
            print(str(depnum) + "個目")
            depp = input()

            f = open(path, 'a')
            if i == 0:
                depop = "\n    depends_on:\n      - " + str(depp) + "\n"  
            else:
                depop = "\n      - " + str(depp) + "\n"
            
            f.write(depop)
            f.close()
            time.sleep(0.3)     
    else:    
     path


def docker():
    print("dockerのインストールは行っていますか？(yes or no)")
    doc = input()
    if doc == "yes":
        time.sleep(0.3)
        print("dockerの操作を行います。")
        docpy()
        
    else:
        path


def docpy():
    cl = docker.from_env()
    print("docker imageのプルを行います")


#########################################################################################
        
try:
    ver()
except:
    print("\nエラーを検知しました。再設定を行います。\n")
    ver()

try:    
    network()
except:
    print("\nエラーを検知しました。再設定を行います。\n")
    network()

if netyesorno == "yes":
    try:
        netall()
    except:
        netall()
        
    f = open(path, 'a')
    space = "\n\n"
    f.write(space)
    f.close()


a = "\nservices:\n" 
f = open(path, 'a')
f.write(a)
f.close()
time.sleep(0.5)

for i in range(connum):
    d = i + 1
    print("\n\n\n\n\n" +str(d) + "個目のコンテナの作成を行います。")
    
    try:
        conname()
    except:
        print("\nエラーを検知しました。再設定を行います。\n")
        conname()

    try:    
        build()
    except:
        print("\nエラーを検知しました。再設定を行います。\n")
        build()
 
    if netyesorno == "yes":
        try:
            connet()
        except:
            print("\nエラーを検知しました。再設定を行います。\n")
            connet()

    try:    
        port()
    except:
        print("\nエラーを検知しました。再設定を行います。\n")
        port()

    try:
        volu()
    except:
        print("\nエラーを検知しました。再設定を行います。\n")
        volu()

    try:
        env()
    except:
        print("\nエラーを検知しました。再設定を行います。\n")
        env()

    try:    
        res()
    except:
        print("\nエラーを検知しました。再設定を行います。\n")
        res()

    try:
        tty()
    except:
        print("\nエラーを検知しました。再設定を行います。\n")
        tty()

    try:    
        com()
    except:
        print("\nエラーを検知しました。再設定を行います。\n")
        com()

    if connum > 1:
        try:
            dep()
        except:
            print("\nエラーを検知しました。再設定を行います。\n")
            dep()





    f = open(path, 'a')
    space = "\n\n"
    f.write(space)
    f.close()

    b = i + 1    
    print("\n" + str(b) + "個目のコンテナを作成しました\n\n")


time.sleep(1)
print("\ndocker-compose.ymlファイルを" + str(path) + "に作成しました。")
print("\n\ndocker-compose.yml\n")
with open(path) as f:
    yml = f.read()
print(yml)
