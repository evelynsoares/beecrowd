// 1046
<?php
    fscanf(STDIN, "%d %d", $start, $end);
    if($start > $end) {
        $total = 24 -$start + $end;
    }
    elseif($start < $end){
        $total = $end - $start;
    }
    else $total = 24;
    echo "O JOGO DUROU $total HORA(S)\n";
?>