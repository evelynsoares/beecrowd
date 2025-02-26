<!-- 1045 -->
<?php
    $line = trim(fgets(STDIN));
    list($a, $b, $c) = explode(" ", $line);
    $a = (float)$a;
    $b = (float)$b;
    $c = (float)$c;
    
    if($a >= $b + $c || $b >= $a + $c || $c >= $a + $b) {
        echo "NAO FORMA TRIANGULO\n";
    }
    else {
        if($a * $a == $b * $b + $c * $c || $b * $b == $a * $a + $c * $c || $c * $c == $a * $a + $b * $b) {
            echo "TRIANGULO RETANGULO\n";
        }  
        else if($a * $a > $b * $b + $c * $c || $b * $b > $a * $a + $c * $c || $c * $c > $a * $a + $b * $b) {
            echo "TRIANGULO OBTUSANGULO\n";
        }
        else if($a * $a < $b * $b + $c * $c || $b * $b < $a * $a + $c * $c || $c * $c < $a * $a + $b * $b) {
            echo "TRIANGULO ACUTANGULO\n";
        }
        if($a == $b && $b == $c) {
            echo "TRIANGULO EQUILATERO\n";
        }
        else if($a == $b || $a == $c || $b == $c) {
            echo "TRIANGULO ISOSCELES\n";
        }
    }
?>
