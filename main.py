from PIDTurner import PIDTurner
from SamplePID import SamplePID
from XtarkPID import XtarkPID


# pid = SamplePID()
pid = XtarkPID()
P_T = PIDTurner(pid)
P_T.run()
