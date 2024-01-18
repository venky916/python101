def g_hour(cor_time,sec_gain,min_ear_reac):
    time=''
    for i in range(2):
        if int(cor_time[i])!=0:
            time+=cor_time[i]
    print(time)
    time=int(time)
    sec_gain_for_1hour=(sec_gain//5)
    hour_diff=sec_gain_for_1hour*min_ear_reac
    result= (hour_diff+time)%24
    return result

print(g_hour('0600',5,10))