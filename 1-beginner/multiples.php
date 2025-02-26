# 1044
<?php
    fscanf(STDIN, "%d %d", $a, $b);
    
    if(($b % $a) == 0 || ($a % $b) == 0) {
        echo "Sao Multiplos\n";
    }
    else {
        echo "Nao sao Multiplos\n";
    }
?>