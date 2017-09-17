from django.shortcuts import render


# Create your views here.
def daybook_list(request):
    # memos = Memo.objects.all()  # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'daybook/daybook_list.html')


def daybook_new(request):
    # memos = Memo.objects.all()  # Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'daybook/daybook_edit.html')
