from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def analysed(request):
    li_purpose=[]
    text_input=request.GET.get('text','default')

    analysed_res= ""
    removepunc=request.GET.get('checkRemovePunc','off')
    capitalize=request.GET.get('checkCapitalizeAll','off')
    capitalizeFullstop=request.GET.get('checkCapitalizefullstop','off')
    extraSpaceRemove= request.GET.get('checkExtraSpaceRemove','off')
    if(text_input==""):
        return render(request, 'empty.html')

    if (removepunc=='on'):
        punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        li_purpose.append("Remove Punctuation")
        for char in text_input:
            if char not in punc:
                analysed_res=analysed_res+char
        text_input=analysed_res

    if(capitalize=='on'):
        analysed_res=""
        li_purpose.append("Capitalize All")
        for char in text_input:
            analysed_res=analysed_res+char.upper()
        text_input = analysed_res

    if (capitalizeFullstop=='on'):
        li_purpose.append("Capitalize fullstop")
        c=1
        flag=0
        analysed_res = text_input[0].upper()+""
        for i in range(1, len(text_input)):
            if (flag == 1):
                flag = 0
                continue
            if text_input[i] == '.':
                analysed_res = analysed_res + "." + text_input[i + 1].upper()
                flag = 1
            else:
                analysed_res = analysed_res + text_input[i]
        text_input=analysed_res

    if extraSpaceRemove=='on' :
            li_purpose.append("Extra space Remover")
            analysed_res=""
            for i in range(0,len(text_input)):
                if(text_input[i] == " " and text_input[i+1] == " "):
                    pass;
                else:
                    analysed_res=analysed_res+text_input[i]

    if (extraSpaceRemove=='off' and capitalizeFullstop=='off' and capitalize=='off' and removepunc=='off'):
        return render(request, 'error.html')

    param={'purpose':li_purpose, 'Analysed':analysed_res}
    return render(request,'result.html',param)