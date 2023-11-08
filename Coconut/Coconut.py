#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- encoding:UTF-8 -*-
# coding=utf-8
# coding:utf-8

import codecs
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
							 QLabel, QHBoxLayout, QVBoxLayout, QLineEdit,
							 QSystemTrayIcon, QMenu, QDialog, QMenuBar, QFileDialog)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction, QIcon, QColor
import PyQt6.QtGui
import webbrowser
import sys
import subprocess
import signal
from bs4 import BeautifulSoup
import html2text
import urllib3
import logging
import requests
import re
import os
import shutil
from pathlib import Path
import time
from datetime import datetime
import filetype
try:
	from AppKit import NSWorkspace
except ImportError:
	print("can't import AppKit -- maybe you're running python from homebrew?")
	print("try running with /usr/bin/python instead")
	exit(1)


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

BasePath = '/Applications/Coconut.app/Contents/Resources/'
# BasePath = ''  # test

# Create the icon
icon = QIcon(BasePath + "Coconut-logo.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action3 = QAction("🥥 Switch on Coconut!")
action3.setCheckable(True)
menu.addAction(action3)

menu.addSeparator()

action7 = QAction("⚙️ Settings")
menu.addAction(action7)

menu.addSeparator()

action2 = QAction("🆕 Check for Updates")
menu.addAction(action2)

action1 = QAction("ℹ️ About")
menu.addAction(action1)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
btna4 = QAction("&Switch on Coconut!")
sysmenu = QMenuBar()
file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(btna4)


class window_about(QWidget):  # 增加说明页面(About)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 说明页面内信息
		self.setUpMainWindow()
		self.resize(400, 410)
		self.center()
		self.setWindowTitle('About')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widg1 = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'Coconut-logo.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumWidth(100)
		l1.setMaximumHeight(100)
		l1.setScaledContents(True)
		blay1 = QHBoxLayout()
		blay1.setContentsMargins(0, 0, 0, 0)
		blay1.addStretch()
		blay1.addWidget(l1)
		blay1.addStretch()
		widg1.setLayout(blay1)

		widg2 = QWidget()
		lbl0 = QLabel('Coconut', self)
		font = PyQt6.QtGui.QFont()
		font.setFamily("Arial")
		font.setBold(True)
		font.setPointSize(20)
		lbl0.setFont(font)
		blay2 = QHBoxLayout()
		blay2.setContentsMargins(0, 0, 0, 0)
		blay2.addStretch()
		blay2.addWidget(lbl0)
		blay2.addStretch()
		widg2.setLayout(blay2)

		widg3 = QWidget()
		lbl1 = QLabel('Version 1.0.0', self)
		blay3 = QHBoxLayout()
		blay3.setContentsMargins(0, 0, 0, 0)
		blay3.addStretch()
		blay3.addWidget(lbl1)
		blay3.addStretch()
		widg3.setLayout(blay3)

		widg4 = QWidget()
		lbl2 = QLabel('Thanks for your love🤟.', self)
		blay4 = QHBoxLayout()
		blay4.setContentsMargins(0, 0, 0, 0)
		blay4.addStretch()
		blay4.addWidget(lbl2)
		blay4.addStretch()
		widg4.setLayout(blay4)

		widg5 = QWidget()
		lbl3 = QLabel('感谢您的喜爱！', self)
		blay5 = QHBoxLayout()
		blay5.setContentsMargins(0, 0, 0, 0)
		blay5.addStretch()
		blay5.addWidget(lbl3)
		blay5.addStretch()
		widg5.setLayout(blay5)

		widg6 = QWidget()
		lbl4 = QLabel('♥‿♥', self)
		blay6 = QHBoxLayout()
		blay6.setContentsMargins(0, 0, 0, 0)
		blay6.addStretch()
		blay6.addWidget(lbl4)
		blay6.addStretch()
		widg6.setLayout(blay6)

		widg7 = QWidget()
		lbl5 = QLabel('※\(^o^)/※', self)
		blay7 = QHBoxLayout()
		blay7.setContentsMargins(0, 0, 0, 0)
		blay7.addStretch()
		blay7.addWidget(lbl5)
		blay7.addStretch()
		widg7.setLayout(blay7)

		widg8 = QWidget()
		bt1 = QPushButton('The Author', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.intro)
		bt2 = QPushButton('Github Page', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(100)
		bt2.clicked.connect(self.homepage)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg8.setLayout(blay8)

		bt7 = QPushButton('Buy me a cup of coffee☕', self)
		bt7.setMaximumHeight(20)
		bt7.setMinimumWidth(215)
		bt7.clicked.connect(self.coffee)

		widg8_5 = QWidget()
		blay8_5 = QHBoxLayout()
		blay8_5.setContentsMargins(0, 0, 0, 0)
		blay8_5.addStretch()
		blay8_5.addWidget(bt7)
		blay8_5.addStretch()
		widg8_5.setLayout(blay8_5)

		widg9 = QWidget()
		bt3 = QPushButton('🍪\n¥5', self)
		bt3.setMaximumHeight(50)
		bt3.setMinimumHeight(50)
		bt3.setMinimumWidth(50)
		bt3.clicked.connect(self.donate)
		bt4 = QPushButton('🥪\n¥10', self)
		bt4.setMaximumHeight(50)
		bt4.setMinimumHeight(50)
		bt4.setMinimumWidth(50)
		bt4.clicked.connect(self.donate2)
		bt5 = QPushButton('🍜\n¥20', self)
		bt5.setMaximumHeight(50)
		bt5.setMinimumHeight(50)
		bt5.setMinimumWidth(50)
		bt5.clicked.connect(self.donate3)
		bt6 = QPushButton('🍕\n¥50', self)
		bt6.setMaximumHeight(50)
		bt6.setMinimumHeight(50)
		bt6.setMinimumWidth(50)
		bt6.clicked.connect(self.donate4)
		blay9 = QHBoxLayout()
		blay9.setContentsMargins(0, 0, 0, 0)
		blay9.addStretch()
		blay9.addWidget(bt3)
		blay9.addWidget(bt4)
		blay9.addWidget(bt5)
		blay9.addWidget(bt6)
		blay9.addStretch()
		widg9.setLayout(blay9)

		widg10 = QWidget()
		lbl6 = QLabel('© 2023 Ryan-the-hito. All rights reserved.', self)
		blay10 = QHBoxLayout()
		blay10.setContentsMargins(0, 0, 0, 0)
		blay10.addStretch()
		blay10.addWidget(lbl6)
		blay10.addStretch()
		widg10.setLayout(blay10)

		main_h_box = QVBoxLayout()
		main_h_box.addWidget(widg1)
		main_h_box.addWidget(widg2)
		main_h_box.addWidget(widg3)
		main_h_box.addWidget(widg4)
		main_h_box.addWidget(widg5)
		main_h_box.addWidget(widg6)
		main_h_box.addWidget(widg7)
		main_h_box.addWidget(widg8)
		main_h_box.addWidget(widg8_5)
		main_h_box.addWidget(widg9)
		main_h_box.addWidget(widg10)
		main_h_box.addStretch()
		self.setLayout(main_h_box)

	def intro(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Ryan-the-hito')

	def homepage(self):
		webbrowser.open('https://github.com/Ryan-the-hito/Coconut')

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def donate(self):
		dlg = CustomDialog()
		dlg.exec()

	def donate2(self):
		dlg = CustomDialog2()
		dlg.exec()

	def donate3(self):
		dlg = CustomDialog3()
		dlg.exec()

	def donate4(self):
		dlg = CustomDialog4()
		dlg.exec()

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def activate(self):  # 设置窗口显示
		self.show()


class CustomDialog(QDialog):  # (About1)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog2(QDialog):  # (About2)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog3(QDialog):  # (About3)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class CustomDialog4(QDialog):  # (About4)
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUpMainWindow()
		self.setWindowTitle("Thank you for your support!")
		self.center()
		self.resize(400, 390)
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		widge_all = QWidget()
		l1 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'wechat50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l1.setMaximumSize(160, 240)
		l1.setScaledContents(True)
		l2 = QLabel(self)
		png = PyQt6.QtGui.QPixmap(BasePath + 'alipay50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
		l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
		l2.setMaximumSize(160, 240)
		l2.setScaledContents(True)
		bk = QHBoxLayout()
		bk.setContentsMargins(0, 0, 0, 0)
		bk.addWidget(l1)
		bk.addWidget(l2)
		widge_all.setLayout(bk)

		m1 = QLabel('Thank you for your kind support! 😊', self)
		m2 = QLabel('I will write more interesting apps! 🥳', self)

		widg_c = QWidget()
		bt1 = QPushButton('Thank you!', self)
		bt1.setMaximumHeight(20)
		bt1.setMinimumWidth(100)
		bt1.clicked.connect(self.cancel)
		bt2 = QPushButton('Neither one above? Buy me a coffee~', self)
		bt2.setMaximumHeight(20)
		bt2.setMinimumWidth(260)
		bt2.clicked.connect(self.coffee)
		blay8 = QHBoxLayout()
		blay8.setContentsMargins(0, 0, 0, 0)
		blay8.addStretch()
		blay8.addWidget(bt1)
		blay8.addWidget(bt2)
		blay8.addStretch()
		widg_c.setLayout(blay8)

		self.layout = QVBoxLayout()
		self.layout.addWidget(widge_all)
		self.layout.addWidget(m1)
		self.layout.addWidget(m2)
		self.layout.addStretch()
		self.layout.addWidget(widg_c)
		self.layout.addStretch()
		self.setLayout(self.layout)

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def coffee(self):
		webbrowser.open('https://www.buymeacoffee.com/ryanthehito')

	def cancel(self):  # 设置取消键的功能
		self.close()


class window_update(QWidget):  # 增加更新页面（Check for Updates）
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 说明页面内信息

		self.lbl = QLabel('Current Version: v1.0.0', self)
		self.lbl.move(30, 45)

		lbl0 = QLabel('Download Update:', self)
		lbl0.move(30, 75)

		lbl1 = QLabel('Latest Version:', self)
		lbl1.move(30, 15)

		self.lbl2 = QLabel('', self)
		self.lbl2.move(122, 15)

		bt1 = QPushButton('Google Drive', self)
		bt1.setFixedWidth(120)
		bt1.clicked.connect(self.upd)
		bt1.move(150, 75)

		bt2 = QPushButton('Baidu Netdisk', self)
		bt2.setFixedWidth(120)
		bt2.clicked.connect(self.upd2)
		bt2.move(150, 105)

		self.resize(300, 150)
		self.center()
		self.setWindowTitle('Coconut Updates')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def upd(self):
		pass

	def upd2(self):
		pass

	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def activate(self):  # 设置窗口显示
		self.show()
		self.checkupdate()

	def checkupdate(self):
		targetURL = 'https://github.com/Ryan-the-hito/Coconut/releases'
		try:
			# Fetch the HTML content from the URL
			urllib3.disable_warnings()
			logging.captureWarnings(True)
			s = requests.session()
			s.keep_alive = False  # 关闭多余连接
			response = s.get(targetURL, verify=False)
			response.encoding = 'utf-8'
			html_content = response.text
			# Parse the HTML using BeautifulSoup
			soup = BeautifulSoup(html_content, "html.parser")
			# Remove all images from the parsed HTML
			for img in soup.find_all("img"):
				img.decompose()
			# Convert the parsed HTML to plain text using html2text
			text_maker = html2text.HTML2Text()
			text_maker.ignore_links = True
			text_maker.ignore_images = True
			plain_text = text_maker.handle(str(soup))
			# Convert the plain text to UTF-8
			plain_text_utf8 = plain_text.encode(response.encoding).decode("utf-8")

			for i in range(10):
				plain_text_utf8 = plain_text_utf8.replace('\n\n\n\n', '\n\n')
				plain_text_utf8 = plain_text_utf8.replace('\n\n\n', '\n\n')
				plain_text_utf8 = plain_text_utf8.replace('   ', ' ')
				plain_text_utf8 = plain_text_utf8.replace('  ', ' ')

			pattern2 = re.compile(r'(v\d+\.\d+\.\d+)\sLatest')
			result = pattern2.findall(plain_text_utf8)
			result = ''.join(result)
			nowversion = self.lbl.text().replace('Current Version: ', '')
			if result == nowversion:
				alertupdate = result + '. You are up to date!'
				self.lbl2.setText(alertupdate)
				self.lbl2.adjustSize()
			else:
				alertupdate = result + ' is ready!'
				self.lbl2.setText(alertupdate)
				self.lbl2.adjustSize()
		except:
			alertupdate = 'No Intrenet'
			self.lbl2.setText(alertupdate)
			self.lbl2.adjustSize()


class TimeoutException(Exception):
	pass


class window3(QWidget):  # 主窗口
	def __init__(self):
		super().__init__()
		self.initUI()
		self.ReLa()
	
	def initUI(self):
		self.mytimer = QTimer(self)
		self.mytimer.timeout.connect(self.onTimer)

	def timeout_handler(self, signum, frame):
		raise TimeoutException("Timeout")

	def notify(self, CMD, title, text):
		subprocess.call(['osascript', '-e', CMD, title, text])

	def onTimer(self):
		active_app = NSWorkspace.sharedWorkspace().activeApplication()
		if active_app['NSApplicationName'] != 'loginwindow':
			# main code
			photos_name = codecs.open(BasePath + 'Photos_NAME.txt', 'r', encoding='utf-8').read()
			signal.signal(signal.SIGALRM, self.timeout_handler)
			signal.alarm(60)
			try:
				home_dir = str(Path.home())
				tarname1 = "CoconutAppPath"
				fulldir1 = os.path.join(home_dir, tarname1)
				if not os.path.exists(fulldir1):
					os.mkdir(fulldir1)
				tarname2 = "Finderpath.txt"
				fulldir2 = os.path.join(fulldir1, tarname2)
				if not os.path.exists(fulldir2):
					with open(fulldir2, 'a', encoding='utf-8') as f0:
						f0.write('')
				cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
				if cont != '':
					donefolder = "CoconutDone"
					donedir = os.path.join(cont, donefolder)
					if not os.path.exists(donedir):
						os.mkdir(donedir)
					errorfolder = "CoconutError"
					errordir = os.path.join(cont, errorfolder)
					if not os.path.exists(errordir):
						os.mkdir(errordir)
					self.list_dir = os.listdir(cont)
					self.list_dir.sort()
					while '.DS_Store' in self.list_dir:
						self.list_dir.remove('.DS_Store')
					while '' in self.list_dir:
						self.list_dir.remove('')
					while 'CoconutDone' in self.list_dir:
						self.list_dir.remove('CoconutDone')
					while 'CoconutError' in self.list_dir:
						self.list_dir.remove('CoconutError')
					Endlist = []
					SuccessImport = 0
					Relist = 0
					if self.list_dir != [] and len(self.list_dir) > 0:
						for x in range(len(self.list_dir)):
							TestName = os.path.join(cont, self.list_dir[x])
							detected_type = filetype.guess(TestName)
							if detected_type is not None and detected_type.mime.startswith('image/'):
								pass
							else:
								shutil.move(TestName, errordir)
								Relist = 1
						if Relist == 1:
							self.list_dir = os.listdir(cont)
							self.list_dir.sort()
							while '.DS_Store' in self.list_dir:
								self.list_dir.remove('.DS_Store')
							while '' in self.list_dir:
								self.list_dir.remove('')
							while 'CoconutDone' in self.list_dir:
								self.list_dir.remove('CoconutDone')
							while 'CoconutError' in self.list_dir:
								self.list_dir.remove('CoconutError')
					if self.list_dir != [] and len(self.list_dir) > 0:
						if len(self.list_dir) == 1:
							current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
							file_extension = os.path.splitext(self.list_dir[0])[1]
							newname = 'CoconutSync ' + current_time + file_extension
							NewName = os.path.join(cont, newname)
							EndName = os.path.join(cont, self.list_dir[0])
							os.rename(EndName, NewName)
							Endlist.append(NewName)
							importcmd = '''
								tell application "%s"
									get count of media items
									set olditems to count of media items
									import POSIX file "%s"
									get count of media items
									set newitems to count of media items
									repeat while newitems < olditems + 1
										delay 1
										get count of media items
										set newitems to count of media items
									end repeat
								end tell''' % (photos_name, Endlist[0])
							subprocess.call(['osascript', '-e', importcmd])
							SuccessImport = 1
						if len(self.list_dir) == 2:
							for i in range(2):
								current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
								file_extension = os.path.splitext(self.list_dir[i])[1]
								newname = 'CoconutSync ' + current_time + file_extension
								NewName = os.path.join(cont, newname)
								EndName = os.path.join(cont, self.list_dir[i])
								os.rename(EndName, NewName)
								Endlist.append(NewName)
							importcmd = '''
								tell application "%s"
									get count of media items
									set olditems to count of media items
									import POSIX file "%s"
									import POSIX file "%s"
									get count of media items
									set newitems to count of media items
									repeat while newitems < olditems + 2
										delay 1
										get count of media items
										set newitems to count of media items
									end repeat
								end tell''' % (photos_name, Endlist[0], Endlist[1])
							subprocess.call(['osascript', '-e', importcmd])
							SuccessImport = 1
						if len(self.list_dir) == 3:
							for i in range(3):
								current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
								file_extension = os.path.splitext(self.list_dir[i])[1]
								newname = 'CoconutSync ' + current_time + file_extension
								NewName = os.path.join(cont, newname)
								EndName = os.path.join(cont, self.list_dir[i])
								os.rename(EndName, NewName)
								Endlist.append(NewName)
							importcmd = '''
								tell application "%s"
									get count of media items
									set olditems to count of media items
									import POSIX file "%s"
									import POSIX file "%s"
									import POSIX file "%s"
									get count of media items
									set newitems to count of media items
									repeat while newitems < olditems + 3
										delay 1
										get count of media items
										set newitems to count of media items
									end repeat
								end tell''' % (photos_name, Endlist[0], Endlist[1], Endlist[2])
							subprocess.call(['osascript', '-e', importcmd])
							SuccessImport = 1
						if len(self.list_dir) == 4:
							for i in range(4):
								current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
								file_extension = os.path.splitext(self.list_dir[i])[1]
								newname = 'CoconutSync ' + current_time + file_extension
								NewName = os.path.join(cont, newname)
								EndName = os.path.join(cont, self.list_dir[i])
								os.rename(EndName, NewName)
								Endlist.append(NewName)
							importcmd = '''
								tell application "%s"
									get count of media items
									set olditems to count of media items
									import POSIX file "%s"
									import POSIX file "%s"
									import POSIX file "%s"
									import POSIX file "%s"
									get count of media items
									set newitems to count of media items
									repeat while newitems < olditems + 4
										delay 1
										get count of media items
										set newitems to count of media items
									end repeat
								end tell''' % (photos_name, Endlist[0], Endlist[1], Endlist[2], Endlist[3])
							subprocess.call(['osascript', '-e', importcmd])
							SuccessImport = 1
						if len(self.list_dir) >= 5:
							for i in range(5):
								current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
								file_extension = os.path.splitext(self.list_dir[i])[1]
								newname = 'CoconutSync ' + current_time + file_extension
								NewName = os.path.join(cont, newname)
								EndName = os.path.join(cont, self.list_dir[i])
								os.rename(EndName, NewName)
								Endlist.append(NewName)
							importcmd = '''
								tell application "%s"
									get count of media items
									set olditems to count of media items
									import POSIX file "%s"
									import POSIX file "%s"
									import POSIX file "%s"
									import POSIX file "%s"
									import POSIX file "%s"
									get count of media items
									set newitems to count of media items
									repeat while newitems < olditems + 5
										delay 1
										get count of media items
										set newitems to count of media items
									end repeat
								end tell''' % (photos_name, Endlist[0], Endlist[1], Endlist[2], Endlist[3], Endlist[4])
							subprocess.call(['osascript', '-e', importcmd])
							SuccessImport = 1
						if SuccessImport == 1:
							for t in range(len(Endlist)):
								shutil.move(Endlist[t], donedir)
			except TimeoutException:
				CMD = '''
				on run argv
					display notification (item 2 of argv) with title (item 1 of argv)
				end run'''
				self.notify(CMD, "Finder-iCloud Photo Synchronizer",
							f"There seems to be an error. Please try again.")
			except Exception as e:
				with open(BasePath + 'errorfile.txt', 'w', encoding='utf-8') as f0:
					f0.write(str(e))
				CMD = '''
				on run argv
					display notification (item 2 of argv) with title (item 1 of argv)
				end run'''
				self.notify(CMD, "Finder-iCloud Photo Synchronizer",
							f"Error. Please try again.")
			signal.alarm(0)

	def activate(self):  # 设置窗口显示
		if action3.isChecked():
			SetTime = int(codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read())
			self.mytimer.start(60000*SetTime)
		if not action3.isChecked():
			self.mytimer.stop()

	def ReLa(self):
		ReLa = codecs.open(BasePath + "ReLa.txt", 'r', encoding='utf-8').read()
		if ReLa == '1':
			action3.setChecked(True)
			SetTime = int(codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read())
			self.mytimer.start(60000 * SetTime)

	def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()

	def cancel(self):  # 设置取消键的功能
		self.close()


class window4(QWidget):  # Customization settings
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):  # 设置窗口内布局
		self.setUpMainWindow()
		self.setFixedSize(500, 170)
		self.center()
		self.setWindowTitle('Customization settings')
		self.setFocus()
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

	def setUpMainWindow(self):
		self.lbl1 = QLabel('Detect target path every (minutes): ', self)

		self.le1 = QLineEdit(self)
		self.le1.setPlaceholderText('Minutes. Numbers only, no decimal. Default=1')
		text = codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read()
		self.le1.setText(text)

		self.lbl0 = QLabel('', self)
		self.btn_0 = QPushButton('Set photo path: ', self)
		self.btn_0.clicked.connect(self.Setpath)
		self.btn_0.setFixedSize(150, 20)
		home_dir = str(Path.home())
		tarname1 = "CoconutAppPath"
		fulldir1 = os.path.join(home_dir, tarname1)
		if not os.path.exists(fulldir1):
			os.mkdir(fulldir1)
		tarname2 = "Finderpath.txt"
		fulldir2 = os.path.join(fulldir1, tarname2)
		if not os.path.exists(fulldir2):
			with open(fulldir2, 'a', encoding='utf-8') as f0:
				f0.write('')
		cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
		if cont != '':
			if len(cont) > 45:
				cont = cont[0:41] + '...'
			self.lbl0.setText(cont)
			self.lbl0.adjustSize()

		self.lbl7 = QLabel('Photos.app is named as: ', self)
		self.le5 = QLineEdit(self)
		self.le5.setPlaceholderText('Photos')
		High = codecs.open(BasePath + 'Photos_NAME.txt', 'r', encoding='utf-8').read()
		self.le5.setText(High)

		self.btn_1 = QPushButton('Save', self)
		self.btn_1.clicked.connect(self.SetTime)
		self.btn_1.setFixedSize(150, 20)

		qw0 = QWidget()
		vbox0 = QHBoxLayout()
		vbox0.setContentsMargins(0, 0, 0, 0)
		vbox0.addWidget(self.btn_0)
		vbox0.addWidget(self.lbl0)
		qw0.setLayout(vbox0)

		qw1 = QWidget()
		vbox1 = QHBoxLayout()
		vbox1.setContentsMargins(0, 0, 0, 0)
		vbox1.addStretch()
		vbox1.addWidget(self.btn_1)
		vbox1.addStretch()
		qw1.setLayout(vbox1)

		qw4 = QWidget()
		vbox4 = QHBoxLayout()
		vbox4.setContentsMargins(0, 0, 0, 0)
		vbox4.addWidget(self.lbl7)
		vbox4.addWidget(self.le5)
		qw4.setLayout(vbox4)

		qw5 = QWidget()
		vbox5 = QHBoxLayout()
		vbox5.setContentsMargins(0, 0, 0, 0)
		vbox5.addWidget(self.lbl1)
		vbox5.addWidget(self.le1)
		qw5.setLayout(vbox5)

		vbox2 = QVBoxLayout()
		vbox2.setContentsMargins(20, 20, 20, 20)
		vbox2.addWidget(qw5)
		vbox2.addWidget(qw0)
		vbox2.addWidget(qw4)
		vbox2.addWidget(qw1)
		self.setLayout(vbox2)
	
	def SetTime(self):
		if self.le1.text() != '' and self.le1.text() != '0':
			SetTime = str(int(self.le1.text()))
			with open(BasePath + "SetTime.txt", 'w', encoding='utf-8') as f0:
				f0.write(SetTime)
		if self.le5.text() != '':
			High = str(self.le5.text())
			with open(BasePath + "Photos_NAME.txt", 'w', encoding='utf-8') as f0:
				f0.write(High)
		self.close()

	def Setpath(self):
		home_dir = str(Path.home())
		fj = QFileDialog.getExistingDirectory(self, 'Open', home_dir)
		if fj != '':
			home_dir = str(Path.home())
			tarname1 = "CoconutAppPath"
			fulldir1 = os.path.join(home_dir, tarname1)
			if not os.path.exists(fulldir1):
				os.mkdir(fulldir1)
			tarname2 = "Finderpath.txt"
			fulldir2 = os.path.join(fulldir1, tarname2)
			if not os.path.exists(fulldir2):
				with open(fulldir2, 'a', encoding='utf-8') as f0:
					f0.write('')
			with open(fulldir2, 'w', encoding='utf-8') as f0:
				f0.write(fj)
			if len(fj) > 45:
				fj = fj[0:41] + '...'
			self.lbl0.setText(fj)
			self.lbl0.adjustSize()

	def totalquit(self):
		with open(BasePath + "ReLa.txt", 'w', encoding='utf-8') as f0:
			f0.write('0')
		sys.exit(0)
	
	def center(self):  # 设置窗口居中
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
		if e.key() == Qt.Key.Key_Escape.value:
			self.close()
	
	def activate(self):  # 设置窗口显示
		text = codecs.open(BasePath + 'SetTime.txt', 'r', encoding='utf-8').read()
		self.le1.setText(text)
		High = codecs.open(BasePath + 'Photos_NAME.txt', 'r', encoding='utf-8').read()
		self.le5.setText(High)
		home_dir = str(Path.home())
		tarname1 = "CoconutAppPath"
		fulldir1 = os.path.join(home_dir, tarname1)
		if not os.path.exists(fulldir1):
			os.mkdir(fulldir1)
		tarname2 = "Finderpath.txt"
		fulldir2 = os.path.join(fulldir1, tarname2)
		if not os.path.exists(fulldir2):
			with open(fulldir2, 'a', encoding='utf-8') as f0:
				f0.write('')
		cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
		if cont != '':
			if len(cont) > 45:
				cont = cont[0:41] + '...'
			self.lbl0.setText(cont)
			self.lbl0.adjustSize()

		w2.checkupdate()
		if w2.lbl2.text() != 'No Intrenet' and 'ready' in w2.lbl2.text():
			w2.show()

		self.show()
		self.setFocus()
		self.raise_()
		self.activateWindow()
	
	def cancel(self):  # 设置取消键的功能
		self.close()

style_sheet_ori = '''
	QTabWidget::pane {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QTableWidget{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #FFFFFF;
		color: #000000;
		font: 14pt Helvetica;
}
	QWidget#Main {
		border: 1px solid #ECECEC;
		background: #ECECEC;
		border-radius: 9px;
}
	QPushButton{
		border: 1px outset grey;
		background-color: #FFFFFF;
		border-radius: 4px;
		padding: 1px;
		color: #000000
}
	QPushButton:pressed{
		border: 1px outset grey;
		background-color: #0085FF;
		border-radius: 4px;
		padding: 1px;
		color: #FFFFFF
}
	QPlainTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QPlainTextEdit#edit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #FFFFFF;
		color: rgb(113, 113, 113);
		font: 14pt Helvetica;
}
	QTableWidget#small{
		border: 1px solid grey;  
		border-radius:4px;
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QLineEdit{
		border-radius:4px;
		border: 1px solid gray;
		background-color: #FFFFFF;
}
	QTextEdit{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
	QListWidget{
		border: 1px solid grey;  
		border-radius:4px;
		padding: 1px 5px 1px 3px; 
		background-clip: border;
		background-color: #F3F2EE;
		color: #000000;
		font: 14pt Times New Roman;
}
'''

if __name__ == '__main__':
	while True:
		try:
			w1 = window_about()  # about
			w2 = window_update()  # update
			w3 = window3()  # main1
			w3.setAutoFillBackground(True)
			p = w3.palette()
			p.setColor(w3.backgroundRole(), QColor('#ECECEC'))
			w3.setPalette(p)
			w4 = window4()  # CUSTOMIZING
			action1.triggered.connect(w1.activate)
			action2.triggered.connect(w2.activate)
			action3.triggered.connect(w3.activate)
			action7.triggered.connect(w4.activate)
			btna4.triggered.connect(w3.activate)
			quit.triggered.connect(w4.totalquit)
			app.setStyleSheet(style_sheet_ori)
			app.exec()
		except Exception as e:
			# 发生异常时打印错误信息
			p = "程序发生异常:" + str(e)
			with open(BasePath + "Error.txt", 'w', encoding='utf-8') as f0:
				f0.write(p)
			# 延时一段时间后重新启动程序（例如延时 5 秒）
			time.sleep(5)
			# 重启后的操作
			with open(BasePath + "ReLa.txt", 'w', encoding='utf-8') as f0:
				f0.write('1')
			# 使用 os.execv() 在当前进程中启动自身，实现自动重启
			os.execv(sys.executable, [sys.executable, __file__])
