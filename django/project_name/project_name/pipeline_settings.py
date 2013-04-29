PIPELINE_LESS_BINARY = "lessc"

PIPELINE_CSS = {
    'master': {
        'source_filenames': (
          'css/*',
        ),
        'output_filename': 'css/base.css',
    },
}


PIPELINE_JS = {
    'master': {
        'source_filenames': (
          'js/base.js',
        ),
        'output_filename': 'js/base.js',
    }
}
