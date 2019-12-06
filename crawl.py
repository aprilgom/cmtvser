import crawl_linux as comcr


comments = comcr.cr_NaverNewsCmt("https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=215&aid=0000819819&date=20191029&type=1&rankingSeq=2&rankingSectionId=100")
comcr.cr_sele_close()
f = open("comments.txt",'w',-1,"utf-8")
for cmt in comments:
    f.write(cmt+"\n")

f.close()
