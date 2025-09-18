import multiprocessing


def startJarvis():
    print("process 1 is starting......")
    from main import start
    start()

def listenHotword():
    print("process 2 is starting......")
    from engine.features import hotword
    hotword()    


if __name__=='__main__':
    from multiprocessing import Process
    p1=multiprocessing.Process(target=startJarvis)
    p2=multiprocessing.Process(target=listenHotword)

    p1.start()
    p2.start()
    p1.join()
    
    if p2.is_alive():
        p2.terminate()
        p2.join()
    print('system stop')    