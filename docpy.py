import docker

def docpy():
    cl = docker.from_env()
    print("docker imageのプルを行います")
