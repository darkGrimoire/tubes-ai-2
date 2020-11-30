(deftemplate sel
    (slot col (default ?NONE))
    (slot row (default ?NONE))
    (slot status (default closed))
    (slot nilai (default ?NONE))
)

(deftemplate look_at_cell
    (slot col (default 0))
    (slot row (default 0))
    (slot col_n (default 0))
    (slot row_n (default 0))
)

(deftemplate sel_neighbors
    (slot col (default ?NONE))
    (slot row (default ?NONE))
    (slot flags (default 0))
    (slot closed (default 8))
    (slot total (default 8))
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

(defrule buka_kotak
    (declare (salience 500))
    ?open <- (open ?col ?row)
    ?sel_closed <- (sel (col ?col) (row ?row) (status closed) (nilai ?x))
    (game mulai)
    =>
    (retract ?open)
    (retract ?sel_closed)
    (bind ?nilai (getNilaiSel ?col ?row))
    (assert (sel (col ?col) (row ?row) (status opened) (nilai ?nilai)))
    (assert (sel_neighbors (col ?col) (row ?row) (flags 0) (closed 8) (total 8)))
    (loop-for-count (?i -1 1) do
        (loop-for-count (?j -1 1) do
            (if (not (and (= ?col (+ ?col ?i)) (= ?row (+ ?row ?j)) ))
                then
                (assert (look_at_cell (col ?col) (row ?row) (col_n (+ ?col ?i)) (row_n (+ ?row ?j))))
                (assert (look_at_cell (col (+ ?col ?i)) (row (+ ?row ?j)) (col_n ?col) (row_n ?row)))
            )
        )
    )
)

(defrule buka_flag
    ?open <- (open ?col ?row)
    ?sel <- (sel (col ?col) (row ?row) (status flag) (nilai ?x))
    (game mulai)
    =>
    (retract ?open)
)


(defrule look_tapi_gak_ada
    ?look <- (look_at_cell (col ?col) (row ?row) (col_n ?cn) (row_n ?rn))
    (not (sel (col ?cn) (row ?rn) (status ?status) (nilai ?x)))
    ?sn <- (sel_neighbors (col ?col) (row ?row) (flags ?f) (closed ?c) (total ?t))
    (game mulai)
    =>
    (retract ?look)
    (bind ?c_new (- ?c 1))
    (bind ?t_new (- ?t 1))
    (retract ?sn)
    (assert (sel_neighbors (col ?col) (row ?row) (flags ?f) (closed ?c_new) (total ?t_new)))
    (assert (check ?col ?row))
)

(defrule look_tapi_udah_kebuka
    ?look <- (look_at_cell (col ?col) (row ?row) (col_n ?cn) (row_n ?rn))
    (sel (col ?cn) (row ?rn) (status opened) (nilai ?x))
    ?sn <- (sel_neighbors (col ?col) (row ?row) (flags ?f) (closed ?c) (total ?t))
    (game mulai)
    =>
    (retract ?look)
    (bind ?c_new (- ?c 1))
    (retract ?sn)
    (assert (sel_neighbors (col ?col) (row ?row) (flags ?f) (closed ?c_new) (total ?t)))
    (assert (check ?col ?row))

)

(defrule look_dan_ada
    ?look <- (look_at_cell (col ?col) (row ?row) (col_n ?cn) (row_n ?rn))
    (sel (col ?cn) (row ?rn) (status ?status) (nilai ?x))
    (game mulai)
    =>
    (retract ?look)
    (assert (check ?col ?row))
)

(defrule check_kotak
    ?checking <- (check ?col ?row)
    ?checked_sel <- (sel (col ?col) (row ?row) (status opened) (nilai ?x))
    ?sn <- (sel_neighbors (col ?col) (row ?row) (flags ?f) (closed ?c) (total ?t))
    (game mulai)
    =>
    (if (and (= ?x (+ ?f ?c)) (not (= ?c 0)))
        then
        (loop-for-count (?i -1 1) do
            (loop-for-count (?j -1 1) do
                (assert (flag (+ ?col ?i) (+ ?row ?j)))))
        (retract ?checking)
        (retract ?sn)
        (assert (sel_neighbors (col ?col) (row ?row) (flags (+ ?f ?c)) (closed 0) (total ?t)))
    )
)

(defrule check_kotak_fin
    ?checking <- (check ?col ?row)
    ?checked_sel <- (sel (col ?col) (row ?row) (status opened) (nilai ?x))
    ?sn <- (sel_neighbors (col ?col) (row ?row) (flags ?x) (closed ?c) (total ?t))
    (game mulai)
    =>
    (loop-for-count (?i -1 1) do
        (loop-for-count (?j -1 1) do
            (assert (open (+ ?col ?i) (+ ?row ?j)))))
    (retract ?checking)
    (retract ?sn)
    (assert (sel_neighbors (col ?col) (row ?row) (flags ?x) (closed 0) (total ?t)))
)


(defrule flag_tapi_gak_ada
    ?mark <- (flag ?col ?row)
    (not (sel (col ?col) (row ?row) (status closed) (nilai ?x)))
    (game mulai)
    =>
    (retract ?mark)
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
    (assert (sel (col ?col) (row ?row) (status flag) (nilai F)))
    (assert (jumlah_bom (- ?bom 1)))
    (loop-for-count (?i -1 1) do
        (loop-for-count (?j -1 1) do
            (if (not (and (= ?col (+ ?col ?i)) (= ?row (+ ?row ?j))))
                then
                (assert (addflag (+ ?col ?i) (+ ?row ?j)))
            )
        )
    )
)

(defrule tambah_flag
    ?f <- (addflag ?c ?r)
    ?s <- (sel_neighbors (col ?c) (row ?r) (flags ?fa) (closed ?closed) (total ?t))
    (game mulai)
    =>
    (retract ?f)
    (retract ?s)
    (assert (sel_neighbors (col ?c) (row ?r) (flags (+ ?fa 1)) (closed (- ?closed 1)) (total ?t)))
    (assert (check ?c ?r))
)

(defrule buka_kotak_0
    (declare (salience 200))
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
    (declare (salience 50))
    (sel (col ?col) (row ?row) (status opened) (nilai -1))
    ?game <- (game mulai)
    =>
    (printout t "You lose..." crlf)
    (printui "You lose...")
    (retract ?game)
    (assert (game selesai))
)

(defrule apakah_aq_menang
    (declare (salience 50))
    (jumlah_bom 0)
    ?game_state <- (game mulai)
    =>
    (printout t "You win!!!" crlf)
    (printui "You win!!")
    (retract ?game_state)
    (assert (game selesai))
)


; RULE BERSIH-BERSIH                                ;
; Untuk menghapus facts yang tidak dibutuhkan lagi  ;
; setelah game selesai                              ;

(defrule bersih_bersih_open
    (game selesai)
    ?open <- (open ?x ?y)
    => 
    (retract ?open)
)

(defrule bersih_bersih_check
    (game selesai)
    ?check <- (check ?x ?y)
    =>
    (retract ?check)
)

(defrule bersih_bersih_neighbors
    (game selesai)
    ?neighbor <- (sel_neighbors (col ?c) (row ?r) (flags ?f) (closed ?cl) (total ?t))
    =>
    (retract ?neighbor)
)

(defrule bersih_bersih_look_at_cell
    (game selesai)
    ?look <- (look_at_cell (col ?c) (row ?r) (col_n ?cn) (row_n ?rn))
    =>
    (retract ?look)
)

(defrule bersih_bersih_flag
    (game selesai)
    ?flag <- (addflag ?a ?b)
    =>
    (retract ?flag)

)
