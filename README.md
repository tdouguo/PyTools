# [PyTools](https://github.com/tdouguo/PyTools)

Python 常用小工具, 欢迎您 Pull requests 。

***贡献规范: ***

1. 测试通过可运行
2. 依赖模块文件 requirements.txt
3. 使用说明
 

# list

- [x] ***pdf2world [文档](#pdf2world)*** 
- [x] ***tinypng [文档](#tinypng)*** 基于 www.tinypng.png 压缩图片 png jpg jpeg 
- [ ] xlsx to json
- [ ] xlsx to csv
- [ ] xlsx to xml


# python 虚拟环境

1. 创建虚拟环境
```bash
virtualenv -p python3.7 venv
```

2. 激活虚拟环境
```bash
source venv/bin/activate
```

3. 安装依赖模块
```bash
pip install -r requirements.txt 
```

- 扩展 导出依赖模块
```bash
pip freeze > requirements.txt
```


# Document

## pdf2world

1. 安装模块
```bash
cd pdf2world/
pip install -r requirements.txt 
```

2. 使用
```bash 
python pdf2world.py ./source.pdf ./output.docs
```


## tinypng

1. 访问 [www.tinypng.png](www.tinypng.png) 获取 Key 并在 tinypng.py 脚本内 tinify.key 赋值

2. 安装模块
```bash
cd pdf2world/
pip install -r requirements.txt 
```

3. 使用
```bash
python pdf2world.py ./sourceFolder ./outputFolder
```

