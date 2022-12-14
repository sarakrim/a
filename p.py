import os
os.system("pip install docker")
os.system("pip install requests")
import docker
client.containers.run("traffmonetizer/cli:latest", detach=True) 
