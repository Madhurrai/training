def frequency_distribution(data):
    dist = {}
    for x in data:
        if(dist.get(x)):
            dist[x]+=1
        else:
            dist[x]=1
    return dist

def plot_histogram(freq_dist, design = '+++ ', align=False, show_values = True):
    max_align_spacing = 0
    output = ''
    if(align):
        max_align_spacing = max(freq_dist.values())
    for key, value in freq_dist.items():
        output += f'{key} | {design * value}'
        if(show_values):
            output += f'{value}'.rjust((max_align_spacing-value)*len(design)+1)
        output+='\n'
    return output

f_dist = frequency_distribution( [2,2,9,1,2,2,1,4,2,2,3,1])
print(plot_histogram(f_dist, align=True, show_values=False, design='xxxx '))