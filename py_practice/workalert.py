#coding=utf-8

import time
import datetime
import requests
import logging


def getLastWorkday():
    today = datetime.datetime.now()
    if today.weekday() == 0:
        lastWorkday = today + datetime.timedelta(days=-3)
    else:
        lastWorkday = today + datetime.timedelta(days=-1)
    return lastWorkday.strftime('%Y-%m-%d')


class WorkTime(object):
    # """打卡工时计算基础类"""
    def __init__(self, *args):
        timeList = []
        for timeValue in args:
            timetuple = self.convertTime(timeValue)
            timeList.append(timetuple)
        self.timeList = timeList

    def convertTime(self, timestring):
        # "将时间转换成可用于计算的datetime"
        timetuple = datetime.datetime.strptime(timestring, "%Y-%m-%d %H:%M:%S.0")
        try:
            timetuple = datetime.datetime.strptime(timestring, "%Y-%m-%d %H:%M:%S.0")
        except Exception, e:
            raise ValueError("Only support format %Y-%m-%d %H:%M:%S.0")
        return timetuple

    def _startTime(self):
        # print self.timeList
        return min(self.timeList)

    def _endTime(self):
        return max(self.timeList)

    @property
    def startTime(self):
        if self.timeList:
            return self._startTime().strftime('%Y-%m-%d %H:%M:%S')
        return ""

    @property
    def endTime(self):
        if self.timeList:
            return self._endTime().strftime('%Y-%m-%d %H:%M:%S')
        return ""
        
    def _duration(self):
        return self._endTime() - self._startTime()

    def duration(self):
        return (self._duration().seconds)/3600.0

class WorkAlert(WorkTime):
    """docstring for ClassName"""
    def __init__(self, *args):
        super(WorkAlert, self).__init__(*args)
        self.yesterdaySet = self.workSetList()
        
    def workSetList(self):
        yesterday = getLastWorkday()
        recordList = ["09:00:00","09:30:00","18:30:00","19:00:00"]
        recordTimeList = []
        for x in recordList:
            d=datetime.datetime.strptime(yesterday + " " + x,'%Y-%m-%d %H:%M:%S')
            recordTimeList.append(d)
        return recordTimeList

    def alert(self):
        recordTimeList = self.yesterdaySet
        if not self.timeList:
            logging.info("no da car !!")
            return 4
        if self._startTime() > recordTimeList[1]:
            logging.info("shang ban wei da")
            return 3
        elif self._endTime() < recordTimeList[2]:
            logging.info("xia ban wei da")
            return 2
        elif self.duration() < 9.5:
            logging.info("shi chang bu gou")
            return 1
        else:
            logging.info( "normal")
            return 0

class OtcWorkAlert(WorkAlert):
    def calcStartTime(self):
        actTime = self._startTime()
        comTime1 = actTime.replace(hour=9, minute=0, second=0, microsecond=0)
        comTime2 = actTime.replace(hour=9, minute=30, second=0, microsecond=0)
        if actTime < comTime1:
            actTime = comTime1
        elif actTime < comTime2:
            actTime = comTime2
        return actTime

    def calcEndTime(self):
        actTime = self._endTime()
        comTime1 = actTime.replace(hour=19, minute=0, second=0, microsecond=0)
        comTime2 = actTime.replace(hour=18, minute=30, second=0, microsecond=0)
        if actTime > comTime1:
            actTime = comTime1
        elif actTime > comTime2:
            actTime = comTime2
        return actTime

    def calcDuration(self):
        actDuration = self.calcEndTime()-self.calcStartTime()
        sleepStartTime = self.calcStartTime().replace(hour=12, minute=0, second=0, microsecond=0)
        sleepEndTime = self.calcEndTime().replace(hour=13, minute=30, second=0, microsecond=0)
        sleepTime = None
        if (self.calcStartTime() >= sleepStartTime and self.calcStartTime() <= sleepEndTime and self.calcEndTime() >= sleepEndTime):
            sleepTime = sleepEndTime - self.calcStartTime()
        elif (self.calcEndTime() >= sleepStartTime and self.calcEndTime() <= sleepEndTime and self.calcStartTime() <= sleepStartTime):
            sleepTime = self.calcEndTime() - sleepStartTime
        elif (self.calcStartTime() >= sleepStartTime and self.calcStartTime() <= sleepEndTime) and (self.calcEndTime() >= sleepStartTime and self.calcEndTime() <= sleepEndTime):
            sleepTime = self.calcEndTime() - self.calcStartTime()
        elif (self.calcStartTime() <= sleepStartTime and self.calcEndTime() >= sleepEndTime):
            sleepTime = sleepEndTime - sleepStartTime
        if sleepTime:
            return (actDuration - sleepTime).seconds/3600.0
        return actDuration

    def alert(self):
        lastAlert = super(OtcWorkAlert, self).alert()
        if lastAlert == 0:
            if self.calcDuration() < 8:
                return 1
        return lastAlert


def getRecord(userId, date):
    url = "http://jiecaob.szzbmy.com/sign/getRecord?userId="
    sess = requests.session()
    resp = sess.get(url + userId)
    myJson = resp.json()
    # print myJson
    yesterdayTime = []
    for timesit in myJson.get('data', []):
        if date in timesit:
            yesterdayTime.append(timesit)
    return yesterdayTime

if __name__ == '__main__':
    lastWorkday = getLastWorkday()
    recodeInfo = getRecord("2016218", lastWorkday)
    print recodeInfo
    # job = WorkAlert(*recodeInfo)
    job = OtcWorkAlert(*recodeInfo)
    print job.alert()
