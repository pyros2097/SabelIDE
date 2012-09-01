from PyQt4 import QtGui 
from PyQt4 import QtCore
from globals import adblist,config,device
from globals import PY_VERSION,__version__,OS_NAME

class DialogAndroid(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(400, 420)
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 361))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.tabWidget = QtGui.QTabWidget(self.horizontalLayoutWidget)
        self.tab_4 = QtGui.QWidget()
       
        
        self.formLayoutWidget = QtGui.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 311))
        
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_2)
        
        #Push
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.formLayoutWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.lineEdit_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.fileButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.fileButton.setText("Browse")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addWidget(self.fileButton)
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.horizontalLayoutWidget_2)
        
        self.lineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.lineEdit_3)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.lineEdit_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget)
        self.formLayout.setWidget(8, QtGui.QFormLayout.SpanningRole, self.lineEdit_5)
        self.tabWidget.addTab(self.tab_4, "Android")
        
        #radio buttons
        self.radio1=QtGui.QRadioButton("Device", self.formLayoutWidget)
        self.radio2=QtGui.QRadioButton("Emulator", self.formLayoutWidget)
        self.radio1.clicked.connect(lambda:self.setDevice(1))
        self.radio2.clicked.connect(lambda:self.setDevice(0))
        self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole,self.radio1)
        self.formLayout.setWidget(10, QtGui.QFormLayout.SpanningRole,self.radio2)
        self.radio1.setChecked(1)
        self.horizontalLayout.addWidget(self.tabWidget)
        
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(40, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(("buttonBox"))
        self.tabWidget.setCurrentIndex(1)
        self.setWindowTitle("Tools")
        self.label_2.setText("Push Main File:")
        self.label_3.setText("Start Activity:")
        self.label_4.setText("Logcat:")
        self.label_5.setText("Exit Activity:")
        self.buttonBox.clicked.connect(self.update)
        self.lineEdit_2.setText(adblist[0])
        self.lineEdit_3.setText(adblist[1])
        self.lineEdit_4.setText(adblist[2])
        self.lineEdit_5.setText(adblist[3])
        self.fileButton.clicked.connect(self.getFile)
        
        
    def getFile(self):
        fname = str(QtGui.QFileDialog.getOpenFileName(self,"Open File", '.', "Files (*.*)"))
        if not (fname == ""):
            val = []
            self.lineEdit_2.setText(fname+" /sdcard/")
            val.append(str(self.lineEdit_2.text()))
            val.append(str(self.lineEdit_3.text()))
            val.append(str(self.lineEdit_4.text()))
            val.append(str(self.lineEdit_5.text()))
            config.setAdb(val)
            
    def update(self,btn):
        val = []
        if(btn.text() == "OK"):
            val.append(str(self.lineEdit_2.text()))
            val.append(str(self.lineEdit_3.text()))
            val.append(str(self.lineEdit_4.text()))
            val.append(str(self.lineEdit_5.text()))
            config.setAdb(val)
        self.close()
        
    def setDevice(self,val):
        config.setDevice(val)
        
class DialogAnt(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(400, 420)
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 361))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        
        self.tabWidget = QtGui.QTabWidget(self.horizontalLayoutWidget)
        self.tab_4 = QtGui.QWidget()
       
        self.formLayoutWidget = QtGui.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 311))
        
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setText((""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setText((""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.lineEdit_3)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setText((""))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.lineEdit_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setText((""))
        self.formLayout.setWidget(8, QtGui.QFormLayout.SpanningRole, self.lineEdit_5)
        self.tabWidget.addTab(self.tab_4, (""))
        self.horizontalLayout.addWidget(self.tabWidget)
        
class DialogSquirrel(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(400, 420)
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 361))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        
        self.tabWidget = QtGui.QTabWidget(self.horizontalLayoutWidget)
        self.tab_4 = QtGui.QWidget()
       
        self.formLayoutWidget = QtGui.QWidget(self.tab_4)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 311))
        
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setText((""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setText((""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.lineEdit_3)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setText((""))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.lineEdit_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setText((""))
        self.formLayout.setWidget(8, QtGui.QFormLayout.SpanningRole, self.lineEdit_5)
        self.tabWidget.addTab(self.tab_4, (""))
        self.horizontalLayout.addWidget(self.tabWidget)
        
class DialogAbout(QtGui.QMessageBox):
    def __init__(self, parent=None):
        QtGui.QMessageBox.__init__(self, parent)
        text = """
                <b>Credits</b>
                <b>Sabel</b> v%s
                <p>
                All rights reserved in accordance with
                GPL v3 or later.
                <p>This application can be used for Squirrel and EmoFramework Projects.
                <p>Squirrel Shell Copyright (c) 2006-2011, Constantin Makshin
                <p>Squirrel Copyright (c) Alberto Demichelis
                <p>zlib Copyright (c) Jean-loup Gailly and Mark Adler
                <p>Icons Copyright (c) Eclipse EPL
                <p>Emo-Framework Copyright (c) 2011 Kota Iguchi
                <p>Python %s - Qt %s - PyQt %s on %s
                <p>Created By: pyros2097
                <p>THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
                 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,INCLUDING, BUT NOT
                 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
                 FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
                 EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
                 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
                 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
                 PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
                 OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
                 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
                 OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
                 OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
                 POSSIBILITY OF SUCH DAMAGE.
                """ % (__version__,PY_VERSION,QtCore.QT_VERSION_STR, QtCore.PYQT_VERSION_STR,OS_NAME)
        self.about(self,"About",text)

class DialogAbout2(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(400, 420)
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 400, 420))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.view = MyView(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.view)
        
class MyView(QtGui.QGraphicsView):
    def __init__(self,parent):
        QtGui.QGraphicsView.__init__(self,parent)
        font=QtGui.QFont('White Rabbit')
        font.setPointSize(8)
        font.setBold(True)
        self.scene = QtGui.QGraphicsScene(self)
        text = """
                <b>Credits</b>
                <b>Sabel</b> v%s
                <p>
                All rights reserved in accordance with
                GPL v3 or later.
                <p>This application can be used for Squirrel and EmoFramework Projects.
                <p>Squirrel Shell Copyright (c) 2006-2011, Constantin Makshin
                <p>Squirrel Copyright (c) Alberto Demichelis
                <p>zlib Copyright (c) Jean-loup Gailly and Mark Adler
                <p>Icons Copyright (c) Eclipse EPL
                <p>Emo-Framework Copyright (c) 2011 Kota Iguchi
                <p>Python %s - Qt %s - PyQt %s on %s
                <p>Created By: pyros2097
                <p>THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
                 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,INCLUDING, BUT NOT
                 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
                 FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
                 EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
                 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
                 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
                 PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
                 OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
                 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
                 OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
                 OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
                 POSSIBILITY OF SUCH DAMAGE.
                """ % (__version__,PY_VERSION,QtCore.QT_VERSION_STR, QtCore.PYQT_VERSION_STR,OS_NAME)
        self.dot1=QtGui.QGraphicsTextItem(text)
        self.dot1.setFont(font)
        self.dot1.setPos(0,0)
        self.dot1=QtGui.QGraphicsTextItem(text)
        
        #self.item = QtGui.QGraphicsEllipseItem(-20, -10, 40, 20)
        #self.scene.addItem(self.item)
        self.scene.addItem(self.dot1)
        self.setScene(self.scene)

        # Remember to hold the references to QTimeLine and QGraphicsItemAnimation instances.
        # They are not kept anywhere, even if you invoke QTimeLine.start().
        self.tl = QtCore.QTimeLine(1000)
        self.tl.setFrameRange(0, 100)
        self.a = QtGui.QGraphicsItemAnimation()
        #self.a.setItem(self.item)
        self.a.setItem(self.dot1)
        self.a.setTimeLine(self.tl)

        # Each method determining an animation state (e.g. setPosAt, setRotationAt etc.)
        # takes as a first argument a step which is a value between 0 (the beginning of the
        # animation) and 1 (the end of the animation)
        self.a.setPosAt(1, QtCore.QPointF(0, -200))
        #self.a.setRotationAt(1, 360)

        self.tl.start()