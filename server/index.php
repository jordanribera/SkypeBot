<?php
        header('Content-Type: text/html; charset=utf-8');

        $English_responses = array(
                "generic" => "BEEP BOOP I AM A ROBOT",
                "greeting" => "GREETINGS HUMAN",
                "farewell" => "FAREWELL"
                );

        $Japanese_responses = array(
                "generic" => "私はロボットです",
                "greeting" => "こんにちは、人間",
                "farewell" => "さようなら"
                );

        $Spanish_responses = array(
                "generic" => "Soy un robot",
                "greeting" => "Hola, humano",
                "farewell" => "Adiós"
                );

        $German_responses = array(
                "generic" => "Ich bin ein Roboter",
                "greeting" => "Hallo, menschliche",
                "farewell" => "Auf Wiedersehen"
                );

        $French_responses = array(
                "generic" => "Je suis un robot",
                "greeting" => "Bonjour, humaine",
                "farewell" => "Au revoir"
                );

        $all_responses = array(
                "English" => $English_responses,
                "Japanese" => $Japanese_responses,
                "Spanish" => $Spanish_responses,
                "German" => $German_responses,
                "French" => $French_responses
                );


        if(isset($_POST['message']))
        {
                $response = "";

                $message = $_POST['message'];
                $country = $_POST['sender_country'];
                $language = $_POST['sender_language'];

                if (strtolower($message) == 'hello')
                {

                        $response = $all_responses[$language]["greeting"];

                        if(isset($_POST['sender_fullname'])) $response = $response . ' ' . strtoupper($_POST['sender_fullname']);

                }
                else if (strtolower($message) == 'goodbye')
                {
                        $response = $all_responses[$language]["farewell"];

                        if(isset($_POST['sender_fullname'])) $response = $response . ' ' . strtoupper($_POST['sender_fullname']);
                }
                else
                {

                        $response = $all_responses[$language]["generic"];

                }

                echo $response;

        }

?>