import sublime
import sublime_plugin
import os
import subprocess
import urllib.request
import webbrowser

class CreateWebpImageCommand(sublime_plugin.WindowCommand):
    VALID_FILE_EXTENSIONS = [
        'png',
        'jpg',
        'bmp',
        'gif'
    ]

    def run(self):
        """run

        Create a WebP image for the current image and save it. Optionally, the
        image can also be opened in the browser.

        Given a file at /a/b/c/d/e.png:

            - base_path = /a/b/c/d
            - base_path = e
            - input_file_path = /a/b/c/d/e.png
            - output_file_path = /a/b/c/d/e.webp
            - uri = file:/a/b/c/d/e.webp

        The default value of settings:

            - open_in_browser = True
            - browser = 'chrome'
        """
        settings = self.settings()
        variables = self.variables()

        base_path = variables['file_path']
        file_name_without_extension = variables['file_base_name']

        input_file_path = variables['file']
        output_file_path = os.path.join(base_path, file_name_without_extension + '.webp')

        try:
            exit_code = subprocess.call(['cwebp', input_file_path, '-o', output_file_path])
        except OSError as error:
            sublime.error_message('Could not run cwebp, is it installed and on PATH? {0}'.format(error))
            return None

        if exit_code != 0:
            sublime.error_message('cwebp failed with exit code {0}'.format(exit_code))
            return None

        if settings.get('open_in_browser', True) == True:
            uri = 'file:' + urllib.request.pathname2url(output_file_path)

            # We use Chrome as the default browser given that WebP is a format
            # created by Google and not supported by all browsers
            # https://developers.google.com/speed/webp/faq
            #
            # If the user would like to use an alternate browser they can do so
            # by changing the default settings
            browser = webbrowser.get(settings.get('browser', 'chrome'))
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
        file_extension = self.variables().get('file_extension', '')

        return file_extension.lower() in self.VALID_FILE_EXTENSIONS

    def is_visible(self):
        """is_visible

        The command is visible for files that match those defined in the
        VALID_FILE_EXTENSIONS class variable.

        The current file extension is lowercased in order to ensure that a
        correct equality check occurs (prevent files ending in .PNG from failing
        the check)
        """
        file_extension = self.variables().get('file_extension', '')

        return file_extension.lower() in self.VALID_FILE_EXTENSIONS

    def description(self):
        return 'Convert a file to the WebP format'

    def settings(self):
        return sublime.load_settings("CreateWebpImage.sublime-settings")

    def variables(self):
        return self.window.extract_variables()
