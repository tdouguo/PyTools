# PyTools


## python 虚拟环境

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

# complete list


***tinypng***

```bash
pip install -r png2svg/requirements.txt
python tinypng/tinypng.py './sourceFolder' './outputFolder'
```


# Future plans

- [ ] xlsx to json
- [ ] xlsx to csv
- [ ] xlsx to xml
