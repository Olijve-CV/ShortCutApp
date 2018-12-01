#-*-coding:utf-8-*-

class CConfigOper(object):

    def __init__(self, oConf):
        self.oConf = oConf

    def GetConfig(self, key, default = None):
        return self.oConf.get(key, default)

    @property
    def Name(self):
        return self.GetConfig("Name")

    @property
    def Tip(self):
        return self.GetConfig("Tip")

    @property
    def Geometry(self):
        return self.GetConfig("Geometry")

    @property
    def BgColor(self):
        return self.GetConfig("BgColor")

    @property
    def TextColor(self):
        return self.GetConfig("TextColor")
