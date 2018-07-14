import sys
import array
import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
import MainWindow
import Parameters
import About

class AbW(QtWidgets.QMainWindow, About.Ui_About):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.Close.clicked.connect(self.close_clicked)

    def close_clicked(self):
        global abw
        abw.destroy()

class ParW(QtWidgets.QMainWindow, Parameters.Ui_MainWindow):
    starting = pyqtSignal(bool)
    comp_play = pyqtSignal(bool)
    race = pyqtSignal(str)
    comp = True
    choosen_race = 'X'
    
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(self)
        self.Cancel.clicked.connect(self.cancel_clicked)
        self.Start.clicked.connect(self.start_clicked)
        self.Comp.clicked.connect(self.comp_checked)
        self.Human.clicked.connect(self.human_checked)
        self.X.clicked.connect(self.x_checked)
        self.O.clicked.connect(self.o_checked)
        self.starting.connect(parent.starting_game)
        self.comp_play.connect(parent.comp_change)
        self.race.connect(parent.race_change)

    def cancel_clicked(self):
        global param
        param.close()

    def start_clicked(self):
        self.starting.emit(True)
        self.comp_play.emit(self.comp)
        self.race.emit(self.choosen_race)
        self.close()

    def comp_checked(self):
        self.comp = True
        self.X.setEnabled(True)
        self.O.setEnabled(True)
        self.Race.setEnabled(True)

    def human_checked(self):
        self.comp = False
        self.X.setEnabled(False)
        self.O.setEnabled(False)
        self.Race.setEnabled(False)

    def x_checked(self):
        self.choosen_race = 'X'

    def o_checked(self):
        self.choosen_race = 'O'

    def getStarted(self):
        global starting
        return starting
    
    def getComp(self):
        return self.comp
    
    def getRace(self):
        return self.choosen_race

class KNApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    comp_play = True
    race = 'X'
    win = True
    step_count = 0
    function_calls = 0
    
    
    def __init__(self, parent = None):
        super(KNApp, self).__init__(parent)
        self.setupUi(self)
        self.param = ParW(self)
        self.Exit.clicked.connect(self.exit_clicked)
        self.NewGame.clicked.connect(self.ng_clicked)
        self.About.clicked.connect(self.about_clicked)
        self.Button1.clicked.connect(self.button1_clicked)
        self.Button2.clicked.connect(self.button2_clicked)
        self.Button3.clicked.connect(self.button3_clicked)
        self.Button4.clicked.connect(self.button4_clicked)
        self.Button5.clicked.connect(self.button5_clicked)
        self.Button6.clicked.connect(self.button6_clicked)
        self.Button7.clicked.connect(self.button7_clicked)
        self.Button8.clicked.connect(self.button8_clicked)
        self.Button9.clicked.connect(self.button9_clicked)

    def exit_clicked(self):
        sys.exit()

    def ng_clicked(self):
        self.param.show()

    def about_clicked(self):
        global abw
        abw = AbW()
        abw.show()

    def button1_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button1.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button1.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button1.text() == '':
            self.Button1.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def button2_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button2.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button2.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button2.text() == '':
            self.Button2.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def button3_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button3.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button3.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button3.text() == '':
            self.Button3.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def button4_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button4.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button4.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button4.text() == '':
            self.Button4.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def button5_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button5.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button5.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button5.text() == '':
            self.Button5.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def button6_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button6.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button6.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button6.text() == '':
            self.Button6.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def button7_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button7.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button7.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button7.text() == '':
            self.Button7.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def button8_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button8.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button8.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button8.text() == '':
            self.Button8.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def button9_clicked(self):
        global t, i
        if self.win:
            self.starting_game()
            if self.comp_play:
                if self.race == 'O':
                    self.comp_step()
                else:
                    self.step_text()
                    self.Button9.setText(t[i])
                    i = (i + 1) % 2
                    self.step_count = 1
                    self.comp_step()
            else:
                self.step_text()
                self.Button9.setText(t[i])
                i = (i + 1) % 2
                self.step_count = 1
            self.win = False
        elif self.Button9.text() == '':
            self.Button9.setText(t[i])
            self.winning_check()
            if self.win == False:
                if self.comp_play:
                    i = (i + 1) % 2
                    self.comp_step()
                else:
                    i = (i + 1) % 2

    def starting_game(self):
        global i
        self.Button1.setText('')
        self.Button2.setText('')
        self.Button3.setText('')
        self.Button4.setText('')
        self.Button5.setText('')
        self.Button6.setText('')
        self.Button7.setText('')
        self.Button8.setText('')
        self.Button9.setText('')
        i = 1
        self.step_text()
        i = 0
        self.step_count = 0

    def comp_change(self, a):
        self.comp_play = a

    def race_change(self, a):
        self.race = a
        if self.comp_play and self.race == 'O':
            self.comp_step()

    def winning_text(self):
        self.win = True
        if i:
            self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:23pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Нолики победили!</span></p></body></html>")
        else:
            self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:23pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Крестики победили!</span></p></body></html>")

    def step_text(self):
        if i:
            self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:23pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Ходят Крестики</span></p></body></html>")
        else:
            self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:23pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Ходят Нолики</span></p></body></html>")

    def winning_check(self):
        global t, i
        if self.Button1.text() == t[i] and self.Button2.text() == t[i] and self.Button3.text() == t[i]:
            self.winning_text()
        elif self.Button4.text() == t[i] and self.Button5.text() == t[i] and self.Button6.text() == t[i]:
            self.winning_text()
        elif self.Button7.text() == t[i] and self.Button8.text() == t[i] and self.Button9.text() == t[i]:
            self.winning_text()
        elif self.Button1.text() == t[i] and self.Button4.text() == t[i] and self.Button7.text() == t[i]:
            self.winning_text()
        elif self.Button2.text() == t[i] and self.Button5.text() == t[i] and self.Button8.text() == t[i]:
            self.winning_text()
        elif self.Button3.text() == t[i] and self.Button6.text() == t[i] and self.Button9.text() == t[i]:
            self.winning_text()
        elif self.Button1.text() == t[i] and self.Button5.text() == t[i] and self.Button9.text() == t[i]:
            self.winning_text()
        elif self.Button3.text() == t[i] and self.Button5.text() == t[i] and self.Button7.text() == t[i]:
            self.winning_text()
        else:
            self.step_check()

    def step_check(self):
        if self.step_count > 7:
            self.win = True
            self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:23pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Ничья</span></p></body></html>")
        else:
            self.step_count = self.step_count + 1
            self.step_text()

    def get_board(self):
        b = ['', '', '', '', '', '', '', '', '']
        b[0] = self.Button1.text()
        b[1] = self.Button2.text()
        b[2] = self.Button3.text()
        b[3] = self.Button4.text()
        b[4] = self.Button5.text()
        b[5] = self.Button6.text()
        b[6] = self.Button7.text()
        b[7] = self.Button8.text()
        b[8] = self.Button9.text()
        return b

    def comp_winning_check(self, board, step):
        if board[0] == step and board[1] == step and board[2] == step:
            return True
        elif board[3] == step and board[4] == step and board[5] == step:
            return True
        elif board[6] == step and board[7] == step and board[8] == step:
            return True
        elif board[0] == step and board[3] == step and board[6] == step:
            return True
        elif board[1] == step and board[4] == step and board[7] == step:
            return True
        elif board[2] == step and board[5] == step and board[8] == step:
            return True
        elif board[0] == step and board[4] == step and board[8] == step:
            return True
        elif board[2] == step and board[4] == step and board[6] == step:
            return True
        else:
            return False

    def comp_race_calc(self):
        if self.race == 'X':
            return 'O'
        else:
            return 'X'

    def available_spots(self, board):
        b = []
        for j in range(9):
            if board[j] == '':
                b.append(j)
        return b

    def step_calculate(self, new_board, s, m):
        self.function_calls = self.function_calls + 1
        a = self.available_spots(new_board)
        if self.comp_winning_check(new_board, self.race):
            return [m, -10]
        if self.comp_winning_check(new_board, self.comp_race_calc()):
            return [m, 10]
        if len(a) == 0:
            return [m, 0]
        moves = []
        for j in range(len(a)):
            move = [-1, -11]
            move[0] = a[j]
            new_board[a[j]] = s
            if s == self.comp_race_calc():
                move = self.step_calculate(new_board, self.race, a[j])
            else:
                move = self.step_calculate(new_board, self.comp_race_calc(), a[j])
            new_board[a[j]] = ''
            moves.append(move)
        best_spot = -1
        if s == self.comp_race_calc():
            best = -20
            for j in range(len(moves)):
                if moves[j][1] > best:
                    best = moves[j][1]
                    best_spot = j
        else:
            best = 20
            for j in range(len(moves)):
                if moves[j][1] < best:
                    best = moves[j][1]
                    best_spot = j
        return moves[best_spot]

    def pre_win_check(self, board, step):
        if board[0] == '' and board[1] == step and board[2] == step:
            return 0
        elif board[0] == step and board[1] == '' and board[2] == step:
            return 1
        elif board[0] == step and board[1] == step and board[2] == '':
            return 2
        elif board[3] == '' and board[4] == step and board[5] == step:
            return 3
        elif board[3] == step and board[4] == '' and board[5] == step:
            return 4
        elif board[3] == step and board[4] == step and board[5] == '':
            return 5
        elif board[6] == '' and board[7] == step and board[8] == step:
            return 6
        elif board[6] == step and board[7] == '' and board[8] == step:
            return 7
        elif board[6] == step and board[7] == step and board[8] == '':
            return 8
        elif board[0] == '' and board[3] == step and board[6] == step:
            return 0
        elif board[0] == step and board[3] == '' and board[6] == step:
            return 3
        elif board[0] == step and board[3] == step and board[6] == '':
            return 6
        elif board[1] == '' and board[4] == step and board[7] == step:
            return 1
        elif board[1] == step and board[4] == '' and board[7] == step:
            return 4
        elif board[1] == step and board[4] == step and board[7] == '':
            return 7
        elif board[2] == '' and board[5] == step and board[8] == step:
            return 2
        elif board[2] == step and board[5] == '' and board[8] == step:
            return 5
        elif board[2] == step and board[5] == step and board[8] == '':
            return 8
        elif board[0] == '' and board[4] == step and board[8] == step:
            return 0
        elif board[0] == step and board[4] == '' and board[8] == step:
            return 4
        elif board[0] == step and board[4] == step and board[8] == '':
            return 8
        elif board[2] == '' and board[4] == step and board[6] == step:
            return 2
        elif board[2] == step and board[4] == '' and board[6] == step:
            return 4
        elif board[2] == step and board[4] == step and board[6] == '':
            return 6
        else:
            return -1

    def comp_step(self):
        global i
        board = self.get_board()
        self.function_calls = 0
        choosen_spot = [-1, -11]
        if self.step_count == 0:
            choosen_spot[0] = 4
        elif self.step_count == 1:
            if self.Button5.text() == '':
                choosen_spot[0] = 4
            else:
                chose = [0, 2, 6, 8]
                choosen_spot[0] = random.choice(chose)
        else:
            check = self.pre_win_check(board, self.comp_race_calc())
            if check > -1:
                choosen_spot[0] = check
            else:
                check = self.pre_win_check(board, self.race)
                if check > -1:
                   choosen_spot[0] = check
                else:
                    choosen_spot = self.step_calculate(board, self.comp_race_calc(), -1)
        if choosen_spot[0] == 0:
            self.Button1.setText(self.comp_race_calc())
        elif choosen_spot[0] == 1:
            self.Button2.setText(self.comp_race_calc())
        elif choosen_spot[0] == 2:
            self.Button3.setText(self.comp_race_calc())
        elif choosen_spot[0] == 3:
            self.Button4.setText(self.comp_race_calc())
        elif choosen_spot[0] == 4:
            self.Button5.setText(self.comp_race_calc())
        elif choosen_spot[0] == 5:
            self.Button6.setText(self.comp_race_calc())
        elif choosen_spot[0] == 6:
            self.Button7.setText(self.comp_race_calc())
        elif choosen_spot[0] == 7:
            self.Button8.setText(self.comp_race_calc())
        elif choosen_spot[0] == 8:
            self.Button9.setText(self.comp_race_calc())
        self.winning_check()
        i = (i + 1) % 2
        
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = KNApp()
    window.show()
    app.exec_()

t = ['X', 'O']
i = 0
if __name__ == '__main__':
    main()
