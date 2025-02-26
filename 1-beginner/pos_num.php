//1060
<?php
    $count = 0;
    for($i = 0; $i < 6; $i++) {
        fscanf(STDIN, "%f", $n);
        if ($n > 0 ) $count++;
    }
    echo "$count valores positivos\n"
?>