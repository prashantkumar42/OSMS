<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data_num = $_POST["data_num"];

    if($data_num == 1){
        $classes = array();
        for($i=1; $i<=20; $i++){
            array_push($classes, ''.($i+1));
        }
        $num_girls = array();
        for($i=1; $i<=20; $i++){
            array_push($num_girls, ''.($i+1));
        }
        $num_boys = array();
        for($i=1; $i<=20; $i++){
            array_push($num_boys, ''.($i+1));
        }

//        echo $classes[5];
//        print_r($classes);
//        print_r($num_boys);

//        for($i=0; $i<20; $i++){
//            $data[$classes[$i]] = $num_students[$i];
//        }
//        print_r($data);
        $data = new stdClass();
        $data->Categories = $classes;
        $data->Girls = $num_girls;
        $data->Boys = $num_boys;

        $json = json_encode($data, JSON_NUMERIC_CHECK);
        echo $json;
    }
    else if($data_num == 2){
        $classes = array();
        for($i=1; $i<=20; $i++){
            array_push($classes, ''.($i+1));
        }
        $percent_girls = array();
        for($i=1; $i<=20; $i++){
            $tmp = rand(60,90);
            array_push($percent_girls, ''.$tmp);
        }
        $percent_boys = array();
        for($i=1; $i<=20; $i++){
            $tmp = rand(60,90);
            array_push($percent_boys, ''.$tmp);
        }

        $data = new stdClass();
        $data->Subject = "Science";
        $data->Categories = $classes;
        $data->Girls = $percent_girls;
        $data->Boys = $percent_boys;

        $json = json_encode($data, JSON_NUMERIC_CHECK);
        echo $json;
    }
    else if($data_num == 3){
        $percent_girls = array();
        $sum = 100;
        $tmp = 0;
        for($i=1; $i<=5; $i++){
            $tmp = rand(0, $sum);
            $sum -= $tmp;
            array_push($percent_girls, ''.$tmp);
        }
        array_push($percent_girls, ''.$sum);

        $percent_boys = array();
        $sum = 100;
        $tmp = 0;
        for($i=1; $i<=5; $i++){
            $tmp = rand(0, $sum);
            $sum -= $tmp;
            array_push($percent_boys, ''.$tmp);
        }
        array_push($percent_boys, ''.$sum);

        $data = new stdClass();
        $data->Categories = ["TableTennis", "Dance", "Music", "Debate", "VolleyBall", "BasketBall"];
        $data->Girls = $percent_girls;
        $data->Boys = $percent_boys;

        $json = json_encode($data, JSON_NUMERIC_CHECK);
        echo $json;
    }
}
