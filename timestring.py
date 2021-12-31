class Solution:
    def __init__(self, time: str):
        self.time = time

    def min_in_btw(self):
        times = self.time.partition('-')
        start = times[0]
        stop = times[2]
        if start[-2:] == 'am' and stop[-2:] == 'am' and stop[:2] != '12':
            if start[:-5] == '12':
                start = '00' + start[-5:-2]
            else:
                start = start[:-2]
            stop = stop[:-2]
        elif start[-2:] == 'am' and stop[-2:] == 'am' and stop[:2] == '12':
            if start[:-5] == '12':
                start = '00' + start[-5:-2]
            else:
                start = start[:-2]
            stop = '24' + stop[-5:-2]
        elif start[-2:] == 'am' and stop[-2:] == 'pm' and stop[:2] != '12':
            if start[:-5] == '12':
                start = '00' + start[-5:-2]
            l = stop.partition(':')
            stop = str(int(l[0]) + 12) + l[1] + stop[-4:-2]
        elif start[-2:] == 'am' and stop[-2:] == 'pm' and stop[:2] == '12':
            if start[:-5] == '12':
                start = '00' + start[-5:-2]
            stop = stop[:-2]
        elif start[-2:] == 'pm' and stop[-2:] == 'am':
            start = start[:-2]
            k = stop.partition(':')
            stop = str(int(k[0]) + 12) + k[1] + stop[-4:-2]
        else:
            start = start[:-2]
            stop = stop[:-2]


        h1 = start.partition(':')
        h2 = stop.partition(':')
        hour1 = h1[0]
        hour2 = h2[0]
        delta_h = (int(hour1) - int(hour2)) * 60
        min1 = h1[2]
        min2 = h2[2]
        delta_m = int(min1) + int(min2)
        return abs(delta_h) + delta_m


time_string = str(input())
answer = Solution(time_string)
print(answer.min_in_btw())
