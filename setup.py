from cream.dist import setup

setup('src/manifest.xml',
    data_files = [
        ('{module_dir}/interface', ['src/interface/youtube-player.svg', 'src/interface/interface.ui']),
        ('{module_dir}', ['src/common.py', 'src/get-stream-url.py', 'src/youtube-player.py', 'src/youtube.py', 'src/buffer.py', 'src/throbberwidget.py', 'src/manifest.xml', 'src/configuration.xml']),
        ]
    )
