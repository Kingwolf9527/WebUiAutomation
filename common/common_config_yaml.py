# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2022/3/9 21:15


import yaml


class CommonYaml(object):

    def __init__(self, file):
        """
        @param file:
        """
        self.file = file

    def read_yaml(self):
        """
        读取yaml文件数据
        """
        with open(self.file, encoding="utf-8") as f:
            return yaml.load(stream=f, Loader=yaml.FullLoader)

    def wtite_yaml(self, data):
        """
        把数据写入yaml文件中，mode模式为追加(a)，同时处理中文(allow_unicode=True)
        """
        with open(self.file, encoding="utf-8", mode="a") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def clear_yaml(self):
        """
        情况yaml文件，mode模式为读取(w)
        """
        with open(self.file, encoding="utf-8", mode="w") as f:
            f.truncate()

if __name__ == '__main__':
    from common.common_file_path import base_yaml_path
    test_path = base_yaml_path / 'login_data.yaml'
    test = CommonYaml(test_path)
    data = test.read_yaml()
    for i in data:
        print(i['login_base']['login_links'])
        print(type(i['login_base']['login_links']))

