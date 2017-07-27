# coding=utf-8
# Must run as administor administrator
# ref 1 (how to change hosts):http://www.jianshu.com/p/2078bfc467b1
# ref 2 (read line from string) : https://docs.python.org/3.5/library/linecache.html
# ref 3 (dateime transfer) : http://www.wklken.me/posts/2015/03/03/python-base-datetime.html#5-huo-qu-liang-ge-datetimede-shi-jian-chai and https://docs.python.org/3/library/datetime.htmls
# ref 4 (json) : http://liuzhijun.iteye.com/blog/1859857



import datetime
from urllib import request
import linecache
import json
import os


lastupdate = r'lastUpdatedRecord.json'
url = r'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
savepath = os.getcwd()
target = r'C:\Windows\System32\drivers\etc\hosts'
tempfile = savepath + r'\temp_hosts'


def downloadHosts(destpath, desturl):
    with request.urlopen(desturl) as f:
        # print(f.status)
        if f.status == 200:
            with open(destpath, 'wb') as fptr:
                fptr.write(f.read())
            line_date = linecache.getline(destpath, 3).split(' ')
            # print(line_date[3])  # 这个是日期，需要与最近一次的更新日期进行比较
            # 获取最近一次的更新
            update = line_date[3].strip('\n')
            jf = open(lastupdate, 'r+')
            json_rd = json.load(jf)
            lastdate = json_rd['lastUpdatedDate']
            print('Update:%s\nCurrent:%s' % (update, lastdate))
            curr = datetime.datetime.strptime(update, '%Y-%m-%d')
            last = datetime.datetime.strptime(lastdate, '%Y-%m-%d')
            if (curr - last).total_seconds() > 0:
                print('Need to update')
                choice = input('Do you want to update hosts?(y/n)')
                if choice.lower() == 'y':
                    try:
                        
                        # 写入hots文件
                        with open(target, 'w') as f:
                            with open(destpath, 'r') as r:
                                f.write(r.read())
                        
                        print('Update %s sucessfully!' % target)
                        # 更新保存的日期
                        jf.seek(0)
                        json_rd['lastUpdatedDate'] = update
                        json.dump(json_rd, jf)
                        jf.close()
                    except WindowsError:
                        print('Might be Persmisssion denied! Please try to run as administrator')
                    except BaseException:
                        print('Some error(s) occured!')
                else:
                    print('user canceled!')
            else:
                print('Not need replace file')
        else:
            print("Download fail")


if __name__ == '__main__':
    downloadHosts(tempfile, url)
    input('Press any key to exit')


