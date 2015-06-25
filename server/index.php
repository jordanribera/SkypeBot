<?php

        $us_responses = array(
                "generic" => "BEEP BOOP I AM A ROBOT",
                "greeting" => "GREETINGS HUMAN",
                "farewell" => "UNTIL NEXT TIME"
                );

        $jp_responses = array(
                "generic" => "私はロボットです",
                "greeting" => "こんにちは、人間",
                "farewell" => "さようなら"
                );

        $all_responses = array(
                "us" => $us_responses,
                "jp" => $jp_responses
                );


        if(isset($_POST['message']))
        {
                $response = "";

                $message = $_POST['message'];
                $country = $_POST['sender_country'];

                if (strtolower($message) == 'hello')
                {

                        $response = $all_responses[$country]["greeting"];

                        if(isset($_POST['sender_fullname'])) $response = $response . ' ' . strtoupper($_POST['sender_fullname']);

                }
                else if (strtolower($message) == 'goodbye')
                {
                        $response = $all_responses[$country]["farewell"];

                        if(isset($_POST['sender_fullname'])) $response = $response . ' ' . strtoupper($_POST['sender_fullname']);
                }
                else
                {

                        $response = $all_responses[$country]["generic"];

                }

                echo $response;

        }

?>