# PlotCrispr

Installation

```bash
pip install -r requirements.txt
```

Local Test

```bash
python manage.py runserver
```

File Tree

```
.
├── Nordic34.json（json格式原始数据）
├── Nordic34.xlsx（excel格式原始数据）
├── PlotCrispr（project）
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py（设置）
│   ├── urls.py（路由配置）
│   └── wsgi.py
├── README.md
├── db.sqlite3
├── display（app）
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py（表单）
│   ├── tests.py
│   ├── urls.py（路由配置）
│   └── views.py（后端函数）
├── manage.py（入口主文件）
├── readExcel.py（excel转json格式的程序）
├── requirements.txt（依赖）
├── static（静态模板文件）
│   ├── css
│   │   └── bootstrap-min.css
│   └── js
│       ├── bootstrap-bundle-min.js
│       ├── echarts-min.js
│       └── jquery-min.js
└── templates（前端页面）
    ├── crispr.html（单个CRISPR序列显示页面）
    ├── home.html（主页）
    └── location.html（显示某地域全部收录的序列）
```


