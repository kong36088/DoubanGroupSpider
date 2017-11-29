# DoubanGroupSpider

豆瓣租房信息爬虫，配合https://github.com/kong36088/DoubanAdmin 使用
## require

`python>3.5`
`mysql`

## 安装

```bash
pip install scrapy
```

导入`init.sql`到`mysql`

## 使用

```bash
cd DoubanGroup
scrapy crawl title
```

## 配置

配置文件`DoubanGroup/settings.py`

`GROUPS`：抓取的主题id（从你想抓取的豆瓣小组的url上可以查看获取，如：nanshanzufang、szsh）

`CRAW_NUM`：抓取的数量
