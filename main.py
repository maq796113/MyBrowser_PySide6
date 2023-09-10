from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QApplication


class WebBrowser(QMainWindow):

    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.window.setWindowTitle("CJ's Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.browser.setUrl(QUrl("https://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)

        self.browser.setUrl(QUrl(url))


if __name__ == "__main__":
    app = QApplication([])
    window = WebBrowser()
    app.exec()
