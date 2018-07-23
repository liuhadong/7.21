tuple = ('《Give up,hold on to me》收视率是:','《The private dishes of the husbands》收视率是:','《My father-in-lawwil do martiaiarts》收视率是:','《North Canton still believe in love》收视率是:','《Music legend》收视率是:','《Impossible task》收视率是:','《Sparrow》收视率是:','《Distant distance》收视率是:','《Theprodigal son of the new frontier town》收视率是:','《East of dream Avenue》收视率是：')
list = ['1.4%','1.343%','0.92%','0.862%','0.553%','0.411%','0.164%','0.259%','0.394%','0.562%']
list.sort(reverse=True)
for i,b in enumerate (tuple):
    for o,a in enumerate(list):
        if i == o:
            print(tuple[i]+list[o])
