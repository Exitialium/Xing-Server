from django.shortcuts import render, HttpResponse
import PIL
import numpy as np
import timeit
import ast
import os
import pickle

class Tasks:
    intputimg=None#np.random.randint(0,255,(512,512,3),np.uint8)
    steps=0
    cfg=0
    intensity=0
    count=0
    outputimg=None
    
def requestAI(request):
    Tasks.count+=1
    return HttpResponse("taken "+str(Tasks.count)+" current time is: "+str(timeit.default_timer())+"s")
    data=request.body

    shape=(512,512,3)
    Tasks.steps=int(data[:2])
    Tasks.intensity=float(data[3:6])
    Tasks.cfg=float(data[7:11])



    Tasks.intputimg=np.frombuffer(data[11:11+shape[0]*shape[1]*shape[2]],dtype=np.uint8).reshape(shape)
    print("task taken")

def recordFile(request):
    data=request.body
    dict=ast.literal_eval(data.decode())
    #write the dict in to a new pickle file
    with open('record.pkl','wb') as f:
        pickle.dump(dict,f)

    #with open('record.pkl','rb') as f:
        #print(pickle.load(f))

    
    return HttpResponse("success")

def retrieveAI(request):
    return HttpResponse("success")
    if Tasks.outputimg is not None:
        data=Tasks.outputimg
        Tasks.outputimg=None
        print("work sent")
        return HttpResponse(data)
    return HttpResponse("task not Done")


def requestWork(request):
    return HttpResponse("success")
    if request.body==b'work':
        if Tasks.intputimg is not None:
            returndata=(b"work"+\
                bytes((2,0,2,0))+Tasks.intputimg.tobytes()+\
                (str(Tasks.steps)+str(Tasks.intensity)+\
                str(Tasks.cfg)).encode()+\

                    
                b"neco girl")
            
            Tasks.intputimg=None
            return HttpResponse(returndata)
        Tasks.intputimg=None#有问题,但是先不管
        return HttpResponse("no task")

def uploadWork(request):
    return HttpResponse("success")
    Tasks.outputimg=request.body
    print("work received")
    return HttpResponse("success")


def test(request):
    return HttpResponse("success")
    #img=cv2.imread('Xing/app01/static/img/download.jfif',cv2.IMREAD_UNCHANGED)
    data=request.body
    shape=tuple(data[:3])
    imgreceived=np.copy(np.frombuffer(data[3:],dtype=np.uint8).reshape(shape))
    imgreceived[:10,:10]=0
    print(11111)
    return HttpResponse(bytes(imgreceived.shape)+imgreceived.tobytes())

def renderTest(request):
    return render(request,'user_list.html')

def check(request):
    return HttpResponse("check")
# Create your views here.
