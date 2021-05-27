import json


class dataConfig():
    def __init__(self):
        json_config = self.__read_config()
        self.data_path = json_config.setdefault("dataPath", "data/adult.data")
        self.qi_index = json_config.setdefault("qiIndex", [0, 1, 4, 5, 6, 8, 9, 13])
        self.is_cat = json_config.setdefault("isCat", [False, True, False, True, True, True, True, True])
        self.sa_index = json_config.setdefault("saIndex", -1)

    def __read_config(self):
        with open("config.json") as fp:
            return json.loads(fp.read())["inputData"]

class modeConfig():
    def __init__(self):
        json_config = self.__read_config()
        self.model = json_config.setdefault("model", "relax")
        self.k = json_config.setdefault("k", 10)
        self.flag = json_config.setdefault("flag", "")

    def __read_config(self):
        with open("config.json") as fp:
            return json.loads(fp.read())["mode"]
        

if __name__ == "__main__":
    # test read config here
    conf = modeConfig()
    print(conf.k)
