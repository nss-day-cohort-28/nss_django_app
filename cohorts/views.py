from django.shortcuts import render, get_object_or_404

from .models import Cohort, Student


def index(request):
    cohort_list = Cohort.objects.all()
    context = { 'cohort_list': cohort_list}
    return render(request, 'cohorts/index.html', context)

def detail(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    # select * from cohort c
    # where c.id = cohort_id
    student_list = Student.objects.filter(cohort_id=cohort_id)
    # select * from cohort c
    # join student s on c.id = s.cohort_id
    context = { 'cohort': cohort, 'student_list': student_list}
    return render(request, 'cohorts/detail.html', context)