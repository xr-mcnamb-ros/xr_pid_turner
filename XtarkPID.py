import XMiddleWare as xmw

from SamplePID import SamplePID


robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)
robot.Init()

class XtarkPID(SamplePID):
    def setPID(self, p: int, i: int, d: int) -> None:
        super().setPID(p, i, d)

        robot.SetPID(p,i,d)


if __name__ == "__main__":
    XtarkPID().setPID(0,0,0)

