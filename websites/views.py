from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .forms import Healthform
from .models import HomePage, Healthcheck, DinnerOption
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import DinnerOptionSerializer


def index(request):
    myinfo = HomePage.objects.all()
    return render(request, "websites/index.html", {"myinfo":myinfo})

def healthcheck(request):
    if request.method == "POST":
        form = Healthform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            today = timezone.now().date()

            birthday = cleaned_data.get("birthday")
            if birthday and birthday > today:
                form.add_error("birthday", "出生日期不能晚於今日")

            hire_date = cleaned_data.get("hire_date")
            if hire_date and hire_date > today:
                form.add_error("hire_date", "受顧日期不能晚於今日")
            if hire_date and hire_date < birthday:
                form.add_error("hire_date", "受顧日期不能早於出生日期")

            check_date = cleaned_data.get("check_date")
            if check_date and check_date > today:
                form.add_error("check_date", "檢查日期不能晚於今日")
            if check_date and check_date < birthday:
                form.add_error("check_date", "檢查日期不能早於出生日期")

            formerJob_start = cleaned_data.get("formerJob_start")
            if formerJob_start and formerJob_start >= today:
                form.add_error("formerJob_start", "先前工作起始日不得等於或晚於今日")
            if formerJob_start and formerJob_start < birthday:
                form.add_error("formerJob_start", "先前工作起始日不得早於出生日期")

            formerJob_end = cleaned_data.get("formerJob_end")
            if formerJob_end and formerJob_end >= today:
                form.add_error("formerJob_end", "先前工作結束日不得等於或晚於今日")
            if formerJob_end and formerJob_end < birthday:
                form.add_error("formerJob_end", "先前工作結束日不得早於出生日期")

            currentJob_start = cleaned_data.get("currentJob_start")
            if currentJob_start and currentJob_start > today:
                form.add_error("currentJob_start", "目前工作起始日期不得晚於今日")
            if currentJob_start and currentJob_start < birthday:
                form.add_error("currentJob_start", "目前工作起始日期不得早於出生日期")

            currentJob_end = cleaned_data.get("currentJob_end")
            if currentJob_end and currentJob_end > today:
                form.add_error("currentJob_end", "目前工作結束日期不得晚於今日")
            if currentJob_end and currentJob_end < birthday:
                form.add_error("currentJob_end", "目前工作結束日期不得早於出生日期")
            if currentJob_end and currentJob_end < currentJob_start:
                form.add_error("currentJob_end", "目前工作結束日期不得早於先前工作結束日期")

            if not form.errors:
                form.save()
                return HttpResponseRedirect(reverse("websites:thanks"))
        else:
            pass
    else:
        form = Healthform()
    return render(request, "websites/healthcheck.html", {"form":form})

def thanks(request):
    showResult = Healthcheck.objects.last()
    print("showResult.smokeHabbit:", showResult.smokeHabbit)
    print("Type of showResult.smokeHabbit:", type(showResult.smokeHabbit))
    print("showResult.smokeHabbit.smoke:", showResult.smokeHabbit.smoke)
    return render(request, "websites/thanks.html", {"showResult":showResult})

class DinnerOptionViewSet(viewsets.ModelViewSet):
    queryset = DinnerOption.objects.all()
    serializer_class = DinnerOptionSerializer

    @action(detail=True, methods=['POST'])
    def vote(self, request, pk=None):
        latest_queryset = DinnerOption.objects.all()
        option = self.get_object()
        option.votes += 1
        option.save()

        serializer = DinnerOptionSerializer(latest_queryset, many=True)

        return Response({'status':'vote counted', 'current_votes':serializer.data}, status=status.HTTP_200_OK)

def dinner(request):
    return render(request, "websites/dinner.html")

def dinner_results(request):
    latest_queryset = DinnerOption.objects.all()
    return render(request, "websites/dinner_result.html", {"options":latest_queryset})




