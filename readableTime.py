def readableTime(seconds):
    hrs=seconds//3600
    mns=(seconds-(hrs*3600))//60
    secs=(seconds-(hrs*3600)-(mns*60))
    
    hrs0, mns0, secs0 = hrs, mns, secs
    
    timeFormat = input('what format would you prefer?\n1. worded\n2. digital\n')

    if len(str(hrs))==1:
        hrs0='0'+str(hrs)
    if len(str(mns))==1:
        mns0='0'+str(mns)
    if len(str(secs))==1:
        secs0='0'+str(secs)

    print(f'{seconds} seconds is:')
    if int(timeFormat) == 1 or timeFormat.lower() == 'w' or timeFormat.lower() == 'worded':
        print(f'{hrs} hours, {mns} minutes and {secs} seconds')
    elif int(timeFormat) == 2 or timeFormat.lower() == 'd' or timeFormat.lower() == 'digital':
        print(f'{hrs0}:{mns0}:{secs0}')

seconds = int(input('enter number of seconds:\n'))
readableTime(seconds)
