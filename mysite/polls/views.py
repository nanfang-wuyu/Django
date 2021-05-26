from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, JsonResponse
from .models import Question, Test, Filters
from django.template import loader
from django.shortcuts import render
import json


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


"""
Graphic type, 0,1,2,3, each refers to red, green, blue, red and green.
"""


def getTestGraphics(request, graphicType):
    path = r""
    with open(path, 'rb') as f:
        img = f.read()
    return HttpResponse(img, content_type='image/png')


"""
degrees: 测试程度，数组长度为3，其中idx为0 1 2 分别是 红 绿 蓝，根据当前测试程度赋值，
红色盲仅赋值degrees[0],以此类推
testType: 测试类型，0-红色盲，1-绿色盲，2-蓝色盲，3-红绿混合
userId: 用户ID
"""


def storeTestDegree(request):
    userId = request.GET['userId']
    testType = request.GET['testType']
    degrees = request.GET['degrees']
    print(type(degrees))
    degrees = list(degrees.split(","))
    print(type(degrees))
    print(degrees)


    # print(degrees, testType, userId)
    # return HttpResponse("{} {} {}".format(degrees, testType, userId))

    try:
        temp = Test.objects.values().filter(userId=userId, testType=testType)
        if temp:
            temp.update(userId=userId, testType=testType,
                        degreeA=degrees[0], degreeB=degrees[1],
                        degreeC=degrees[2])

            temp = temp[0]
            print(temp)
            print("Update OK")
        else:
            t = Test(userId=userId, testType=testType,
                     degreeA=degrees[0], degreeB=degrees[1],
                     degreeC=degrees[2])
            print("Test created")
            t.save()
            print("Save OK")

    except:
        return HttpResponse("ERROR!")

    return HttpResponse("YES")
    # if request.method == 'POST':
    #     print("the POST method")
    #     concat = request.POST
    #     print(concat)
    #     # print(concat['username'])
    #
    #     postBody = request.body
    #     print(type(postBody))
    #     print(postBody)
    # print(degrees, testType, userId)
    #
    # return HttpResponse("YES!")

def storeTestFilter(t: Test):
    id = t.userId
    type = t.testType

    f = Filters(userId=id, filterType=type)

def getDefaultParams(request):

    # search for default params in database
    # return these data in array

    user_filter = [[2, 2], [3, 3]]
    data = {"arr": user_filter}
    return JsonResponse(data)

def getUserFilterParams(request):
    # user_filter = get_object_or_404(Filters, pk=userId)

    userId = request.GET["userId"]
    print(userId)

    try:
        temp = Test.objects.values().filter(userId=userId)
        print(temp)

        if temp:
            temp = list(temp)
            print(temp)
            data = {
                "userFilterParams": temp,
                "message": "OK"
            }

        else:
            data = {
                "userFilterParams": [],
                "message": "Not Match"
            }

        print(data)
        return JsonResponse(data)

    except:
        data = {
            "userFilterParams": [],
            "message": "ERROR"
        }
        return JsonResponse(data)



