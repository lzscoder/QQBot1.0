#coding:UTF-8
from qqbot import _bot as bot

def getGroups(bot):
    """返回群的Group类List，以及对应的群名称与下标"""
    groups = bot.List('group')
    glist = []
    i = 0
    group_names = []
    for group in groups:
        glist.append(group)
        group_names.append(group.nick)
        i = i + 1
    return groups,group_names

def getNeedSeedGroupName(fileName):
    """返回文本文件中需要发送信息的群名称"""
    willSendMessageGroups = []
    f = open("qq.txt")
    line = f.readline() 
    while line:   
        if line!='\n':
            line = line.strip('\n')
            willSendMessageGroups.append(line)
        line = f.readline() 
    return willSendMessageGroups

def SendMessage(willSendMessageGroups,groups,group_names,str):
    """开始发送信息"""
    
    for willSendMessageGroup in willSendMessageGroups:
        #需要循环跑一遍，因为有很多名称相同的群
        index = 0
        for group_name in group_names:
            if group_name == willSendMessageGroup:
                bg=bot.List('group',group_name)
                if bg is not None:
                    bot.SendTo(bg[0],str)
            index += 1
                
def getMessage(fileName):
    """从文件中获取要转发的消息"""
    f = open(fileName) 
    line = f.readline()
    str = ''
    while line:  
        str += line
        line = f.readline()  
    return str
        
if __name__=='__main__':

    bot.Login(['-q', '1655505348'])
    willSendMessageGroups = getNeedSeedGroupName('qq.txt')
    groups,group_names = getGroups(bot)
    str = getMessage('message.txt')
    SendMessage(willSendMessageGroups,groups,group_names,str)
