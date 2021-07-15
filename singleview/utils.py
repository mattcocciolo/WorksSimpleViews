from singleview.models import MusicalWorks


def refactor(request, data_list):
    update = MusicalWorks.objects.get(title=data_list[0])
    if data_list[0]:
        update.title = data_list[0]
        if update.contributors != data_list[1]:
            update.contributors = data_list[1] + '|' + update.contributors
            remove_rep = update.contributors.split('|')
            no_rep = []
            for i in remove_rep:
                if i not in no_rep:
                    no_rep.append(i)
                    no_rep_to_string = "".join(str(contrib + '|') for contrib in no_rep)
                    final_contributors = no_rep_to_string.rstrip(no_rep_to_string[-1])
            update.contributors = final_contributors
        update.save()
    return request, data_list
