def dzien(r,m,d):
    rm = (-1,0,3,3,6,1,4,6,2,5,0,3,5)
    dt= d + rm[m] + (r-1900)+(r-1900)//4
    if r%4==0 and m < 3:
        dt-=1

    return dt % 7
#end_def
