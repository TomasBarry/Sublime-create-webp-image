import sublime
import sublime_plugin
import os
import webbrowser

class CreateWebpImageCommand(sublime_plugin.WindowCommand):
    VALID_FILE_EXTENSIONS = [
        'png',
        'jpg',
        'bmp',
        'gif'
    ]

    def __init__(self, window):
        self.variables = window.extract_variables()
        self.settings = sublime.load_settings("CreateWebpImage.sublime-settings")

    def run(self):
        """run

        Create a WebP image for the current image and save it. Optionally, the
        image can also be opened in the browser.

        Given a file at /a/b/c/d/e.png:

            - base_path = /a/b/c/d
            - base_path = e
            - input_file_path = /a/b/c/d/e.png
            - output_file_path = /a/b/c/d/e.webp
            - uri = file:///a/b/c/d/e.web

        The default value of settings:

            - openInBrowser = True
            - browser = 'chrome'
        """
        base_path = self.variables['file_path']
        file_name_without_extension = self.variables['file_base_name']

        input_file_path = self.variables['file']
        output_file_path = "{0}/{1}.webp".format(base_path, file_name_without_extension)

        os.system("cwebp {0} -o {1}".format(input_file_path, output_file_path))

        if self.settings.get('openInBrowser', True) == True:
            uri = 'file://' + output_file_path

            browser = webbrowser.get(self.settings.get('browser', 'chrome'))
            browser.open_new_tab(uri)

        return None

    def is_enabled(self):
        """is_enabled

        The command is enabled when run on files that match those defined
        in the VALID_FILE_EXTENSIONS class variable.

        The current file extension is lowercased in order to ensure that a
        correct equality check occurs (prevent files ending in .PNG from failing
        the check)
        """
        file_extension = self.variables['file_extension']

        return file_extension.lower() in self.VALID_FILE_EXTENSIONS

    def is_visible(self):
        """is_visible

        The command is visible for files that match those defined in the
        VALID_FILE_EXTENSIONS class variable.

        The current file extension is lowercased in order to ensure that a
        correct equality check occurs (prevent files ending in .PNG from failing
        the check)
        """
        file_extension = self.variables['file_extension']

        return file_extension.lower() in self.VALID_FILE_EXTENSIONS

    def description(self):
        return 'Convert a file to the WebP format'

    def input(self, _rest):
        return None
