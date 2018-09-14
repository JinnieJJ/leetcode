class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        rList=[0] * n
        startList=[]
        preId = int(logs[0].split(':')[0])
        preKind = logs[0].split(':')[1]
        preTime = int(logs[0].split(':')[2])
        startList.append(preId)
        for i in range(1, len(logs)):
            Id = int(logs[i].split(':')[0])
            Kind = logs[i].split(':')[1]
            Time = int(logs[i].split(':')[2])
            if Kind == 'start':
                startList.append(Id)
                #被抢占，抢占前运行时间
                #Id抢占资源，preId进入等待。这种情况要计算preId等待前已经运行的时间
                if preKind == 'start':
                    rList[preId] += (Time - preTime)
                #被抢占，抢占后运行时间
                #preId结束后到Id开始前，有一段时间，这段时间其实就是startList上最近一个等待的线程在运行的时间，参考实例如下
                #example2:n=2,logs=["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
                #在"0:end:5","1:start:7"期间，有个时间片6，这个时间就是"0:start:0"运行的时间
                else:
                    if len(startList) > 1:
                        rList[startList[-2]] += (Time - preTime - 1)          
            else:
                del startList[-1]
                #没有被抢占的线程运行时间
                #由于是递归调用，所以这种情况下，必有Id=preId，参考实例如下
                #example1:n=1,logs=["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
                #在"0:start:2","0:end:5"，出现一个end，如果前一个是start，则必有Id=preId
                if preKind == 'start':
                    rList[Id] += (Time - preTime + 1)
                #被抢占，抢占后运行时间
                else:
                    rList[Id] += (Time - preTime)
            preId=Id
            preKind=Kind
            preTime=Time
        return rList
