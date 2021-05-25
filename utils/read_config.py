import json


class config():
    def __init__(self) -> None:
        json_config = self.__read_config()
        self.data_path = json_config.setdefault("dataPath", "data/adult.data")
        self.qi_index = json_config.setdefault("qiIndex", [0, 1, 4, 5, 6, 8, 9, 13])
        self.is_cat = json_config.setdefault("isCat", [False, True, False, True, True, True, True, True])
        self.sa_index = json_config.setdefault("saIndex", -1)

    def __read_config(self):
        with open("config.json") as fp:
            return json.loads(fp.read())

if __name__ == "__main__":

    conf = config()
    print(conf.is_cat)
