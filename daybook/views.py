from django.shortcuts import render, redirect
from .forms import MemoForm


# Create your views here.
def daybook_list(request):
    # memos = Memo.objects.all()  # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'daybook/daybook_list.html')


def daybook_new(request):
    # memos = Memo.objects.all()  # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return redirect('daybook_list')
    else:
        form = MemoForm()
    return render(request, 'daybook/daybook_edit.html', {'form': form})

    # if request.method == "POST":
    #     form = MemoForm(request.POST)
    #     if form.is_valid():
    #         memo = form.save(commit=False)
    #         # post.author = request.user
    #         # post.published_date = timezone.now()
    #         memo.save()
    #         return redirect('docx_detail', pk=memo.pk)
    # else:
    #     form = MemoForm()
# return render(request, 'docx/docx_edit.html', {'form': form})