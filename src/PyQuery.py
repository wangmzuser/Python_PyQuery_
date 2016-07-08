from pyquery import PyQuery as pyq
import re
from urllib.error import URLError,HTTPError
import urllib.request
import urllib.parse

# hlt = requests.get('http://tieba.baidu.com/f?kw=%B5%D8%CF%C2%B3%C7%D3%EB%D3%C2%CA%BF&fr=ala0&tpl=5')
# f =  open('html.txt','w')
# f.write(hlt.text)
# f.close()

# print(hlt.text)

# doc = pyq(url = 'http://tieba.baidu.com/f?kw=%B5%D8%CF%C2%B3%C7%D3%EB%D3%C2%CA%BF&fr=ala0&tpl=5')
# sun = doc('#pagelet_frs-list/pagelet/thread_list')
# print(sun)
# txt = sun.text()
# txtlist = txt.split(' ')
# for i in txtlist:
#     print(i)
# for i in doc('li'):
#     print(pyq(i).text())
# for i in sum.text():
#     print(i)
# print(doc.html())
# print(doc.attr('title'))

str = """<div id="info">
<span><span class='pl'>导演</span>: <a href="/celebrity/1047989/" rel="v:directedBy">汤姆·提克威</a> / <a href="/celebrity/1161012/" rel="v:directedBy">拉娜·沃卓斯基</a> / <a href="/celebrity/1013899/" rel="v:directedBy">安迪·沃卓斯基</a></span><br/>
<span><span class='pl'>编剧</span>: <a href="/celebrity/1047989/">汤姆·提克威</a> / <a href="/celebrity/1013899/">安迪·沃卓斯基</a> / <a href="/celebrity/1161012/">拉娜·沃卓斯基</a></span><br/>
<span><span class='pl'>主演</span>: <a href="/celebrity/1054450/" rel="v:starring">汤姆·汉克斯</a> / <a href="/celebrity/1054415/" rel="v:starring">哈莉·贝瑞</a> / <a href="/celebrity/1019049/" rel="v:starring">吉姆·布劳德本特</a> / <a href="/celebrity/1040994/" rel="v:starring">雨果·维文</a> / <a href="/celebrity/1053559/" rel="v:starring">吉姆·斯特吉斯</a> / <a href="/celebrity/1057004/" rel="v:starring">裴斗娜</a> / <a href="/celebrity/1025149/" rel="v:starring">本·卫肖</a> / <a href="/celebrity/1049713/" rel="v:starring">詹姆斯·达西</a> / <a href="/celebrity/1027798/" rel="v:starring">周迅</a> / <a href="/celebrity/1019012/" rel="v:starring">凯斯·大卫</a> / <a href="/celebrity/1201851/" rel="v:starring">大卫·吉雅西</a> / <a href="/celebrity/1054392/" rel="v:starring">苏珊·萨兰登</a> / <a href="/celebrity/1003493/" rel="v:starring">休·格兰特</a></span><br/>
<span class="pl">类型:</span> <span property="v:genre">剧情</span> / <span property="v:genre">科幻</span> / <span property="v:genre">悬疑</span><br/>
<span class="pl">官方网站:</span> <a href="http://cloudatlas.warnerbros.com" rel="nofollow" target="_blank">cloudatlas.warnerbros.com</a><br/>
<span class="pl">制片国家/地区:</span> 德国 / 美国 / 香港 / 新加坡<br/>
<span class="pl">语言:</span> 英语<br/>
<span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="2013-01-31(中国大陆)">2013-01-31(中国大陆)</span> / <span property="v:initialReleaseDate" content="2012-10-26(美国)">2012-10-26(美国)</span><br/>
<span class="pl">片长:</span> <span property="v:runtime" content="134">134分钟(中国大陆)</span> / 172分钟(美国)<br/>
<span class="pl">IMDb链接:</span> <a href="http://www.imdb.com/title/tt1371111" target="_blank" rel="nofollow">tt1371111</a><br>
<span class="pl">官方小站:</span>
<a href="http://site.douban.com/202494/" target="_blank">电影《云图》</a>
</div>"""

# doc=pyq(str)

# print(doc.html())

def AnalyHtml(url,filePath):
    if filePath != '':
        pass
    else:

        htl = pyq(url = url)
        htl2 = htl('cc')
        for i in htl2:
            htl3 = pyq(i)
            htl4 = htl3('div')
            if htl4.find('img'):
                # print(htl4)
                print(htl4('img').attr('src'))
            else:
                # print(htl3('div').text())
                pass
def main():
    doc = pyq(filename='html.txt')
    doc1 = doc('div')
    doc2 = doc1('a')
    # print(doc2)
    TieBaDate = {}

    try:
        f = open('source.txt', 'w')
    except IOError:
        print("Error: open file failed.")
    iSum = 0
    for i in doc2:
        tmphref = pyq(i).attr('href')
        tmptitle = pyq(i).attr('title')
        strhref = repr(tmphref)
        strtitle = repr(tmptitle)
        aryhref = re.findall('/p/(\d+)', strhref)

        if re.findall('/p/(\d+)', strhref) != [] and re.findall('(.*?)魔枪(.*?)', strtitle) != []:
            # print(strtitle)
            # print(strhref)
            strsource = 'http://tieba.baidu.com/p/%s' % aryhref[0]
            f.write(strsource)
            f.write("\n")
            iSum += 1
            AnalyHtml(url=strsource, filePath='')
            break

    print('sum :', iSum)
    f.close()

if __name__ == '__main__':
    # main()
    url = 'http://www.baidu.com/s'
    values = {'wd': 'python',
              'opt-webpage': 'on',
              'ie': 'gbk'}
    url_values = urllib.parse.urlencode(values)
    # print(url_values)

    url_values = url_values.encode(encoding='UTF8')
    full_url = urllib.request.Request(url, url_values)
    # or ony one sentense:full_url=url+'?'+url_values

    try:
        response = urllib.request.urlopen(full_url)  # open=urlopen
    except HTTPError as e:
        print('Error code:', e.code)
    except URLError as e:
        print('Reason', e.reason)
    the_page = response.read()
    print(the_page)

