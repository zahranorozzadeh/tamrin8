class time:
    def __init__(self,hr,min,sec) :
        self.h = hr
        self.m = min
        self.s =sec 

    def second_to_time(self):
        result = time(0,0,0) 
        sec=int(input("lotfan saniyeh ra vared konid:"))  
        result.h = sec // 3600
        result.m = sec // 60
        result.s = sec
        print('saniyeh hast:') 
        print(result.h,":",result.m,":",result.s)
        return result

    def time_to_second(self):
        result = self.h*3600 + self.m*60 +self.s
        return result


    def sum(self,other):
        result=time(None,None,None)
        result.h= self.h + other.h
        result.m = self.m + other.m
        result.s = self.s + other.s

        if result.s >= 59:
            result.m+=1
            result.s-=60
        if result.m >=59:
            result.h +=1
            result.m-=60
        return result


    
def subtraction(self,other):   
    result = time(None,None,None) 
    result.h=self.h -other.h
    result.m=self.m-other.m
    result.s=self.s-other.s
    
    if result.s<0:
        result.m-=1
        result.s+=60
    if result.m < 0:
        result.h-=1
        result.m+=60
    return result



    def show(self):
        print(self.h,":",self.m,":",self.s)


while True:
    print('1-jame do zaman')
    print('2-tafrighe do zaman')
    print('3-tabdile saniyeh be zaman')
    print('4- tabdile zaman be saniyeh ')
    print('5-khorog')

    choice = int(input('kodom ro entekhab mikonid?:'))
    if choice == 1:
        hr = int(input("vared kon saat:"))
        m = int(input("vared kon daghighe:"))
        s = int(input("vared kon saniyeh:"))
        a =time(hr,m,s)    
        hr = int(input("vared kon saat:"))
        m = int(input("vared kon daghighe:"))
        s = int(input("vared kon saniyeh:"))
        b =time(hr,m,s)

        #c= sum(a,b)
        print('majmoe in do zaman hast:')
        #print(c['h'],':',c['m'],':',c['s'])
        a.sum(b).show()



    elif choice == 2:
        h = int(input("vared kon saat:"))
        m = int(input("vared kon daghighe:"))
        s = int(input("vared kon saniyeh:"))
        a = time(hr,m,s)

        h= int(input("vared kon saat:"))
        m = int(input("vared kon daghighe:"))
        s = int(input("vared kon saniyeh"))
        b = time(hr,m,s)

       # c= subtraction(a,b)
        print('tafrighe in do zaman hast:')
       # print(c['h'],':',c['m'],':',c['s']) 
        a.subtraction(b).show()

    elif choice == 3:
        c = time(None,None,None)
        a = c.second_to_time()

    elif choice == 4:
        c=time(0,0,0)
        a = c.time_to_second()


    elif choice ==5:
        exit()
    else:
        print('vared koon gozineh sahih ra az meno')



