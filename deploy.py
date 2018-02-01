#!/usr/bin/env python3
import os
import subprocess
import re
import datetime
import argparse
from PIL import Image

########################################################################################################################
# Global contants

d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
gitmessage = 'Rebuilding site {0}'.format(d)

cwd = os.getcwd()
public = os.path.join(cwd, 'public')
content = os.path.join(cwd, 'content')

########################################################################################################################
# Deploy


def generate_progressive(root, ext):
    size = (15, 15)
    imgs = filesin(root, ext)
    for path in imgs:
        f,e = os.path.splitext(path)
        newpath = '{0}_progressive{1}'.format(f,e)
        if os.path.exists(newpath):
            pass
        elif f.endswith('_progressive'):
            pass
        else:
            img = Image.open(path)
            img = img.resize(size)
            img.save(newpath)


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


def clean_html_files(public):
    rebegin = [
        re.compile(r'<pre')
    ]
    reend = [
        re.compile(r'</pre')
    ]

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
                if inside <= 0:
                    if not line.isspace():
                        html.append(line)
                else:
                    html.append(line)
        with open(path, 'w') as f:
            f.write("".join(html))
            # call(['tidy', '-m', '-utf8', '-i', path], cwd)


def generate_public():
    global cwd
    global public
    print('Generating public files')
    call('hugo', cwd)

    print('Cleaning up public html files')
    clean_html_files(public)


def update_github_repo():
    global public
    global gitmessage

    print('Adding generated files to github.io repo')
    call(['git', 'add', '-A'], public)

    print('Comming files to github.io repo')
    call(['git', 'commit', '-m', gitmessage], public)

    print('Pushing files to github.io')
    call(['git', 'push', 'origin', 'master'], public)


def update_homepage_repo():
    global cwd
    global gitmessage

    print('Adding github.io push to homepage repo')
    call(['git', 'add', '-A'], cwd)

    print('Commiting github.io push')
    call(['git', 'commit', '-m', gitmessage], cwd)


def is_repo_clean(cwd):
    if len(call(['git', 'status', '-s'], cwd)) > 0:
        return False
    else:
        return True


def deploy():
    global cwd

    if not is_repo_clean(cwd):
        print('The working directory is dirty. Please commit any pending changes.')
        exit(-1)

    # print('Generating images')
    # generate_progressive(content, '.png')
    # generate_progressive(content, '.jpg')

    print('Deploying updates to GitHub...')

    # generate new copy
    generate_public()

    # update local github.io repo
    update_github_repo()

    # update homepage repo
    update_homepage_repo()

    print('Done')


def dirty_repo_as_string(repo):
    return 'Clean' if is_repo_clean(repo) else 'Dirty'


########################################################################################################################
# Sub commands

def handle_deployment(args):
    deploy()


def handle_info(args):
    global gitmessage
    global cwd
    global public
    global content

    print('Git commit message would be', gitmessage)
    print('Working direction is', cwd, dirty_repo_as_string(cwd))
    print('Public directory is', public, dirty_repo_as_string(public))
    print('Content directory is', content)


def handle_generate_public(args):
    generate_public()


########################################################################################################################
# Main

def main():
    parser = argparse.ArgumentParser(description='Manage my hugo homepage repo')
    sub_parsers = parser.add_subparsers(dest='command_name', title='Commands', help='', metavar='<command>')

    sub = sub_parsers.add_parser('deploy', help='Run whole deploy process')
    sub.set_defaults(func=handle_deployment)

    sub = sub_parsers.add_parser('info', help='Display some paths')
    sub.set_defaults(func=handle_info)

    sub = sub_parsers.add_parser('generate', help='Generate github.io data without publishing')
    sub.set_defaults(func=handle_generate_public)

    args = parser.parse_args()
    if args.command_name is not None:
        args.func(args)
    else:
        parser.print_help()
    print()

########################################################################################################################

if __name__ == "__main__":
    main()
