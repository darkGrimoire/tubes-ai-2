import clips
import re
import time
class MainProgram:
    def __init__(self):
        self.papan = []
        self.env = clips.Environment()
        print("Hallo")
        self.env.clear()
        self.env.define_function(self.getNilaiSel)
        self.env.define_function(self.printui)
        self.env.load("minesweeper.clp")
        self.ukuran = 4
        self.jumlah_bom = 0
        self.bombLoc = []
        self.is_finished = 0
        self.printToUI = None

    def getNilaiSel(self, col, row):
        # INGET, di ARRAY disimpen dalam format papan[row][col]
        return self.papan[row][col]

    def printui(self, msg):
        self.printToUI(msg)

    def generateNilai(self):
        for i in range(self.ukuran):
            for j in range(self.ukuran):
                if (self.papan[i][j] != -1):
                    continue
                daftar_sel_tetangga = [[i+1, j], [i+1, j+1], [i, j+1],
                                    [i-1, j+1], [i-1, j], [i-1, j-1], [i, j-1], [i+1, j-1]]
                for sel_tetangga in daftar_sel_tetangga:
                    if (sel_tetangga[0] < 0 or sel_tetangga[1] < 0 or sel_tetangga[0] >= self.ukuran or sel_tetangga[1] >= self.ukuran):
                        continue
                    temp = self.papan[sel_tetangga[0]][sel_tetangga[1]]
                    if (temp == -1):
                        continue
                    self.papan[sel_tetangga[0]][sel_tetangga[1]] = temp + 1
    
    def updatePapanBasedOnFacts(self):
        daftar_fakta_sel = []
        status_papan = []
    
        # Masukkan semua fakta mengenai papan
        for fact in self.env.facts():
            if re.search("\(sel \(col ", str(fact)):
                daftar_fakta_sel.append(fact)
        
        # Cetak isi papan
        for row in range(len(self.papan)):
            for col in range(len(self.papan[row])):
                i = 0
                temu = False
                while ((i < len(daftar_fakta_sel)) and (not temu)):
                    temp_fakta = daftar_fakta_sel[i]
                    temp_str = "\(col "+str(col)+"\) \(row "+str(row)+"\)"
                    if re.search(temp_str, str(temp_fakta)):
                        fakta_sel = temp_fakta
                        temu = True
                    else:
                        i += 1
                        continue
                nilai_sel = re.search("(nilai ([0-9]|X|F)*)", str(fakta_sel))
                nilai_sel = nilai_sel.group(0)
                nilai_sel = nilai_sel.replace("nilai ","")
                status = re.search("(status (flag|closed|opened)*)", str(fakta_sel))
                status = status.group(0)
                status = status.replace("status ", "")
                status_papan.append((row, col, nilai_sel, status))
        return status_papan

    def main(self):
        # udah pasti ukuran sama jumlah bom disetel sebelumnya
        for i in range(self.ukuran):
            self.papan.append([])
            for j in range(self.ukuran):
                self.papan[i].append(0)
        for col, row in self.bombLoc:
            self.papan[col][row] = -1
        self.generateNilai()
        fact_string_ukuran = "(ukuran " + str(self.ukuran) + ")"
        self.env.assert_string(fact_string_ukuran)
        fact_string_jumlah_bom = "(jumlah_bom " + str(self.jumlah_bom) + ")"
        self.env.assert_string(fact_string_jumlah_bom)
        for row in range(self.ukuran):
            for col in range(self.ukuran):
                template = self.env.find_template('sel')
                new_fact = template.new_fact()
                new_fact['col'] = col
                new_fact['row'] = row
                new_fact['nilai'] = clips.Symbol('X')
                new_fact.assertit()
        self.is_finished = 1
        while (self.env.run(1)):
            time.sleep(0.02)
        self.is_finished = 2
        self.printToUI('Program finished!')
    