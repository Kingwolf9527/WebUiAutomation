# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/7/14 4:23

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
import os


# # 谷歌浏览器驱动
# chrome_driver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))),
#                                    "data", "browser_drivers", "chromedriver.exe")
# # 火狐浏览器驱动
# firefox_driver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))),
#                                    "data", "browser_drivers", "geckodriver.exe")
# # edge浏览器驱动
# edge_driver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))),
#                                 "data", "browser_drivers", "msedgedriver.exe")

# 处理allure报告的路径
allure_json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'allure_report', 'json_path')

allure_html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'allure_report', 'allure_path')


# 基础yaml配置路径
base_yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

# 配置文件路径
base_config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "base.yaml")

# 数据库yaml格式配置文件
db_config = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "db_config.yaml")

# 普通用户账号数据
foreground_infos = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "foreground.yaml")


# 截图保存文件路径
image_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images")


# 默认Excel文件的路径
default_excel_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                  "data", "excel_data.xlsx")

# 默认sheet_name
default_sheet_name = "users"

print(base_yaml_path)

