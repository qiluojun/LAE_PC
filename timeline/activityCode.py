def read_activity(plan):
    lines = plan.splitlines()
    blocks = []
    current_block = []
    plan_show=''
    for line in lines:
        if line.strip() == '':
            if current_block:
                blocks.append(current_block)
                current_block = []
        else:
            current_block.append(line)
    
    if current_block:
        blocks.append(current_block)
    
    activities = {}
    i = 1
    
    for block in blocks:
        paragraphs = block
        activity = {}
        activity['name'] = paragraphs[0]
        plan_show+=activity['name']+'\n'
        activity['address'] = paragraphs[1]
        activity['time'] = paragraphs[2]
        plan_show+=activity['time']+'\n'
        activity['content'] = '\n'.join(paragraphs[3:])
        plan_show+=activity['content']+'\n\n'
        activities['activity{}'.format(i)] = activity
        i += 1

    return activities,plan_show
