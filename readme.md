
### 爬取 **LetPub** 专业词汇，[词汇表链接](https://www.letpub.com.cn/index.php?page=dict&level1=allfields)
 本仓库中主要包含一下方向专业词汇-- scientific vocabulary：
- 农学  *Agriculture*
- 土壤学 *Soil*
- 大气科学 *Atmosphere*
- 林学 *Forest*
- 神态学 *Ecology*

根据需要可使用voc_spider.py自行下载
## usage

```python
def main():
    baseurl = 'https://www.letpub.com.cn/index.php?page=dict&level1='
    '%E5%9C%B0%E7%90%83%E7%A7%91%E5%AD%A6&level2=%E5%9C%B0%E7%90%86%E5%AD%A6&k=&currentpage='
    max_pages = 971
    output_name = '地理学'
    results = []
    for i in range(1, max_pages + 1):
        url = baseurl + str(i)
        vocs = parser_page(url)
        if vocs is not None:
            res = page_results(vocs)
            results.append(res)
            print("{}/{} completed".format(i, max_pages))
            time.sleep(1.5)
        else:
            pass
    final = pd.concat(results, ignore_index=True)
    final.to_csv(output_name + '.csv', encoding='GB18030', index=None)

```
***
<mark style="background-color：red">参数</mark>
1. url: 目标词汇单的第一页, 直至最后 'currentpage='
2. max_pages : 目标词汇单的最大页数
3. output_name : 输出CSV文件的文件名，建议使用 目标

<mark style="background-color：green">bug</mark>  
偶然会出现页面解析失败的情况


