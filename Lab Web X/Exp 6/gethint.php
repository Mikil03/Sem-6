<?php
// Array with names
$names = ["Mikil Lalwani", "Mohan Harwami", "Mitesh Bathija", "Rishi Rajpal"];
// Array with colleges
$colleges = ["Vivekanand Education Society's Institute of Technology (VESIT)", "VJTI", "K K Wagh
Polytechnic Nashik", "Sandip Foundation", "Don Bosco", "TSEC"];
// Get the "q" parameter from URL
$q = isset($_GET['q']) ? $_GET['q'] : '';
// Lookup all hints from array if $q is different from ""
if ($q !== "") {
    $q = strtolower($q);
    $len = strlen($q);
    $hints = array();
    foreach ($names as $name) {
        if (stristr($q, substr($name, 0, $len))) {
            array_push($hints, $name);
        }
    }
    echo implode(", ", $hints);
}
// Get the "c" parameter from URL
$c = isset($_GET['c']) ? $_GET['c'] : '';
// Lookup all hints from array if $c is different from ""
if ($c !== "") {
    $c = strtolower($c);
    $len = strlen($c);
    $hints = array();
    foreach ($colleges as $college) {
        if (stristr($c, substr($college, 0, $len))) {
            array_push($hints, $college);
        }
    }
    echo implode(", ", $hints);
}
