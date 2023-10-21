from django.db import models

class HomePage(models.Model):
    myPhoto = models.ImageField(upload_to="websites/images/")
    header = models.CharField(max_length=100)
    briefIntro = models.CharField(max_length=500)
    companyImage = models.ImageField(upload_to="websites/images/")
    companyName = models.CharField(max_length=50)
    spanOfDate = models.CharField(max_length=50)
    workIntro = models.CharField(max_length=1000)

    def __str__(self):
        return self.header

class ChronicalDiseases(models.Model):
    diseases = models.CharField(max_length=100)
    def __str__(self):
        return self.diseases

class Smoking(models.Model):
    smoke = models.CharField(max_length=100)
    def __str__(self):
        return self.smoke

class Chewing(models.Model):
    chew = models.CharField(max_length=100)
    def __str__(self):
        return self.chew

class Drinking(models.Model):
    drink = models.CharField(max_length=100)
    def __str__(self):
        return self.drink

class Symptoms(models.Model):
    symptom = models.CharField(max_length=200)
    def __str__(self):
        return self.symptom


class Healthcheck(models.Model):
    GENDER_CHOICES = [
        ("男","男"),
        ("女","女"),
    ]

    REASONS = [
        ("新進員工（受僱時）","新進員工（受僱時）"),
        ("定期檢查","定期檢查"),
    ]

    DIAGNOSED = [
        ("是","是"),
        ("否","否"),
    ]
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    security_number = models.CharField(max_length=10, unique=True)
    birthday = models.DateField()
    hire_date = models.DateField(null=True, blank=True)
    check_date = models.DateField()

    formerJob = models.CharField(max_length=200)
    formerJob_start = models.DateField()
    formerJob_end = models.DateField()

    currentJob = models.CharField(max_length=200)
    currentJob_start = models.DateField()
    currentJob_end = models.DateField()
    workHourLastMonth = models.PositiveIntegerField()
    workHourLastSixMonth = models.PositiveIntegerField()

    checkReason = models.CharField(max_length=20, choices=REASONS)

    chronicals = models.ManyToManyField(ChronicalDiseases)
    cancer = models.CharField(max_length=100, null=True, blank=True)
    detail = models.CharField(max_length=500, null=True, blank=True)
    diagnosed = models.CharField(max_length=100, choices=DIAGNOSED, null=True, blank=True)
    doctor = models.CharField(max_length=100, null=True, blank=True)
    familyHistory = models.CharField(max_length=500, null=True, blank=True)

    smokeHabbit = models.ForeignKey(Smoking, on_delete=models.CASCADE)
    smokequantity = models.PositiveIntegerField(null=True, blank=True)
    smokeyears = models.PositiveIntegerField(null=True, blank=True)
    smokequityear = models.PositiveIntegerField(null=True, blank=True)
    smikequitmonth = models.PositiveIntegerField(null=True, blank=True)

    betelnutHabbit = models.ForeignKey(Chewing, on_delete=models.CASCADE)
    chewquantity = models.PositiveIntegerField(null=True, blank=True)
    chewyears = models.PositiveIntegerField(null=True, blank=True)
    chewquityear = models.PositiveIntegerField(null=True, blank=True)
    chewquitmonth = models.PositiveIntegerField(null=True, blank=True)

    drinkingHabbit = models.ForeignKey(Drinking, on_delete=models.CASCADE)
    drinktimes = models.PositiveIntegerField(null=True, blank=True)
    wine = models.CharField(max_length=50, null=True, blank=True)
    drinkquantity = models.PositiveIntegerField(null=True, blank=True)
    drinkquityear = models.PositiveIntegerField(null=True, blank=True)
    drinkquitmonth = models.PositiveIntegerField(null=True, blank=True)

    sleeptime = models.PositiveIntegerField()

    selfSymptoms = models.ManyToManyField(Symptoms)
    othersymptoms = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class DinnerOption(models.Model):
    name = models.CharField(max_length=100)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name










