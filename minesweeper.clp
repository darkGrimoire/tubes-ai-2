(deftemplate sel
    (slot col (default ?NONE))
    (slot row (default ?NONE))
    (slot status (default closed))
    (slot nilai (default ?NONE))
)

(deftemplate sel_prob
    (slot col (default ?NONE))
    (slot row (default ?NONE))
    (slot prob (default ?NONE))
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
    (assert (open 0 0))
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
    (game mulai)
    =>
    (retract ?open)
    (retract ?sel_closed)
    (bind ?nilai (getNilaiSel ?col ?row))
    (assert (sel (col ?col) (row ?row) (status opened) (nilai ?nilai)))
    (loop-for-count (?i -1 1) do
        (loop-for-count (?j -1 1) do
            (assert (check (+ ?col ?i) (+ ?row ?j)))))
)

(defrule flag_kotak
    ?flag <- (flag ?col ?row)
    ?sel_closed <- (sel (col ?col) (row ?row) (status closed) (nilai ?x))
    ?sumbom <- (jumlah_bom ?bom)
    (game mulai)
    =>
    (retract ?flag)
    (retract ?sel_closed)
    (retract ?sumbom)
    (assert (sel (col ?col) (row ?row) (status flag) (nilai ?x)))
    (assert (jumlah_bom (- ?bom 1)))
    (loop-for-count (?i -1 1) do
        (loop-for-count (?j -1 1) do
            (assert (check (+ ?col ?i) (+ ?row ?j)))))
)

(defrule check_kotak
    ?check <- (check ?col ?row)
    ?sel_checked <- (sel (col ?col) (row ?row) (status opened) (nilai ?x))
    (game mulai)
    =>
    (retract ?check)
    (loop-for-count (?k 1 ?x) do
        (loop-for-count (?i -1 1) do
            (loop-for-count (?j -1 1) do
                (assert (count (+ ?col ?i) (+ ?row ?j))))))
)

(defrule count_prob_kotak
    ?count <- (count ?col ?row)
    (sel (col ?col) (row ?row) (status closed) (nilai ?x))
    ?sel_prob <- (sel_prob (col ?col) (row ?row) (prob ?prob))
    =>
    (retract ?count)
    (retract ?sel_prob)
    (assert (sel_prob (col ?col) (row ?row) (prob (+ ?prob 1))))
)

(defrule count_prob_kotak_nol
    ?count <- (count ?col ?row)
    (sel (col ?col) (row ?row) (status closed) (nilai ?x))
    =>
    (retract ?count)
    (assert (sel_prob (col ?col) (row ?row) (prob 1)))
)

(defrule buka_kotak_0
    ?sel_opened <- (sel (col ?col) (row ?row) (status opened) (nilai 0))
    (game mulai)
    =>
    (loop-for-count (?i -1 1) do
        (loop-for-count (?j -1 1) do
            (assert (open (+ ?col ?i) (+ ?row ?j)))))
)

(defrule pingin_buka_tapi_gak_ada
    ?open <- (open ?col ?row)
    (not (sel (col ?col) (row ?row) (status ?status) (nilai ?x)))
    (game mulai)
    =>
    (retract ?open)
)

(defrule pingin_cek_tapi_gak_ada
    ?check <- (check ?col ?row)
    (not (sel (col ?col) (row ?row) (status ?status) (nilai ?x)))
    (game mulai)
    =>
    (retract ?check)
)

(defrule apakah_aq_kalah
    (sel (col ?col) (row ?row) (status opened) (nilai -1))
    ?game <- (game mulai)
    =>
    (printout t "maneh kalah anjing" crlf)
    (retract ?game)
)
