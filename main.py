start_time = ''
end_time = ''
date = ''
liveId = ''
accountId = ''

print(
    r'{"param":"{\"queryId\":\"1|66037072|undefined\",\"cubeId\":\"tblive_rpt_abstract_indicator\",\"queryDetail\":false,\"startTime\":\%s\",\"endTime\":\%s\",\"timeType\":2,\"sign\":null,\"limit\":1,\"row\":\"[]\",\"measure\":\"[{\\\"name\\\":\\\"观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"额外奖励流量\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算平均在线时长\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"新增粉丝数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM在线人数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算封面图点击率\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"直播间浏览次数_粉丝占比\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数_粉丝占比\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[%s],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}' % (start_time, end_time, date, liveId, accountId))

'''

{"param":"{\"queryId\":\"1|66037072|undefined\",\"cubeId\":\"tblive_rpt_abstract_indicator\",\"queryDetail\":false,\"startTime\":\"2020-09-10 20:59:36\",\"endTime\":\"2020-09-10 23:58:41\",\"timeType\":2,\"sign\":null,\"limit\":1,\"row\":\"[]\",\"measure\":\"[{\\\"name\\\":\\\"观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"额外奖励流量\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算平均在线时长\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"新增粉丝数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM在线人数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算封面图点击率\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"直播间浏览次数_粉丝占比\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数_粉丝占比\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"20200910\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"279107487542\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[2648620207],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}

'''
