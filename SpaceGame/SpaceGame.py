from GameEngine import GameEngine
import json

CONFIG_FILE = "config.json"

def __loadConfigJson():
    global config
    with open(CONFIG_FILE,"r") as f:
        print("Configuration file loaded!")
        config = json.load(f)
    return config

def __saveConfigJson(config):
    with open(CONFIG_FILE,"w") as f:
        print("Configuration file saved!")
        f.write(json.dumps(config, indent=4, sort_keys=True))

def main():
    ge = GameEngine(__loadConfigJson())
    ge.loop()
    __saveConfigJson(ge.getConfig())


if __name__ == "__main__":
    main()
