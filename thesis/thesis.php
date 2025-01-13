<?php
    


    $json = trim(file_get_contents("php://input"));
    $data = json_decode($json);

    // echo $data->fullname;
    // echo $data->key1;
    // echo $data->key2;
    
    
    
    // echo "starting ";
    if($data->function == "booktitles")
        $result= exec("C:\Python311\python.exe thesis-booktitles-senond-option.py $data->fullname / $data->key1 /"); /*$data->key2" );*/

    if($data->function == "journals")
        $result= exec("C:\Python311\python.exe thesis-journals-second-option.py $data->fullname / $data->key1 /");/* $data->key2" );*/

    if($data->function == "booktitlesANDjournals")
        $result= exec("C:\Python311\python.exe thesis-booktitlesANDjournals-second-option.py $data->fullname / $data->key1 /");
    // if($data->function == "booktitlesANDjournals")
    //     $result= exec("C:\Python311\python.exe tesingAll.py $data->fullname / $data->key1 /");

    
   
    
    echo $result

    // echo $result_array
    // echo $result
    

?>