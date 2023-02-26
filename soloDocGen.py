#! /usr/bin/python3

import re
import sys
import glob
import treelib

import slprint

from typing import Any
from pprint import pprint
from slprint import *
from treelib import Node, Tree
from pathlib import Path

from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QTreeWidget, QWidget
from PySide2.QtCore import QFile, QSortFilterProxyModel, QRegExp, Qt
from PySide2.QtGui import QStandardItemModel, QStandardItem
from ui_mainWindow import Ui_mainWindow


class MainWindow(QWidget):
    textBrowser = None
    def __init__(self, tree, documentation):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.__setupTreeData(tree, documentation)

        self.ui.modelTypesTreeViewer.clicked.connect(self.__setTextData)
        self.ui.lineEdit.textEdited.connect(self.__setFilterRegex)

    def __setupTreeData(self, tree, documentation):
        self.sourceTreeData = QStandardItemModel()
        nodes = tree.children("root")
        for node in nodes:
            self.sourceTreeData.appendRow(self.__buildTreeItem(node, tree, documentation))

        self.treeProxyModel =  QSortFilterProxyModel(self)
        self.treeProxyModel.setSourceModel(self.sourceTreeData)
        self.treeProxyModel.setRecursiveFilteringEnabled(True)
        self.__setFilterRegex("*")

        self.ui.modelTypesTreeViewer.setModel(self.treeProxyModel)

    def __buildTreeItem(self, node, tree, documentation):
        item = QStandardItem(node.tag)
        if node.identifier in documentation:
            item.setData(documentation[node.identifier])
        else:
            item.setData("")
        children = tree.children(node.identifier)
        for row, child in enumerate(children):
            item.setChild(row, self.__buildTreeItem(child, tree, documentation))
        return item

    def __setFilterRegex(self, pattern):
        self.treeProxyModel.setFilterRegExp(QRegExp(pattern, Qt.CaseInsensitive, QRegExp.Wildcard))

    def __setTextData(self, index):
        sourceIndex = self.treeProxyModel.mapToSource(index)
        item = self.sourceTreeData.itemFromIndex(sourceIndex)
        self.ui.textBrowser.setPlainText(item.data())


def buildTreeFromDict(inputDict, root):
    dictCopy = dict(inputDict);
    added = set()
    tree = treelib.Tree()
    tree.create_node(root, root)
    initialSize = len(dictCopy)
    nodeAdded = False
    while dictCopy:
        nodeAdded = False
        for name, parent in dictCopy.items():
            size = len(dictCopy)
            slprint(f"Building tree: ({size} from {initialSize}) ModelType {name}(@{parent})")
            if parent in added:
                tree.create_node(name, name, parent=parent)
                added.add(name)
                dictCopy.pop(name)
                nodeAdded = True
                break
            elif parent is None:
                tree.create_node(name, name, parent=root)
                added.add(name)
                dictCopy.pop(name)
                nodeAdded = True
                break
        if not nodeAdded:
            slprint(f"Building tree: failed to add {size} nodes")
            tree.show()
            break
    if nodeAdded:
        slclear()
    return tree

def getDictFromFolder(folder):
    targetFiles = f"/home/ubuntu/initi/installation/305/core/{folder}/**/*.xxc"
    filesList = glob.glob(targetFiles, recursive=True)

    modelTypeRegexPattern = r"(?P<comment>/\*\*\n( \*[^\n]*\n)* \*/\n)?ModelType[ ]+(?P<name>[\w\d_]+)\((@(?P<parent>[\w\d_]+))?\)"
    modelTypeRegex = re.compile(modelTypeRegexPattern)

    modelTypes = {}
    documentation = {}
    for filePath in filesList:
        slprint(f"Parsing files: {Path(filePath).name}")
        inputFile = open(filePath)
        fileContent = inputFile.read()
        inputFile.close()
        modelTypesData = modelTypeRegex.finditer(fileContent)
        for modelTypeData in modelTypesData:
            modelTypes[modelTypeData.group('name')] = modelTypeData.group('parent')
            if modelTypeData.group('comment'):
                documentation[modelTypeData.group('name')] = modelTypeData.group('comment')

    slclear()
    return modelTypes, documentation

def main():
    folders = "basic", "collectors", "datasources", "modelCatalog"

    modelTypes = {}
    documentation = {}
    for folder in folders:
        folderModelTypes, folderDocumentation = getDictFromFolder(folder)
        modelTypes.update(folderModelTypes)
        documentation.update(folderDocumentation)

    tree = buildTreeFromDict(modelTypes, "root")
    #tree.show()

    app = QApplication(sys.argv)
    window = MainWindow(tree, documentation)
    MainWindow.textBrowser = window.ui.textBrowser

    slstop()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
