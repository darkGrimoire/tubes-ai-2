(defrule start
    (declare (salience 500))
    ?init <- (initial-fact)
    =>
    (printout t "Starting program" crlf)
    (retract ?init)
    (assert (data no))
)

(defrule ukuran
    (data no)
    (not (ukuran ?x))
    =>
    (printout t "Masukkan ukuran dari papan minesweeper:" crlf)
    (assert (ukuran =(read)))
)

(defrule jumlah_bom
    (data no)
    (not (total_bom ?x))
    (not (bom_dimasukkan ?y))
    =>
    (printout t "Masukkan jumlah bom pada papan" crlf)
    (assert (total_bom =(read)))
    (assert (bom_dimasukkan 0))
)

(defrule tambah_bom
    (data no)
    (total_bom ?x)
    ?bomb <- (bom_dimasukkan ?y)
    (test (> ?x ?y))
    =>
    (printout t "Masukkan titik X lokasi bom pada papan" crlf)
    (assert (koordinatx_bom =(read)))
    (printout t "Masukkan titik y lokasi bom pada papan" crlf)
    (assert (koordinaty_bom =(read)))
    (retract ?bomb)
    (assert (bom_dimasukkan (+ ?y 1)))
)

(defrule gabung_koordinat
    (declare (salience 10))
    ?bomx <- (koordinatx_bom ?x)
    ?bomy <- (koordinaty_bom ?y)
    =>
    (retract ?bomx)
    (retract ?bomy)
    (assert (koordinat_bom ?x ?y))
)