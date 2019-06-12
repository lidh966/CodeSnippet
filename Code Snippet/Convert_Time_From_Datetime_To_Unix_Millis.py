from datetime import datetime

def unix_time_millis(dt):
    """return [int] unix millis time
    dt [timestamp]
    """
    epoch = datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * 1000)

if __name__ == '__main__':
    dt = datetime(1971, 1, 1, 0, 0)
    millis = unix_time_millis(dt)
    print(millis)