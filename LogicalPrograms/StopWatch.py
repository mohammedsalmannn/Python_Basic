'''
* @Author: Mohammed Salman
* @Date: 2021-11-10 5:02:15
* @Last Modified by:   Uthsavi KP
* @Last Modified time:  2021-11-10 5:02:15
* @Title :  Stopwatch Program for measuring the time that elapses between the start and end clicks
'''
def stopWatch():
    from timeit import default_timer as timer
    from datetime import timedelta
    start_watch=int(input("Enter To Start The Watch:"))
    end_watch=int(input("Enter To Stop The Watch:"))
    start_watch=timer()
    end_watch=timer()
    print("Elapsed Time In Seconds:")
    print(timedelta(end_watch - start_watch))
stopWatch()