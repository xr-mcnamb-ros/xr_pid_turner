from asyncio import sleep
from select import select


from BaseTurner import AbstractTurner
from config import key_dev
from key_num2str_map import key_map


class PIDTurner(AbstractTurner):
    def __init__(self, pid_instance):
        self._p = 300
        self._i = 0
        self._d = 200
        self.max_v = 1000
        self.min_v = 0

        self._pid_instance = pid_instance

        self._hold_count = 0
        self._delta = 1
        self._is_running = False

        self._chek_num = lambda num, max_n, min_n: \
            num if min_n <= num <= max_n else (max_n if num > max_n else min_n)

    def run(self):
        self._is_running = True

        while self._is_running:
            try:
                key = self._analysis()
                if key:
                    self._hold_count += 1
                    self.complete(key)
                else:
                    self._hold_count = 0

            except KeyboardInterrupt:
                self.stop()

            # if hold press,turn delta up.
            if self._hold_count > 30:
                self._delta = 10
                self._hold_count = 32
            else:
                self._delta = 3

            sleep(0.04)

            print("-"*4, "delta: {}".format(self._delta), "-"*4)
            # print("-"*7, "P: {}".format(self._p), "-"*8)
            # print("-"*7, "I: {}".format(self._i), "-"*8)
            # print("-"*7, "D: {}".format(self._d), "-"*8)
            self._pid_instance.showPID()

    def stop(self):
        self._is_running = False

    @staticmethod
    def _analysis() -> str:

        # waiting for IO event
        dev_list, _, _ = select([key_dev], [], [], 0.2)

        for dev in dev_list:
            if dev is key_dev:
                events = dev.read()
                print("-"*20)

                # get keyboard input event
                for env in events:
                    if env.code in key_map and env.type == 0x01:
                        print("-"*9, key_map[env.code], "-"*10)
                        return key_map[env.code]
        return ""

    def complete(self, key):
        if key == 't':
            self._is_running = False
            return None

        elif key == 'q':
            self._p += self._delta
        elif key == 'a':
            self._p -= self._delta

        elif key == 'w':
            self._i += self._delta
        elif key == 's':
            self._i -= self._delta

        elif key == 'e':
            self._d += self._delta
        elif key == 'd':
            self._d -= self._delta

        elif key == 'r':
            self._p = 300
            self._i = 0
            self._d = 200

        self._p = self._chek_num(self._p, self.max_v, self.min_v)
        self._i = self._chek_num(self._i, self.max_v, self.min_v)
        self._d = self._chek_num(self._d, self.max_v, self.min_v)
        self._pid_instance.setPID(self._p, self._i, self._d)


