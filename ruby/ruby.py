#!/usr/bin/env python3
"""
Author: Marcell Barsony
Date  : June 2023
Desc  : Ruby setup
"""


class Ruby():

    """
    Docstring for Ruby lang
    https://wiki.archlinux.org/title/ruby
    """

    @staticmethod
    def install():
        print('[TODO] Ruby install')
            #cmd = 'sudo pacman -S ruby rubygems'
            #try:
            #    subprocess.run(cmd, shell=True, check=True)
            #    logger.info('Ruby install')
            #except Exception as err:
            #    logger.error(f'Ruby install {err}')
            #    sys.exit(1)
        pass

    @staticmethod
    def gems():
        print('[TODO] Ruby gems')
            # cd ${HOME}/.local/git/blog
            # gem update
            # gem install jekyll bundler
            # bundle update
            # cd ${HOME}
        pass


if __name__ == '__main__':
    r = Ruby()
    r.install()
    r.gems()
