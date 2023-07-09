from krita import Krita, Extension
from PyQt5.QtWidgets import QWidget, QListView
from PyQt5.QtCore import pyqtSlot, QModelIndex
from PyQt5.QtGui import QIcon

class StoryboardTimelineSelector(Extension):
    _storyboardSceneView = None

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        Krita.instance().notifier().windowCreated.connect(self._kritaNotifier_on_windowCreated)

    def cleanup(self):
        if self._storyboardSceneView:
            self._storyboardSceneView.clicked.disconnect(self._storyboardListItem_on_clicked)
            self._storyboardSceneView = None

    @pyqtSlot()
    def _kritaNotifier_on_windowCreated(self):
        storyboardDocker = next((docker for docker in Krita.instance().dockers() if docker.objectName() == "StoryboardDocker"), None)
        if storyboardDocker is not None:
            wdgStoryboardDock = storyboardDocker.findChild(QWidget, "WdgStoryboardDock")
            if wdgStoryboardDock is not None:
                self._storyboardSceneView = wdgStoryboardDock.findChild(QListView, "sceneView")
                if self._storyboardSceneView is not None:
                    self._storyboardSceneView.clicked.connect(self._storyboardListItem_on_clicked)
                    return
        window = Krita.instance().activeWindow()
        if window is not None:
            view = window.activeView()
            if view is not None:
                view.showFloatingMessage("Storyboard Timeline Selector can not find storyboard list object.", QIcon(), 10000, 1)
        

    def createActions(self, window):
        pass

    @pyqtSlot(QModelIndex)
    def _storyboardListItem_on_clicked(self, index):
        index_parent = index.parent()
        if index_parent.isValid():
            index = index_parent
        model = index.model()
        storyFirstFrame = model.index(0, 0, index).data()
        # storyName = model.index(1, 0, index).data()
        storySeconds = model.index(2, 0, index).data()
        storyExtraFrames = model.index(3, 0, index).data()
        document = Krita.instance().activeDocument()
        document.setFullClipRangeStartTime(storyFirstFrame)
        document.setFullClipRangeEndTime(storyFirstFrame + \
            storySeconds * document.framesPerSecond() + storyExtraFrames - 1)

Krita.instance().addExtension(StoryboardTimelineSelector(Krita.instance()))
