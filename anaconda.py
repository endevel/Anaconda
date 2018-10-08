#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

#from PyQt5.QtWidgets import QApplication
#from gui.main_form import MainWindow

if __name__ == '__main__':

    import sys

    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG,
                        filename = u'anaconda.log'
    )
    print('Anaconda is running . . .')

'''
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
'''
