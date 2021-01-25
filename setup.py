from setuptools import setup

setup(
    name="APRG",
    version = "0",
    options = {
        'build_apps': {
            'include_patterns': [
                '**/*.bam',
            ],
            'gui_apps': {
                'APRG': 'main.py',
            },
            'plugins': [
                'pandagl',
                'p3openal_audio',
                ],
                'platforms': [
                    'win_amd64'
                ],
        }
    }
)
