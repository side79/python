import configparser

def demo_config_parser():
    config = configparser.ConfigParser()
    config.read("8_less_files_and_network/demo-config.ini")
    print(config)
    print(config.sections())

    print(list(config))
    psql = config['postgresql']
    print("psql", psql)
    print("psql", list(psql))
    
    for kay in psql:
        print(kay, psql[kay])
    print("----------------------------------")
    psql_host = psql['host']
    print(psql_host)
    psql_user = config["postgresql"]["user"]
    print(psql_user)
    
    myql_user = config["mysql"]["user"]
    print(myql_user)
    
    
    psql_port = psql.get("port", 5432)
    print(psql_port)
    
    config["postgresql"]["port"] = str(psql_port)
    
    with open("8_less_files_and_network/demo-config.ini" , "w") as f:
        config.write(f)
    
if __name__ == "__main__":
    demo_config_parser()