# About Scrapy

1. pip3 install scrapy
2. scrapy startproject [project name]
   then you can see this directory structure
   ```shell
   user % tree .
   .
    ├── scrapy.cfg
    └── start_scrapy
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-312.pyc
        │   └── settings.cpython-312.pyc
        ├── items.py # 스크랩할 요소 정의
        ├── middlewares.py # 미들웨어 정의
        ├── pipelines.py # 파이프라인 정의
        ├── settings.py # 설정
        └── spiders
            ├── __init__.py
            ├── __pycache__
            │   ├── __init__.cpython-312.pyc
            │   ├── pagerutine.cpython-312.pyc # 사용자 정의
            │   └── testspider.cpython-312.pyc # 사용자 정의
            ├── pagerutine.py # 사용자 정의
            └── testspider.py # 사용자 정의
    
    5 directories, 16 files

Each Spider Execute
> scrapy runspuder [project name] --output [result file name] --output-format [output file format]
