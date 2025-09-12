from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html') 

def movies_info(request):
    head_msg='moves information'
    sub_msg1='MAD Square is very good movie'
    sub_msg2='OG will come very soon'
    sub_msg3='planning for aashiqui3 with mahesh'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sun_msg':sub_msg3} 
    return render(request,'testapp/index.html',my_dict)

def sport_info(request):
    head_msg='sport information'
    sub_msg1='present IPL is going on'
    sub_msg2='yesterday RCB won the match'
    sub_msg3='today match was between KKR & LSG'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3}
    return render(request,'testapp/index.html',my_dict) 

def politics_info(request):
    head_msg='politics infromation'
    sub_msg1='india pm is modi ji'
    sub_msg2='ap cm was chandra babu'
    sub_msg3='ap sub cm was pavan kalyan'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3}
    return render(request,'testapp/index.html',my_dict)
