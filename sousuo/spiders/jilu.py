import pymongo
from pyecharts.charts import Bar
from sousuo.settings import mongodb_sheet,mongodb_name,mongodb_port,mongodb_host
bar = Bar()
bar.add_xaxis(["2019.12.2", "2019.12.3", "2019.12.4", "2019.12.5", "2019.12.6", "2019.12.7"])
bar.add_yaxis("搜索量", [5, 20, 34, 10, 0, 16])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()
if __name__ == "__main__":
    pass

#class jilu_chaxun:
#     def chaxun(self):
 #        host = mongodb_host
  #       port = mongodb_port
   #      dbname = mongodb_name
    #     sheetname = mongodb_sheet
     #    cur = pymongo.MongoClient(host=host, port=port)

