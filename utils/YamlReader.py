import yaml
import os

class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError(yamlf,' 文件不存在')
        self._data = None

    @property
    def data(self):
        # 如果第一次调用data,读取yaml文件，否则返回之前保存的数据
        if not self._data:
            with open(self.yamlf,'rb') as f :
                self._data = list(yaml.safe_load_all(f))
        return self._data


def loadyaml(fileName):
    files = open(fileName,'r',encoding='utf-8')

    data = yaml.load(files,Loader=yaml.FullLoader)

    return data


if __name__ == '__main__':

    a = loadyaml('../config/searchdata.yaml')
    print(a)

    b = YamlReader('../config/searchdata.yaml').data
    print(b)