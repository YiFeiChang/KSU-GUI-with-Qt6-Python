import os
import sys

# 匯入 PyQt6 所需模組
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar
)

# 取得目前檔案的資料夾路徑，方便載入圖示等資源
basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")  # 設定視窗標題

        label = QLabel("My App")  # 建立中央顯示的標籤元件
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 置中對齊
        self.setCentralWidget(label)  # 設定為主視窗的中央元件

        # 建立工具列
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))  # 設定圖示大小
        self.addToolBar(toolbar)  # 加到主視窗

        # 建立第一個工具列按鈕動作
        button_action = QAction(
            QIcon(os.path.join(basedir, "bug.png")),  # 圖示
            "&Your button",  # 按鈕文字 (有快捷鍵提示)
            self
        )
        button_action.setStatusTip("This is your button")  # 滑鼠提示文字
        button_action.triggered.connect(self.onMyToolBarButtonClick)  # 點擊事件綁定
        button_action.setCheckable(True)  # 可切換開關狀態
        button_action.setShortcut(QKeySequence("Ctrl+p"))  # 快捷鍵
        toolbar.addAction(button_action)  # 加到工具列

        toolbar.addSeparator()  # 加分隔線

        # 建立第二個工具列按鈕動作
        button_action2 = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "&Your button2",
            self
        )
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        # 加入額外元件到工具列
        toolbar.addWidget(QLabel("Hello"))  # 加入文字
        toolbar.addWidget(QCheckBox())      # 加入勾選框

        self.setStatusBar(QStatusBar(self))  # 設定狀態列

        # 建立選單列
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")  # 建立 File 選單
        file_menu.addAction(button_action)  # 加入第一個按鈕動作

        file_menu.addSeparator()  # 加入分隔線

        # 建立子選單
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)  # 加入第二個按鈕動作

    # 工具列按鈕的事件處理函式
    def onMyToolBarButtonClick(self, is_checked):
        print("click", is_checked)


# 建立應用程式實例
app = QApplication(sys.argv)

# 建立主視窗實例並顯示
window = MainWindow()
window.show()

# 進入主事件迴圈
app.exec()