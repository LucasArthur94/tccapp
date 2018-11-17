from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Score

# Create your views here.

@login_required
def scores_list(request, rule_id):
    scores = Score.objects.filter(rule__id=rule_id)
    return render(request, 'scores.html', {'scores': scores, 'rule_id': rule_id})
