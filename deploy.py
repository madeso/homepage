#!/usr/bin/env python3
import os
import subprocess
import re
import datetime

d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
gitmessage = 'Rebuilding site {0}'.format(d)

rebegin = [
    re.compile(r'<pre')
]
reend = [
    re.compile(r'</pre')
]

cwd = os.getcwd()
public = os.path.join(cwd, 'public')
content = os.path.join(cwd, 'content')

def filesin(top, ext=None):
    ret = []
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            f = os.path.join(root, name)
            add = True
            if ext is not None:
                e = os.path.splitext(f)[1]
                if e != ext:
                    add = False
            if add:
                ret.append(f)
    return ret

def call(args, cwd):
    p = subprocess.Popen(args, cwd=cwd, universal_newlines=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()

print('Deploying updates to GitHub...')

if len(call(['git', 'status', '-s'], cwd)) > 0:
    print('The working directory is dirty. Please commit any pending changes.')
    exit(-1)

print('Generating public files')
call('hugo', cwd)

print('Cleaning up public files')
publichtml = filesin(public, '.html')
for path in publichtml:
    html = []
    with open(path, 'r') as f:
        inside = 0
        for line in f:
            for r in rebegin:
                inside += len(r.findall(line))
            for r in reend:
                inside -= len(r.findall(line))
            if inside <=0:
                if not line.isspace():
                    html.append(line)
            else:
                html.append(line)
    with open(path, 'w') as f:
        f.write("".join(html))
    # call(['tidy', '-m', '-utf8', '-i', path], cwd)

print('Adding files to git')
call(['git', 'add', '-A'], public)

print('Comming files to git')
call(['git', 'commit', '-m', gitmessage], public)

print('Pushing files to origin')
call(['git', 'push', 'origin', 'master'], public)

print('Adding push to local')
call(['git', 'add', '-A'], cwd)

print('Commiting push')
call(['git', 'commit', '-m', gitmessage], cwd)

print('Done')
