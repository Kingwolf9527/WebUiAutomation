# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/7/14 4:23

import sys
sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")
from pathlib import Path



# 处理allure报告的路径
allure_json_path = Path.cwd().parent.joinpath("allure_report", "json_path")
allure_html_path = Path.cwd().parent.joinpath("allure_report", "allure_path")


# 基础yaml配置路径
base_yaml_path = Path.cwd().parent.joinpath("data")
# base_yaml_path = Path.cwd().parent / 'data'

# 配置文件路径
base_config_path = Path.cwd().parent.joinpath("data", "base.yaml")

# 数据库yaml格式配置文件
db_config = Path.cwd().parent.joinpath("config", "db_config.yaml")

# 普通用户账号数据
foreground_infos = Path.cwd().parent.joinpath("data", "foreground.yaml")

# 截图保存文件路径
image_dir = Path.cwd().parent.joinpath("images")

# 默认Excel文件的路径
default_excel_path = Path.cwd().parent.joinpath("data", "excel_data.xlsx")

# 默认sheet_name
default_sheet_name = "users"

