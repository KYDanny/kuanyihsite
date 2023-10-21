from django import forms
from .models import ChronicalDiseases, Smoking, Chewing, Drinking, Symptoms, Healthcheck, DinnerOption
from django.core.validators import RegexValidator

class Healthform(forms.ModelForm):
    security_number = forms.CharField(max_length=10,
                                      label="身分證字號",
                                      validators=[
                                          RegexValidator(
                                              regex=r'^[a-zA-Z][0-9]{9}$',
                                              message="請輸入正確身分證字號",
                                              code="身分證字號格式錯誤", )
                                      ])
    chronicals = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                queryset=ChronicalDiseases.objects.all(),)
    smokeHabbit = forms.ModelChoiceField(widget=forms.RadioSelect,
                                               queryset=Smoking.objects.all(),)
    betelnutHabbit = forms.ModelChoiceField(widget=forms.RadioSelect,
                                                  queryset=Chewing.objects.all(),)
    drinkingHabbit = forms.ModelChoiceField(widget=forms.RadioSelect,
                                            queryset=Drinking.objects.all(),)
    selfSymptoms = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                  queryset=Symptoms.objects.all(),)
    class Meta:
        model = Healthcheck
        fields = "__all__"
        labels = {
            "name":"姓名",
            "gender":"性別",
            "security_number":"身分證字號",
            "birthday":"出生日期",
            "hire_date":"受僱日期",
            "check_date":"檢查日期",
            "formerJob":"曾經從事",
            "formerJob_start":"起始日期",
            "formerJob_end":"結束日期",
            "currentJob":"目前從事",
            "currentJob_start":"起始日期",
            "currentJob_end":"結束日期",
            "workHourLastMonth":"過去1個月，平均每週工時為",
            "workHourLastSixMonth":"過去6個月，平均每週工時為",
            "doctor":"醫師//醫院名",
        }
        widgets = {
            "birthday":forms.DateInput(attrs={"type":"date"}),
            "hire_date":forms.DateInput(attrs={"type":"date"}),
            "check_date":forms.DateInput(attrs={"type":"date"}),
            "formerJob_start":forms.DateInput(attrs={"type":"date"}),
            "formerJob_end":forms.DateInput(attrs={"type":"date"}),
            "currentJob_start":forms.DateInput(attrs={"type":"date"}),
            "currentJob_end":forms.DateInput(attrs={"type":"date"}),
            "detail":forms.Textarea(attrs={"rows":10, "cols":100}),
            "familyHistory":forms.Textarea(attrs={"rows":10, "cols":100}),
        }

