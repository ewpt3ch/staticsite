from os import path, mkdir, listdir
from shutil import rmtree, copy
from gencontent import gen_page_recurse

#define paths
public = 'public'
static = 'static'
content = 'content'
template_path = './template.html'

# remove all exisiting files in public dir
if path.exists(public):
    rmtree(public)

# recreate public and copy everything in static to public
mkdir(public) # normally would want to error check and exit if fails

def copystatic(srcpath, destpath):
    tree = listdir(srcpath)
    print(tree)
    for item in tree:
        print(item)
        if path.isfile(path.join(srcpath, item)):
            copy(path.join(srcpath, item), destpath)
        else:
            mkdir(path.join(destpath, item))
            copystatic(path.join(srcpath, item), path.join(destpath, item))


def main():
    copystatic(static, public)
    print("Generating Page")
    gen_page_recurse(
            content,
            template_path,
            public
    )
    

if __name__ == "__main__":
    main()
