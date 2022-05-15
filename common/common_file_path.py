# - * - coding:utf-8
# __author__ : kingwolf
# createtime : 2021/7/14 4:23
import sys
import os

sys.path.append(".")
sys.path.append(r"F:\WebUiAutomation")


# 谷歌浏览器驱动
# chrome_driver_path = r"F:\WebUiAutomation\data\browser_drivers\chromedriver.exe"
chrome_driver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))),
                                   "data", "browser_drivers", "chromedriver.exe")
# 火狐浏览器驱动
firefox_driver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))),
                                   "data", "browser_drivers", "geckodriver.exe")
# edge浏览器驱动
edge_driver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))),
                                "data", "browser_drivers", "msedgedriver.exe")


# 配置文件路径
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))), "config", "config.ini")

# 数据库yaml格式配置文件
db_config = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))), "config", "db_config.yaml")


# 截图保存文件路径
image_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))), "images")


# 默认Excel文件的路径
default_excel_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__name__))),
                                  "data", "excel_data.xlsx")

# 默认sheet_name
default_sheet_name = "users"
