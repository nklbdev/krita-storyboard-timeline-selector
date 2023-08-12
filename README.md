# Storyboard Timeline Selectior for Krita

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)
[![en](https://img.shields.io/badge/lang-ru-green.svg)](README.ru.md)

**Storyboard Timeline Selector** is a plugin for Krita that selects a range of frames in the timeline when selecting a story.

## Why

Krita has the ability to create "stories" - consecutive ranges of frames
that could be conveniently used to create multiple animations
of the same character in a single file for use as a resource for game engines.
However, in Krita, it is extremely inconvenient to choose
the range of frames that will be played at the moment
(for example, to loop it and see if the running animation looks organic).
To do this, you need to go to the Timeline docker menu
and explicitly specify the start and end frames of the range with numbers.

## How to install

- Clone the repository or download its contents as a ZIP archive.
- Launch Krita.
- In Krita, select the "Settings -> Manage Resources..." menu item.
- In the window that opens, click the "Open Resource Folder" button - a file manager window will open. The "Manage Resources" window can be closed.
- Copy the "pykrita" folder from the repository directory to the Krita resources folder with file replacement.
- Restart Krita (this is necessary for the new plugin to be detected).
- In Krita, select the menu item "Settings -> Configure Krita...".
- In the preferences window, select the "Python Plugin Manager" section.
- Check the box in front of the plugin name "Storyboard Timeline Selector".
- Restart Krita (this is necessary to initialize the selected plugins).

## How to use

When a story is selected with the mouse in the "Storyboard" docker, the frame range of that story is automatically selected on the "Timeline" docker.

<p align="center"><img alt="Screenshot" src="https://user-images.githubusercontent.com/7024016/257639175-980581e4-a8e4-49b3-868c-770bd20c2ce2.png" /></p>

To test this:

- Add a "Storyboard" docker to the Krita interface. To do this, check the box in the "Settings -> Dockers -> Storyboard" menu item.
- Add one or more "stories" in the "Storyboard" docker.
- Draw animation frames for the created "stories".
- Try switching between "stories" by clicking on them with the left mouse button and starting the animation playback.

## Feedback

If you have comments, suggestions, or need to contact me,
send me an email at <a href="mailto:nklbdev@gmail.com">nklbdev@gmail.com</a>
or open an issue at <a href="https://github.com/nklbdev/krita-storyboard-timeline-selectior">GitHub repository</a>
(which is also where you can re-download it in case of need)
