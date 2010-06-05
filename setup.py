from cream.dist import setup

class NotImplemented(BaseException):
    pass

raise NotImplemented

"""
setup('src/manifest.xml',
    data_files = [
        ('{module_dir}', ['src/hotkey.py', 'src/manifest.xml'])
        ]
    )
"""
