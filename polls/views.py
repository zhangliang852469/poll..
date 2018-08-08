

# Create your views here.
"""
在我们的投票应用中，我们将建立下面的视图：

问卷“index”页：显示最新的一些问卷
问卷“detail”页面：显示一个问卷的详细文本内容，没有调查结果但是有一个投票或调查表单。
问卷“results”页面：显示某个问卷的投票或调查结果。
投票动作页面：处理针对某个问卷的某个选项的投票动作。

"""

from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        # 按照最近的发布5个问卷
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def index(request):
#     # 按照创建时间的倒序方式 每5个取一次
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     # 然后 返回
#     return HttpResponse(template.render(context, request))
#
# # 问题详情页面:示一个问卷的详细文本内容，没有调查结果但是有一个投票或调查表单。
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# # 投票结果页面:显示某个问卷的投票或调查结果。
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question', question})
#
# # 问卷“index”页：显示最新的一些问卷
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice', None])
    except(KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('polls:results', args=(question_id)))


