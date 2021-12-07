# CreateWebpImage

A plugin for [Sublime Text](https://www.sublimetext.com/) providing an interface to [CWebP](https://developers.google.com/speed/webp/docs/using).

## Install

You can install via with [Package Control](https://packagecontrol.io/) and restart Sublime.

- **Install Package**: Search with `CreateWebpImage`.
- **Add Repository**: Put URL `https://github.com/TomasBarry/Sublime-create-webp-image`.

### Prerequisites

[CWebP](https://developers.google.com/speed/webp/download)

This can be downloaded and installed by downloading a precompiled version of `libwebp` from the [downloads repository](https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html).

Details on which version to pick (and the macOS packages) can be found [in the official documentation](https://developers.google.com/speed/webp/docs/precompiled).

By following the instructions in the documentation above you will have `cwebp` available to use and you will be able to use it with this Sublime Text package. You can test that you have `cwebp` available by testing some of the [Getting Started instructions](https://developers.google.com/speed/webp/docs/using) from the official documentation.

## Usage

In a PNG, JPG, BMP, or GIF file, open the Command Palette (<kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>P</kbd>) and choose **Convert to WebP**.

## Config

You can configure following options from Preferences → Package Settings → CreateWebpImage → Settings - User.
