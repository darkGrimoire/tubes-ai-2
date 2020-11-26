import clips


def cetakPapan(papan):
    for i in range(len(papan)):
        print(str(i) + "|", end="")
        for j in range(len(papan[i])):
            print(papan[i][j], end=' ')
        print("")
    print("----------")


if __name__ == "__main__":
    print("Hallo")
    ukuran = 0
    # Di dalam papan tiap koordinat disimpan dalam bentuk [row,col]
    # Sisi Y dari atas ke bawah, Sisi X dari kiri ke kanan
    papan = []
    while ((ukuran < 4) or (ukuran > 10)):
        ukuran = int(input("Masukkan ukuran papan: "))
        if ((ukuran < 4) or (ukuran > 10)):
            print("ukuran tidak valid")
    for i in range(ukuran):
        papan.append([])
        for j in range(ukuran):
            papan[i].append(0)
    jumlah_bom = 101
    while (jumlah_bom > pow(ukuran, 2)):
        jumlah_bom = int(input("Masukkan jumlah bom: "))
        if ((jumlah_bom > pow(ukuran, 2))):
            print("jumlah bom tidak valid")
    for i in range(jumlah_bom):
        lok_bom = input("Masukkan koordinat bom (format 'row,col'): ")
        arr_lok_bom = lok_bom.split(",")
        papan[int(arr_lok_bom[0])][int(arr_lok_bom[1])] = -1
    cetakPapan(papan)
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
    cetakPapan(papan)
