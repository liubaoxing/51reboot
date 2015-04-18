job = []
while True:
    action = raw_input('action: ')
    if action == 'add':
        j = raw_input('add job: ')
        if j:
            job.append(j)
            print 'job list now: ',job
        else:
            print 'nothing added to your job list:',job
    elif action == 'do':
        if not job:
            print 'null job list,exit now'
            break
        else:
#            print 'now to do: %s' % job.pop(0)
            print 'now to do: %s' % job.pop()
    else:
        print 'not valid action,continue'
