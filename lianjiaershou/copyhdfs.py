from pyhdfs import HdfsClient

HdfsClient(hosts='master:50070',user_name='hadoop').create('D:\programs\JetBrains\pythonwork\lianjiaershou\syershoufang.txt','/sy.txt')