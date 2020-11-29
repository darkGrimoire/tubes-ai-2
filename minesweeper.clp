(deftemplate sel
    (slot col (default ?NONE))
    (slot row (default ?NONE))
    (slot status (default closed))
    (slot nilai (default ?NONE))
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


(defrule input_selesai
    ?status_input <- (input_complete no)
    (jumlah_bom ?total)
    (ukuran ?x)
    =>
    (retract ?status_input)
    (assert (input_complete yes))
)

(defrule mulai_papan
    ?status_input <- (input_complete yes)
    =>
    (retract ?status_input)
    (assert (game mulai))
)

; (defrule bom_di_atas
;     (empty_koor ?col ?row)
;     (not (atas ?col ?row))
;     (koordinat_bom ?x ?y)
;     ?sel <- (sel (col ?col) (row ?row) (status ?c) (nilai ?d))
;     (test (and (= ?col ?x) (= (+ ?row 1) ?y)))
;     (not (test (= ?d -1)))
;     =>
;     (assert (atas ?col ?row))
;     (retract ?sel)
;     (assert (sel (col ?col) (row ?row) (nilai (+ ?d 1))))
; )

; (defrule bom_di_kanan_atas
;     (empty_koor ?col ?row)
;     (not (kanan_atas ?col ?row))
;     (koordinat_bom ?x ?y)
;     ?sel <- (sel (col ?col) (row ?row) (status ?c) (nilai ?d))
;     (test (and (= (+ ?col 1) ?x) (= (+ ?row 1) ?y)))
;     (not (test (= ?d -1)))
;     =>
;     (assert (kanan_atas ?col ?row))
;     (retract ?sel)
;     (assert (sel (col ?col) (row ?row) (nilai (+ ?d 1))))
; )

; (defrule bom_di_kanan
;     (empty_koor ?col ?row)
;     (not (kanan ?col ?row))
;     (koordinat_bom ?x ?y)
;     ?sel <- (sel (col ?col) (row ?row) (status ?c) (nilai ?d))
;     (test (and (= (+ ?col 1) ?x) (= ?row ?y)))
;     (not (test (= ?d -1)))
;     =>
;     (assert (kanan ?col ?row))
;     (retract ?sel)
;     (assert (sel (col ?col) (row ?row) (nilai (+ ?d 1))))
; )

; (defrule bom_di_kanan_bawah
;     (empty_koor ?col ?row)
;     (not (kanan_bawah ?col ?row))
;     (koordinat_bom ?x ?y)
;     ?sel <- (sel (col ?col) (row ?row) (status ?c) (nilai ?d))
;     (test (and (= (+ ?col 1) ?x) (= (- ?row 1) ?y)))
;     (not (test (= ?d -1)))
;     =>
;     (assert (kanan_bawah ?col ?row))
;     (retract ?sel)
;     (assert (sel (col ?col) (row ?row) (nilai (+ ?d 1))))
; )

; (defrule bom_di_bawah
;     (empty_koor ?col ?row)
;     (not (bawah ?col ?row))
;     (koordinat_bom ?x ?y)
;     ?sel <- (sel (col ?col) (row ?row) (status ?c) (nilai ?d))
;     (test (and (= ?col ?x) (= (- ?row 1) ?y)))
;     (not (test (= ?d -1)))
;     =>
;     (assert (bawah ?col ?row))
;     (retract ?sel)
;     (assert (sel (col ?col) (row ?row) (nilai (+ ?d 1))))
; )

; (defrule bom_di_kiri_bawah
;     (empty_koor ?col ?row)
;     (not (kiri_bawah ?col ?row))
;     (koordinat_bom ?x ?y)
;     ?sel <- (sel (col ?col) (row ?row) (status ?c) (nilai ?d))
;     (test (and (= (- ?col 1) ?x) (= (- ?row 1) ?y)))
;     (not (test (= ?d -1)))
;     =>
;     (assert (kiri_bawah ?col ?row))
;     (retract ?sel)
;     (assert (sel (col ?col) (row ?row) (nilai (+ ?d 1))))
; )

; (defrule bom_di_kiri
;     (empty_koor ?col ?row)
;     (not (kiri ?col ?row))
;     (koordinat_bom ?x ?y)
;     ?sel <- (sel (col ?col) (row ?row) (status ?c) (nilai ?d))
;     (test (and (= (- ?col 1) ?x) (= ?row ?y)))
;     (not (test (= ?d -1)))
;     =>
;     (assert (kiri ?col ?row))
;     (retract ?sel)
;     (assert (sel (col ?col) (row ?row) (nilai (+ ?d 1))))
; )

; (defrule bom_di_kiri_atas
;     (empty_koor ?col ?row)
;     (not (kiri_atas ?col ?row))
;     (koordinat_bom ?x ?y)
;     ?sel <- (sel (col ?col) (row ?row) (status ?c) (nilai ?d))
;     (test (and (= (- ?col 1) ?x) (= (+ ?row 1) ?y)))
;     (not (test (= ?d -1)))
;     =>
;     (assert (kiri_atas ?col ?row))
;     (retract ?sel)
;     (assert (sel (col ?col) (row ?row) (nilai (+ ?d 1))))
; )
(defrule buka_kotak
    ?open <- (open ?col ?row)
    ?sel_closed <- (sel (col ?col) (row ?row) (status closed) (nilai ?x))
    =>
    (retract ?open)
    (retract ?sel_closed)
    ; Assert si sel dengan nilai ambil dari fungsi python
    ; (assert (sel (col ?col) (row ?row) (status opened) (nilai )))
)

(defrule pingin_buka_tapi_gak_ada
    ?open <- (open ?col ?row)
    (not (sel (col ?col) (row ?row) (status ?status) (nilai ?x)))
    =>
    (retract ?open)
)