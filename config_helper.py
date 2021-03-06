import os

def initialize_config(config):
    '''
    Setup config dictionary values from the environment.
    '''
    try:
        config["site"] = str(os.getenv("site"))
        config["api_token"] = str(os.getenv("api_token"))
        config["api_token_endpoint"] = str(os.getenv("api_token_endpoint"))
        config["access_token"] = str(os.getenv("access_token"))
        config["app_id"] = str(os.getenv("app_id"))
        config["app_secret"] = str(os.getenv("app_secret"))
        config["redirect_uri"] = str(os.getenv("redirect_uri"))
        config["created_at"] = int(os.getenv("created_at"))
        config["request_endpoint"] = str(os.getenv("request_endpoint"))
    except Exception as err:
        print(f"Problem getting environment variables. {err}")
        exit()

def print_config_as_env(config):
    '''
    Print the config.json in a way that can be stored in a .env
    '''
    for k,v in config.items():
        print(f'{k} = {v}')
