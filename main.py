import clips
import re
import time

papan = []
env = clips.Environment()

def cetakPapan():
    global papan

    # Cetak header dari papan
    print("  |", end='')
    for i in range(len(papan)):
        if (i < 10):
            print(str(i)+"  ", end='')
        else:
            print(str(i)+" ", end='')
    print('')
    length = 3 * (len(papan)+1)
    for i in range(length):
        print("-", end="")
    print('')

    # Cetak isi papan
    for row in range(len(papan)):
        if (row < 10):
            print("0", end='')
        print(str(row) + "|", end="")
        for col in range(len(papan[row])):
            print(papan[row][col], end='')
            if (col != ukuran-1):
                if (papan[row][col+1] == -1):
                    print(" ", end="")
                else:
                    print("  ", end="")
        print("")

    # Cetak border bawah dari papan
    for i in range(length):
        print("-", end="")
    print('')


def cetakPapanBasedOnFacts():
    global papan
    daftar_fakta_sel = []
    
    # Masukkan semua fakta mengenai papan
    for fact in env.facts():
        if re.search("\(sel \(col ", str(fact)):
            daftar_fakta_sel.append(fact)
    
    # Cetak header papan
    print("  |", end='')
    for i in range(len(papan)):
        if (i < 10):
            print(str(i)+"  ", end='')
        else:
            print(str(i)+" ", end='')
    print('')
    length = 3 * (len(papan)+1)
    for i in range(length):
        print("-", end="")
    print('')
    
    # Cetak isi papan
    for row in range(len(papan)):
        if (row < 10):
            print("0", end='')
        print(str(row) + "|", end="")
        for col in range(len(papan[row])):
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
            nilai_sel = re.search("(nilai ([0-9]|X|F)*)", str(fakta_sel))
            nilai_sel = nilai_sel.group(0)
            nilai_sel = nilai_sel.replace("nilai ","")
            print(nilai_sel, end='')
            if (col != ukuran-1):
                if (nilai_sel == "-1"):
                    print(" ", end="")
                else:
                    print("  ", end="")
        print("")
    
    # Cetak border bawah papan
    for i in range(length):
        print("-", end="")
    print('')

def printKoordinatBomb():
    global papan
    daftar_fakta_sel = []
    koordinatBomb = []
    
    # Masukkan semua fakta mengenai papan
    for fact in env.facts():
        if re.search("\(sel \(col ", str(fact)):
            daftar_fakta_sel.append(fact)
    
    for row in range(len(papan)):
        for col in range(len(papan[row])):
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
            nilai_sel = re.search("(nilai F)", str(fakta_sel))
            if not nilai_sel:
                continue
            print(f"{row}, {col}")
    
def getNilaiSel(col, row):
    # INGET, di ARRAY disimpen dalam format papan[row][col]
    return papan[row][col]

def printui(msg):
    pass

if __name__ == "__main__":
    print("Hallo")
    env.clear()
    env.define_function(getNilaiSel)
    env.define_function(printui)
    env.load("minesweeper.clp")
    ukuran = 0
    jumlah_bom = 101
    # Di dalam papan tiap koordinat disimpan dalam bentuk papan[row][col]
    # Sisi Y dari atas ke bawah, Sisi X dari kiri ke kanan
    while ((ukuran < 4) or (ukuran > 10)):
        ukuran = int(input("Masukkan ukuran papan: "))
        if ((ukuran < 4) or (ukuran > 10)):
            print("ukuran tidak valid")
    for i in range(ukuran):
        papan.append([])
        for j in range(ukuran):
            papan[i].append(0)
    
    while (jumlah_bom > pow(ukuran, 2)):
        jumlah_bom = int(input("Masukkan jumlah bom: "))
        if ((jumlah_bom > pow(ukuran, 2))):
            print("jumlah bom tidak valid")
    for i in range(jumlah_bom):
        lok_bom = input("Masukkan koordinat bom (format 'row,col'): ")
        arr_lok_bom = lok_bom.split(",")
        papan[int(arr_lok_bom[0])][int(arr_lok_bom[1])] = -1
    for i in range(ukuran):
        for j in range(ukuran):
            if (papan[i][j] != -1):
                continue
            daftar_sel_tetangga = [[i+1, j], [i+1, j+1], [i, j+1],
                                   [i-1, j+1], [i-1, j], [i-1, j-1], [i, j-1], [i+1, j-1]]
            for sel_tetangga in daftar_sel_tetangga:
                if (sel_tetangga[0] < 0 or sel_tetangga[1] < 0 or sel_tetangga[0] >= ukuran or sel_tetangga[1] >= ukuran):
                    continue
                temp = papan[sel_tetangga[0]][sel_tetangga[1]]
                if (temp == -1):
                    continue
                papan[sel_tetangga[0]][sel_tetangga[1]] = temp + 1
    fact_string_ukuran = "(ukuran " + str(ukuran) + ")"
    env.assert_string(fact_string_ukuran)
    fact_string_jumlah_bom = "(jumlah_bom " + str(jumlah_bom) + ")"
    env.assert_string(fact_string_jumlah_bom)
    for row in range(ukuran):
        for col in range(ukuran):
            template = env.find_template('sel')
            new_fact = template.new_fact()
            new_fact['col'] = col
            new_fact['row'] = row
            new_fact['nilai'] = clips.Symbol('X')
            new_fact.assertit()
    count = 1
    while (env.run(5)):
        # print("AGENDA: ")
        # for rule in env.activations():
        #     print(rule)
        # print("FACTS: ")
        # for fact in env.facts():
        #     print(fact)
        # time.sleep(0.02)
        # input()
        print(f"ITERATION: {count}")
        count += 1
    cetakPapanBasedOnFacts()
    print("Koordinat bom:")
    printKoordinatBomb()