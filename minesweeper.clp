(deftemplate sel
    (slot col (default ?NONE))
    (slot row (default ?NONE))
    (slot status (default closed))
    (slot nilai (default 0))
)

; Start the program
(defrule start
    (declare (salience 500))
    ?init <- (initial-fact)
    =>
    (printout t "Starting program" crlf)
    (retract ?init)
    (assert (input_complete no))
)

; Ask user for board size
(defrule ukuran
    (input_complete no)
    (not (ukuran ?x))
    =>
    (printout t "Masukkan ukuran dari papan minesweeper:" crlf)
    (assert (ukuran =(read)))
)

; Ask user for amount of bomb
(defrule jumlah_bom
    (input_complete no)
    (not (total_bom ?x))
    (not (bom_dimasukkan ?y))
    =>
    (printout t "Masukkan jumlah bom pada papan" crlf)
    (assert (total_bom =(read)))
    (assert (bom_dimasukkan 0))
)

; Ask for col and row location of one bomb
(defrule tambah_bom
    (input_complete no)
    (total_bom ?total)
    ?bomb <- (bom_dimasukkan ?entry)
    (test (> ?total ?entry))
    =>
    (printout t "Masukkan col lokasi bom pada papan" crlf)
    (bind ?col_bom =(read) )
    (printout t "Masukkan row lokasi bom pada papan" crlf)
    (bind ?row_bom =(read) )
    (retract ?bomb)
    (assert (bom_dimasukkan (+ ?entry 1)))
    (assert (koordinat_bom ?col_bom ?row_bom))
)


(defrule input_selesai
    ?status_input <- (input_complete no)
    (total_bom ?total)
    ?bomb <- (bom_dimasukkan ?entry)
    (test (= ?total ?entry))
    =>
    (retract ?status_input)
    (assert (input_complete yes))
    (retract ?bomb)
)

(defrule mulai_papan
    ?status_input <- (input_complete yes)
    =>
    (retract ?status_input)
    (assert (papan mulai))
)

(defrule buat_sel_kosong_0_0
    ?papan <- (papan mulai)
    (not (empty_koor 0 0))
    =>
    (retract ?papan)
    (assert (empty_koor 0 0))
)
(defrule tambah_sel_kosong
    (empty_koor ?col ?row)
    (ukuran ?size)
    (test (< ?row ?size))
    (test (< (+ ?col 1)  ?size))
    =>
    (assert (empty_koor (+ ?col 1) ?row))
)

(defrule tambah_sel_kosong_pindah_row
    (empty_koor ?col ?row)
    (ukuran ?size)
    (test (< (+ ?row 1) ?size))
    (test (>= (+ ?col 1)  ?size))
    =>
    (assert (empty_koor 0 (+ ?row 1)))
)

(defrule buat_sel
    (declare (salience 10))
    (empty_koor ?col ?row)
    =>
    (assert (sel (col ?col) (row ?row)))
)

(defrule sel_bom
    ?sel <- (sel (col ?a) (row ?b) (status ?c) (nilai 0))
    (koordinat_bom ?x ?y)
    (test (= ?a ?x))
    (test (= ?b ?y))
    =>
    (retract ?sel)
    (assert (sel (col ?a) (row ?b) (nilai -1)))
)



